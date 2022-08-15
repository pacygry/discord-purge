import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="your prefix here") # add a prefix for your bot, EG. "<" or "!" 

token = "your token here" #add your discord bots token here

@bot.event
async def on_ready():
    print ("the bot is ready!")

#purge command - 
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount:int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
                            
bot.run(token)
