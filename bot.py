import discord
from discord.ext import commands
import datetime
import json
import config

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

with open("versiculos.json", "r", encoding="utf-8") as arquivo:
    versiculos = json.load(arquivo)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.command()
async def versiculo(ctx):
    dia = datetime.datetime.now().timetuple().tm_yday
    
    if dia <= len(versiculos):
        mensagem = versiculos[str(dia)]
    else:
        mensagem = "Deus abençoe seu dia! 🙏"

    await ctx.send(
        f"📖 **Versículo do Dia**\n\n{mensagem}\n\n"
        "⚽ Blessing FC | 🙏 Deus abençoe"
    )

bot.run(config.TOKEN)
