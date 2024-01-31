# The model parameter is responsible for the communication model. initially, there is a gpt-4 model

import asyncio
from Gpt_Client import Completion

async def main() -> str:
    async for chunk in Completion.create(
     model="gpt-4-0613", # model
     messages=[{"role": "user", "content": "hello"}] # messages
     ):
        print(chunk, flush=True, end='')

asyncio.run(main())