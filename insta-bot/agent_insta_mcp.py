import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
agent_app_name = "fast-agent insta_mcp_orchestrator (Instagram MCP controller)"
fast = FastAgent(agent_app_name)


# Define the Instagram MCP agent
@fast.agent(
    name="insta_mcp_agent",
    instruction="""
    You are an Instagram tool agent. You can:
    - Send DMs to users
    - List, search, and read chats and messages
    - Look up users by username or ID
    Use the 'insta_mcp' MCP server to perform all Instagram actions.
    """,
    servers=["insta_mcp"],
    model="azure.gpt-4.1-nano",
    use_history=True,
    human_input=True,
)
async def insta_mcp_agent():
    pass  # Tool agent, no main loop needed


# Define the orchestrator
@fast.orchestrator(
    name="insta_mcp_orchestrator",
    instruction=(
        "You are an Instagram chat assistant. "
        "Plan and execute multi-step tasks using the 'insta_mcp_agent'. "
        "Work iteratively and interactively to achieve the user's goals. "
        "Ask for clarification if the user's request is ambiguous."
    ),
    agents=["insta_mcp_agent"],
    model="azure.gpt-4.1-nano",
    use_history=True,
    human_input=True,
    plan_type="iterative",
)
async def main():
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
