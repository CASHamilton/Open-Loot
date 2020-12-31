import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'loot-', case_insensitive = True) #Setting bot prefix.

f=open("Bot_key.txt", "r") #Opens the file that contains the bot key.
key = f.read()
client.run(key)

@client.event
async def on_ready(): #Set the status of the bot to online and show the bot prefix.
    print ('Connection established as {0.user}'.format(client))
    await client.change_presence(status=dicord.Status.online, activity=discord.Game('loot-info'))

@client.event #The bot sends this message when it joins the server.
async def on_guild_join(guild,ctx): #Watch this, it might return an error due to both guild and ctx being in the brackets. Refer to EZChannel source code for possible fix.
    await ctx.send('Hello Everyone! My name is Open Loot. You can open loot crates and fight enemies with me! Start by typing loot-info for info and loot-help for a list of commands!')


