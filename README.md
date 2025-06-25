# Insta Sales Bot

This is a simple example of how to use FastAgent to build an Instagram sales bot.

## Setup

First, install uv: https://docs.astral.sh/uv/getting-started/installation/

Then, create a virtual environment and install the dependencies:

```bash
uv venv
source .venv/bin/activate
uv sync
```

### Configure Azure OpenAI

Copy the example secrets file and fill in the Azure OpenAI API key, endpoint, and deployment name.
```bash
cp insta-bot/fastagent.secrets.yaml.example insta-bot/fastagent.secrets.yaml
```

Fill in the Azure OpenAI API key, endpoint, and deployment name.
For more details, see [Azure OpenAI Configuration guide](https://fast-agent.ai/ref/azure-config/#prerequisites)

### Run the agents

```bash
uv run insta-bot/agent_one.py
```

### Run the agents as a MCP server

```bash
uv run insta-bot/agent_one.py --server --transport http --port 8001
```

From another terminal, start the MCP inspector:

```bash
npx @modelcontextprotocol/inspector
```

Choose the `Streamable HTTP` transport type, and the url `http://localhost:8001/mcp`. After clicking the `connect` button, you can interact with the agent from the tools tab. Use the `agent_one_send` tool to send the agent a chat message and see it's response.

## Quickstart guide for FastAgent
Quickstart guide for FastAgent: [here](https://fast-agent.ai/mcp/state_transfer/#step-3-connect-and-chat-with-agent-one)