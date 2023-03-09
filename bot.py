import asyncio
import discord
from discord.ext import commands
import os
import json
from collections import Counter

client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

@client.event
async def on_ready():
    print('RecipeBot is ready')


@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()

@client.command()
@commands.is_owner()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start('Insert secret here')

asyncio.run(main())
