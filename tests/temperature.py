# The temperature parameter indicates the quality of the AI's response. the higher the temperature, the worse the AI's response. The optimal temperature is 0.5 - 0.7

import asyncio
from Gpt_Client import Completion

async def main() -> str:
    async for chunk in Completion.create(
     temperature=0.7, # temperature
     messages=[{"role": "user", "content": "hello world"}] # messages
     ):
        print(chunk, flush=True, end='')

asyncio.run(main())