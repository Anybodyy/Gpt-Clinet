<h1 align="center">Gpt-Client</h1>

## Author
👤 Anybodyy

* Github: [@Anybodyy](https://github.com/anybodyy)
* Telegram: [@User_With_Username](t.me/RealAnybody)

Thanks to the [@xtekky](https://github.com/xtekky). I was inspired by his project(gpt4free)

## Description
This is a powerful script to communicate with big text AI models like gpt4 or OpenChat for free

## Installing
You can load this lib using pip:
```shell
pip install Gpt-Client
```

## Docs
To communicate with AI, you can use this code:
```python
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
```
More examples in `tests` dir

## License
This project is licensed under the [MIT License](LICENSE).
