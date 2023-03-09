import json
import discord
from discord.ext import commands
from collections import Counter

class Recipe(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Recipe is loaded')


    @commands.command()
    async def pingRecipe(self, ctx):
        await ctx.send('Pong from Recipe!')

    @commands.command()
    async def recipe(self, ctx, *, input):
        input = input.lower()
        item_clean = input.replace(" ", "_")
        filename = "minecraft-data\\recipes\\" + item_clean + ".json"

        file = open(filename, "r")
        data = json.load(file)

        count = Counter()
        for i in data['pattern']: # count items in pattern
            count.update(i)
        # print(count)

        recipe = ""
        for i in data['key']:
            item = data['key'][i]['item']
            recipe = recipe + str(count[i]) + " " + item[10:] + "\n"
            # print(count[i], item[10:]) # prints: "<item count> <item>"

        file.close()
        await ctx.send(recipe)


async def setup(client):
    await client.add_cog(Recipe(client))
