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

GUILD_ID = 1191346186880286770
TARGET_THREAD_ID = 1551388337263091732  # 対象のフォーラム投稿ID

def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = CTFBot(command_prefix="!", intents=intents)

    @bot.event
    async def on_message(message):
        # BOT自身の発言は無視
        if message.author.bot:
            return

        # DM
        if message.guild is None:
            if message.content.strip().lower() == "untitledproject":
                await message.reply(
                    "ハロー、UntitledProject。\n\n"
                    "https://ctf.sibainu.site/"
                )
            else:
                await message.reply("...")
            return

        # 指定したフォーラム投稿（Thread）のみ
        if (
            message.guild.id == GUILD_ID
            and isinstance(message.channel, discord.Thread)
            and message.channel.id == TARGET_THREAD_ID
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
