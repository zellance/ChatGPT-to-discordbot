import openai
import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=settings['!'], intents=intents)
openai.api_key = "YOUR OPENAI KEY HERE"
conversation_history = []


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    message_content = message.content
    if message_content:
        conversation_history.append({"role": "user", "content": message_content})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You're a virtual assistent."}] + conversation_history
    )

    reply = chat.choices[0].message.content
    channel = message.channel
    await channel.send(reply)


bot.run('YOUR DISCORD TOKEN HERE')
