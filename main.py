import discord
import asyncio
from discord.ext import commands


class Cutie(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="?", intents=discord.Intents.all())

    async def on_ready(self):
        print(f"ready!! {self.user}")


cutie = Cutie()
# cutie

async def load():
    print(":3")
    await cutie.load_extension("shiggy.chatbot")
    await cutie.load_extension("shiggy.botchat")


asyncio.run(load())
cutie.run("token")
