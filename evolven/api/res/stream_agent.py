import json

from .api_base import ApiBaseObject


class StreamAgent(ApiBaseObject):

    def __init__(self, api):
        self.api = api

    async def ainvoke(self, agent: str, message: str, chat_history=None, **kwargs):

        async for res in self.api.arequest(
            "/html/scripts/api/evo-gpt-api.jsp",
            {
                "question": message,
                "agent": agent,
                "chat_history": chat_history,
                "stream": "true",
                "action": "get",
            },
        ):
            if res:
                yield json.loads(res.replace("data:", "", 1))