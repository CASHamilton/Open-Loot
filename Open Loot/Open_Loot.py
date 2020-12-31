import discord
import pandas as pd
import numpy
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'loot-', case_insensitive = True) #Setting bot prefix.

f=open("Bot_key.txt", "r") #Opens the file that contains the bot key.
key = f.read()


@client.event
async def on_ready(): #Set the status of the bot to online and show the bot prefix.
    print ('Connection established as {0.user}'.format(client))
  
    await client.change_presence(status=discord.Status.online, activity=discord.Game('loot-info'))

@client.event #Server join message
async def on_guild_join(guild): #Thanks to the GitHub user 0xicl33n for this code! https://gist.github.com/0xicl33n/e5008c5865347aafc644a67455507314 
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hello Everyone! My name is Open Loot. You can open loot crates and fight enemies with me! Start by typing loot-info for info and loot-help for a list of commands!')
        break
    
client.run(key)