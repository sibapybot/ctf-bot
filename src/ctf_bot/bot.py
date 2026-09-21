import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()


class CTFBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token: str = os.getenv("DISCORD_BOT_TOKEN", "")

    async def on_ready(self):
        print(f"Logged in as {self.user.name} ({self.user.id})")


def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = CTFBot(command_prefix="!", intents=intents)

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        if message.guild is None:
            if message.content.strip().lower() == "untitledproject":
                await message.reply(
                    "ハロー、UntitledProject。\n\n"
                    "https://ctf.example.com/"
                )
            else:
                await message.reply("...")
            return

        if (
            message.guild.id == 964656515686465608
            and message.channel.id == 1029349704879849482
        ):
            if message.content.strip().lower() == "untitledproject":
                await message.delete()
                await message.author.send(
                    "その名前は、ここで呼ぶものではないようです。\n\n"
                    "もう一度、ここで呼んでみてください。"
                )

        await bot.process_commands(message)

    if not bot.token:
        raise RuntimeError("DISCORD_BOT_TOKEN is not set")

    bot.run(bot.token)
