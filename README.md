# Bakery Customer Support Agent

This is an example of how to use FastAgent to build an Instagram sales bot.

## Setup

First, install uv: https://docs.astral.sh/uv/getting-started/installation/

Then, create a virtual environment and install the dependencies:

```bash
uv venv
source .venv/bin/activate
uv sync
```

### Configure LLM

Copy the example secrets file and configure the LLM in `fastagent.secrets.yaml` and `fastagent.config.yaml`

```bash
cp insta_bot/fastagent.secrets.yaml.example insta_bot/fastagent.secrets.yaml
```

**For Azure OpenAI API**
Fill in the Azure OpenAI API key, endpoint, and deployment name.
For more details, see [Azure OpenAI Configuration guide](https://fast-agent.ai/ref/azure-config/#prerequisites)

### Run the MCPs

We have re-configured the MCPs to make them available through `http` protocol.

Setup your instagram `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD` in `.env` inside the `insta-mcp` folder. 

To prevent having your account blocked due to "suspicious login attempt", save your device settings using `cl.dump_settings('/tmp/dump.json')`

For more details: refer here- https://subzeroid.github.io/instagrapi/usage-guide/interactions.html

Then, run the Instagram MCP server:

```bash
uv run insta_mcp/mcp_server.py
```

Next run the Bakery MCP server.

```bash
uv run bakery_mcp/mcp_server.py
```

### Run the Agents

The agents have been implemented using [Fast Agent](https://fast-agent.ai/).
Fast Agent enables you to create and interact with sophisticated Agents and Workflows in minutes. It's multi-modal - supporting Images and PDFs in Prompts, Resources and MCP Tool Call results.

The Bakery Assistant Agents are located in `agent_bakery_assistant.py`. You can interact directly with this assistant using the following command:

```bash
cd insta_bot
uv run agent_bakery_assistant.py
```

You can also run the bakery assistant as an MCP server:

```bash
uv run agent_bakery_assistant.py --server --transport http --port 8001
```

From another terminal, start the Instagram Manager Agent:

```bash
uv run agent_insta_manager.py
```


### Debugging MCPs

Run the inspector:

```bash
npx @modelcontextprotocol/inspector
```

Choose the `Streamable HTTP` transport type, and the url `http://localhost:4300/bakery-mcp`. After clicking the `connect` button, you can interact with the MCP from the tools tab.
