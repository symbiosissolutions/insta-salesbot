import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Instagram Sales Assistant")


@fast.agent(
    name="Instagram DM Manager",
    instruction=(
        """
        You are an Instagram DM Manager at Pumpernickel Bakery.
        Your task is to fetch and return all pending chat threads using the insta mcp tools made available to you.
        You must return a structured list where each chat thread includes the following details:
        1.thread_id 2.username and  3.user_id
        The format should be a JSON array of threads.
        Do not return any message content at this stage— only metadata about the thread.
        If no pending threads are found, return an empty list.
        """
    ),
    model="azure.gpt-4.1-nano",
    servers=["insta_mcp"],
)
async def main():
    async with fast.run() as agent:
        await agent.interactive("Instagram DM Manager")


if __name__ == "__main__":
    asyncio.run(main())
