from aiohttp import ClientSession
from typing import Text


class Client:
    def __init__(self, token: Text, *, session: ClientSession, user_agent: str=...) -> None: ...

    async def request(self, query: str, operation: str=..., variables: dict=...) -> dict: ...
