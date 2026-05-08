<div align="center">

# Self Healing Infrastructure MCP

**MCP server for self healing infrastructure mcp operations**

[![PyPI](https://img.shields.io/pypi/v/meok-self-healing-infrastructure-mcp)](https://pypi.org/project/meok-self-healing-infrastructure-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

Self Healing Infrastructure MCP provides AI-powered tools via the Model Context Protocol (MCP).

## Tools

| Tool | Description |
|------|-------------|
| `node_health_check` | Check health of infrastructure nodes including CPU, memory, disk, and GPU. |
| `cluster_health_check` | Check health of all 9 nodes in the cluster. |
| `restart_service` | Restart a failed service with automatic rollback on repeated failures. |
| `cost_report` | Generate infrastructure cost report with breakdown by service, region, and resou |
| `auto_remediate` | Automatically remediate common infrastructure issues using predefined playbooks. |
| `gpu_orchestration` | Orchestrate GPU allocation across the 9-node cluster. |
| `failover_decision` | Determine failover action for a failed node in the cluster. |

## Installation

```bash
pip install meok-self-healing-infrastructure-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "self-healing-infrastructure-mcp": {
      "command": "python",
      "args": ["-m", "meok_self_healing_infrastructure_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 7 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
