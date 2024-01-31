# full tests

import asyncio
from Gpt_Client import Completion

async def main() -> str:
    async for chunk in Completion.create(
     model="gpt-4-0613", # model
     temperature=0.7, # temperature
     system_prompt="You're ChatGpt, big trained AI.", # system prompt
     messages=[{"role": "user", "content": "hello"}] # messages
     ):
        print(chunk, flush=True, end='')

asyncio.run(main())