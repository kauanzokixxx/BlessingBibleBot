import discord
from discord.ext import commands
import discord.app_commands
import config
import json
import datetime


# Intents
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Carregar versículos
with open("versiculos.json", "r", encoding="utf-8") as arquivo:
    versiculos = json.load(arquivo)


@bot.event
async def on_ready():
    await bot.tree.sync()

    print("==============================")
    print(f"🤖 Bot online: {bot.user}")
    print("⚽ Blessing FC iniciado")
    print("==============================")


# /ping
@bot.tree.command(
    name="ping",
    description="Mostra a latência do bot"
)
async def ping(interaction: discord.Interaction):

    ms = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong!\n⚡ {ms}ms"
    )


# /ajuda
@bot.tree.command(
    name="ajuda",
    description="Mostra os comandos do bot"
)
async def ajuda(interaction: discord.Interaction):

    embed = discord.Embed(
        title="⚽ Blessing FC Bot",
        description="""
🙏 **Comandos disponíveis**

📖 /versiculo
Mostra o versículo do dia

🏓 /ping
Verifica o bot

⚙️ Mais comandos em breve:

⚽ /jogo
🎯 /treino
📊 /ranking
🏆 /mvp
📅 /calendario

🙏 Deus abençoe!
        """,
        color=0xFFD700
    )

    await interaction.response.send_message(embed=embed)


# /versiculo
@bot.tree.command(
    name="versiculo",
    description="Envia o versículo do dia"
)
async def versiculo(interaction: discord.Interaction):

    dia = str(datetime.datetime.now().timetuple().tm_yday)

    if dia in versiculos:
        mensagem = versiculos[dia]
    else:
        mensagem = "🙏 Deus abençoe seu dia!"

    embed = discord.Embed(
        title="🙏 Versículo do Dia",
        description=f"""
{mensagem}

⚽ **Blessing FC**
🙏 Deus abençoe!
        """,
        color=0xFFD700
    )

    await interaction.response.send_message(embed=embed)


# Iniciar bot
bot.run(config.TOKEN)
