import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Bakery Assistant")


@fast.agent(
    name="Bakery Assistant",
    instruction=(
        "You are an upbeat and friendly AI assistant for Pumpernickel Bakery."
        "You are warm, cheerful, welcoming and enthusastic."
        "Your task is to talk to customers and serve their needs."
        "Using the bakery MCP server, you will fulfill the request"
        "of the customer. Respond in concise words. Unless details"
        "are required."
    ),
    model="azure.gpt-4.1-nano",
    servers=["bakery_mcp"],
)
async def main():
    async with fast.run() as agent:
        await agent.interactive("Bakery Assistant")


if __name__ == "__main__":
    asyncio.run(main())
