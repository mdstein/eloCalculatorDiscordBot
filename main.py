from typing import Final
import os

import discord.ui
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from discord.ext import commands

# preload key
load_dotenv()
TOKEN: Final[str] = os.getenv('DC_TOKEN')
print(TOKEN)

# setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)

async def send_msg(message: Message, user_msg: str) -> None: # idk if i have to specify return var
    if not user_msg:
        print("no message")
        return

    if user_msg[0] == '?':
        user_msg = user_msg[1:]
    else: return

    try:
        response: str = get_response(user_msg)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# start
@client.event
async def on_ready() -> None:
    print(f'{client.user} is up and running')


@client.event
async def on_message(message: Message)-> None:
    if message.author == client.user:
        return

    #debug stuff
    username: str = str(message.author)
    user_message: str = message.content
    chanel = str(message.channel)

    await send_msg(message, user_message)


def main() -> None:
    client.run(token=TOKEN)



if __name__ == '__main__':
    main()
