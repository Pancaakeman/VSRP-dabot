import discord
from discord import Intents, Interaction, Embed
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
import dotenv

bot = commands.Bot(command_prefix="!", intents=Intents.all())  # Initializes Bot user

dotenv.load_dotenv()

token = os.getenv('TOKEN')
statuses = [
    "Making Liveries with Cookie",
    "Making myself with Pancakes",
    "Making a rulebook with Malk",
    "Modding with Mack",
    "Feeling Lazy"
]
status = cycle(statuses)  # Creates a cycle

@tasks.loop(seconds=60)
async def status_change():
    await bot.change_presence(status=discord.Status.do_not_disturb)  # Sets DC Bot status to DND
    await bot.change_presence(activity=discord.CustomActivity(next(status)))  # Goes to the next status from the above list

async def load():
    for filename in os.listdir('./cogs'):  # Lists the relative cogs Directory
        if filename.endswith('.py'):  # Looks for .py files
            await bot.load_extension(f'cogs.{filename[:-3]}')  # removes the .py from found files so cogs can load correctly


@bot.event
async def on_ready():
    await load()  # Loads cogs
    await print("Cogs Loaded")
    status_change.start()
    await bot.tree.sync()  # Syncs commands

async def main():
    print(f"Starting bot ")
    await bot.start(token)  # Starts bot

asyncio.run(main())
