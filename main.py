import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()

class CTFBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token: str = os.getenv('DISCORD_BOT_TOKEN')

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')

intents = discord.Intents.default()
intents.message_content = True

bot = CTFBot(command_prefix='!', intents=intents)



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
                "https://ctf.example.com/"
            )
        else:
            # 失敗パターン
            await message.reply("...")

        return
    
    # UniProjectサーバーの指定チャンネル
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


bot.run(bot.token)