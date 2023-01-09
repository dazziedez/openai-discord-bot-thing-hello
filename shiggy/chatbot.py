import openai
from discord.ext import commands

openai.api_key = "apikey"
chat = channel_id


async def gen(query):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=1,
        max_tokens=1920
    )
    api_json = response["choices"][0]["text"]
    print(api_json)
    return api_json


class OpenAI(commands.Cog):
    def __init__(self, cutie):
        super().__init__()
        self.cutie = cutie

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != chat or message.author.bot or message.content.startswith(">"):
            return

        async with message.channel.typing():
            q = await gen(message.content)
            await message.channel.send(q)


async def setup(cutie):
    await cutie.add_cog(OpenAI(cutie))
