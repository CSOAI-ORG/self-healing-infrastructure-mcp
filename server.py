#!/usr/bin/env python3
"""Self-Healing Infrastructure MCP Server — Auto-recovery and cost optimization for clusters."""

import sys, os
sys.path.insert(0, os.path.expanduser('~/clawd/meok-labs-engine/shared'))
from auth_middleware import check_access

import json, subprocess, os
from datetime import datetime, timezone
from collections import defaultdict
from mcp.server.fastmcp import FastMCP

FREE_DAILY_LIMIT = 15
_usage = defaultdict(list)
def _rl(c="anon"):
    now = datetime.now(timezone.utc)
    _usage[c] = [t for t in _usage[c] if (now-t).total_seconds() < 86400]
    if len(_usage[c]) >= FREE_DAILY_LIMIT: return json.dumps({"error": f"Limit {FREE_DAILY_LIMIT}/day"})
    _usage[c].append(now); return None

mcp = FastMCP("self-healing-infrastructure", instructions="MEOK AI Labs MCP Server")

@mcp.tool()
def node_health_check(node_name: str, api_key: str = "") -> str:
    # Simulated health check
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}
    if err := _rl(): return err

    metrics = {"cpu_percent": 45, "memory_percent": 62, "disk_percent": 78, "gpu_temp_c": 72}
    healthy = all(v < 85 for v in metrics.values())
    return {"node": node_name, "healthy": healthy, "metrics": metrics}

@mcp.tool()
def restart_service(service_name: str, node_name: str, api_key: str = "") -> str:
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}
    if err := _rl(): return err

    return {"service": service_name, "node": node_name, "action": "restart_initiated", "status": "pending"}
    return {"service": service_name, "node": node_name, "action": "restart_initiated", "status": "pending"}

@mcp.tool()
def cost_report(nodes: list, cost_per_hour: float, api_key: str = "") -> str:
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}
    if err := _rl(): return err

    total_hours = len(nodes) * 24 * 30
    cost = total_hours * cost_per_hour
    return {"nodes": len(nodes), "monthly_estimate": round(cost, 2), "recommendation": "Consolidate idle nodes" if len(nodes) > 5 else "Optimal"}

@mcp.tool()
def auto_remediate(issue: str, node_name: str, api_key: str = "") -> str:
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}
    if err := _rl(): return err

    actions = {
        "high_cpu": "scale_out_requested",
        "high_memory": "restart_service_requested",
        "disk_full": "cleanup_logs_requested",
        "gpu_overheat": "throttle_requested",
    }
    return {"issue": issue, "node": node_name, "action": actions.get(issue.lower(), "manual_review_required"), "automated": issue.lower() in actions}

if __name__ == "__main__":
    mcp.run()
