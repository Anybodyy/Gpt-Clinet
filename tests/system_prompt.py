# The system_prompt parameter "suggests" an AI role (system prompt)

import asyncio
from Gpt_Client import Completion

async def main() -> str:
    async for chunk in Completion.create(
     system_prompt="You're DaniilSV, AI clone of brawl stars mod creator", # system prompt
     messages=[{"role": "user", "content": "hello"}] # messages
     ):
        print(chunk, flush=True, end='')

asyncio.run(main())