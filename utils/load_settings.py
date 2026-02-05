import json

import anyio


async def load_language():
    async with await anyio.open_file('assets/settings.json', 'r', encoding='utf-8') as f:
        content = await f.read()
        language_file = json.loads(content)
        language_data = language_file['settings']['language']
        local_server_language = language_data
        return local_server_language