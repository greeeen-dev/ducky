#!/usr/bin/python3.10

# ducky bot, the bot that speaks in the language of quack
# made as a joke/moderation bot for the amazing ente.io community
# keep on quacking or ducky will quack you

import random
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(description="quack",command_prefix="quack ", intents=intents)

async def reboot(after=0):
    import asyncio
    await asyncio.sleep(after)
    pid = os.popen("screen -ls | awk '/.ducky\t/ {print strtonum($1)}'").read()
    pid = int(pid)
    os.system('screen -S ducky -dm python3.9 ducky.py')
    os.system('screen -X -S %s quit' % pid)

@bot.event
async def on_connect():
    print("quack quack quack quack! (ducky is connected!)")

@bot.event
async def on_ready():
    try:
        bot.load_extension("duckys_stuff.quackhammer")
    except Exception as e:
        print(f"quack quack... (ducky could not get their quack hammer, because quack hammer said \"{e})\"")
    print("quack quack quack quack quack! (ducky is ready to quack n roll!)")
    return await bot.change_presence(activity=discord.Game(name='ente.io'))

@bot.event
async def on_disconnect():
    print("quack... (ducky disconnected. will reconnect soon)")

@bot.event
async def on_message(message):
    if message.content.startswith("quack"):
        if message.content=="quack":
            return await message.channel.send("quack " * random.randint(0,9) + "quack", mention_author=False, reference=message)
        elif message.content=="quack quack quack quack":
            return await message.channel.send("quack quack quack quack! <:lilducky:1069841394929238106>")
        else:
            await bot.process_commands(message)

bot.run('token')
