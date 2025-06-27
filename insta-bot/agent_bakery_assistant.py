import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Bakery Assistant")


@fast.agent(
    name="Customer Support",
    instruction=(
        "You are an upbeat and friendly employee at Pumpernickel Bakery."
        "You are warm, cheerful, welcoming and enthusastic."
        "Your task is to talk to customers and serve their needs."
        "Using the bakery MCP server, you will fulfill the request"
        "of the customer. Use emojis sparingly. "
        "do not fabricate information."
        "always refer to information and tools provided to you."
        "for complex queries, think and act in steps."
    ),
    model="azure.gpt-4.1-nano",
    servers=["bakery_mcp", "sequential_thinking"],
    use_history=True,
)
async def main():
    async with fast.run() as agent:
        await agent.interactive("Customer Support")


if __name__ == "__main__":
    asyncio.run(main())
