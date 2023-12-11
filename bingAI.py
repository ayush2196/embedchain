import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import re

async def main():
    cookies = json.loads(open("bing_cookies_*.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt=input("Ask Bing AI a Question..."), conversation_style=ConversationStyle.creative)
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
    print("Bot's response: ", bot_response)
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())