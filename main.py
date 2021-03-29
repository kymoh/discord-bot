import discord, datetime, time
import random
import asyncio
import json
import getopt
import aiohttp
import os
import urllib.parse
import re
import math
import typing
from typing import Optional, List
from random import randint 
from discord.ext import commands
from discord import Embed
from datetime import datetime

client = commands.Bot(command_prefix=commands.when_mentioned_or(';'),case_insensitive=True,help_command=None)



@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(msg):
    for word in filtered_words:    
        if word in msg.content.lower():
           await msg.delete()

    await client.process_commands(msg)    
         

filtered_words = ["censored words"]




@client.command()
@commands.has_permissions(administrator = True)
async def nuke(ctx):
  try:
    pos = ctx.channel.position
    def check(message):
      return message.author == ctx.author and message.channel == ctx.channel
    await ctx.send(f" {ctx.author.mention}, You sure about that? Reply with a 'yes' or 'no'")
    try:
      confirm = await client.wait_for('message', check = check, timeout = 10)
    except asyncio.TimeoutError:
      await ctx.send("Okay no nuking today")
    if confirm.content == "yes":
      await ctx.send(f"Purging {ctx.channel.mention}...")
      new_channel = await ctx.channel.clone()
      await ctx.channel.delete()
      await new_channel.edit(position = pos)
      await new_channel.send("<:okkk:823408627079577630> Nuked This Channel.")
      await new_channel.send("https://tenor.com/view/nuke-nuclear-explosion-gif-14867944")
  except:
    pass


@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, dont u dare")



gif = [
     'https://cdn.weeb.sh/images/rkaqm1twZ.gif',
     'https://cdn.weeb.sh/images/SJx7M0Ft-.gif',
     'https://cdn.weeb.sh/images/ryn_Zg5JG.gif',
     'https://cdn.weeb.sh/images/rJYqQyKv-.gif',
     'https://cdn.weeb.sh/images/HyV5mJtDb.gif',
     'https://imgur.com/o2SJYUS',
     'https://cdn.weeb.sh/images/Hk6JVkFPb.gif',
     'https://cdn.weeb.sh/images/HkK2mkYPZ.gif',
     'https://cdn.weeb.sh/images/SJ-CQytvW.gif',
     ]


@client.command()
async def slap( ctx, member : discord.Member ):    
    embed=discord.Embed(title=None,description=f"{ctx.author.mention} **slapped!** {member.mention}**!**", color=discord.Color.random())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    random_link = random.choice(gif)
    embed.set_image(url=random_link)
    
    await ctx.send(embed=embed)

@client.command()
async def messagecount(ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("There were {} messages in {}".format(count, channel.mention))



@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Loaded ``{extension}`` successfully")


@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unloaded ``{extension}`` successfully")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')    


gify = [
     'https://cdn.weeb.sh/images/SkFLH129z.gif',
     'https://cdn.weeb.sh/images/B1-ND6WWM.gif',
     'https://cdn.weeb.sh/images/B1rZP6b-z.gif',
     'https://cdn.weeb.sh/images/rkkZP6Z-G.gif',
     'https://cdn.weeb.sh/images/HykeDaZWf.gif',
     'https://cdn.weeb.sh/images/SJAfH5TOz.gif',
     'https://cdn.weeb.sh/images/HJqSvaZ-f.gif',
     'https://cdn.weeb.sh/images/SJR-PpZbM.gif',
     'https://cdn.weeb.sh/images/ByI7vTb-G.gif',
     ]

@client.command()
async def punch( ctx, member : discord.Member ):    
    embed=discord.Embed(title=None,description=f"{ctx.author.mention} **punched!** {member.mention}**!**", color=discord.Color.random())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    random_link = random.choice(gify)
    embed.set_image(url=random_link)
    
    await ctx.send(embed=embed)

@punch.error
async def punch_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("mention a person for this command!!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping player (ie. <@797023993591889920>).")




@client.command()
async def geturl(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)


        
@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def deletechannel(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        await nuke_channel.delete()

    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@client.command()
async def dababy(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/720466261267447848/824497178549551104/video0.mp4")


@client.command()
async def mock(ctx, *, message):
    out = ''.join(random.choice((str.upper, str.lower))(c) for c in message)
    await ctx.message.delete()
    await ctx.send(out)


gipy = [
     'https://cdn.weeb.sh/images/HkfgF_QvW.gif',
     'https://cdn.weeb.sh/images/S1a0DJhqG.gif',
     'https://cdn.weeb.sh/images/S1OAduQwZ.gif',
     'https://cdn.weeb.sh/images/H1ui__XDW.gif',
     'https://cdn.weeb.sh/images/r1G3xCFYZ.gif',
     'https://cdn.weeb.sh/images/SJAfH5TOz.gif',
     'https://cdn.weeb.sh/images/S1qX2OJ_Z.gif',
     'https://cdn.weeb.sh/images/ryjJFdmvb.gif',
     'https://cdn.weeb.sh/images/rkV6r56Oz.gif',
     ]

@client.command()
async def hug( ctx, member : discord.Member ):    
    embed=discord.Embed(title=None,description=f"{ctx.author.mention} **hugged!** {member.mention}**!**", color=discord.Color.random())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    random_link = random.choice(gipy)
    embed.set_image(url=random_link)
    
    await ctx.send(embed=embed)

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def deleteallchannels(ctx):
    def check(message) -> bool:
        return ctx.author == message.author

    embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                          description='ARE YOU SURE? THIS WILL DELETE ALL THE CHANNELS, VOICE CHANNELS AND '
                                      'CATEGORIES. THIS ACTION AINT REVERSABLE @everyone')
    await ctx.send(embed=embed)
    try:
        message = await client.wait_for('message', timeout=5.5, check=check)
    except asyncio.TimeoutError:
        await ctx.send('aight, no bombing of channels today')
    else:
        if message.content == 'y':
            await ctx.send('aight, server dead!')

            channels = ctx.guild.channels
            for i in channels:
                try:
                    await i.delete()
                except Exception:
                    pass
        else:
            await ctx.send('aight!')




@client.command()
async def ping(ctx):
  start = time.perf_counter()
  a = await ctx.send("Pinging...")
  end = time.perf_counter()
  dur = (end-start) * 1000
  embed = discord.Embed(title = "Pong!", description = f"**Response Time** \n ```{dur:.2f}ms``` \n **Websocket Latency** \n ```{round(((client.latency) * 1000), 2)}ms```", color=0x2F3136)
  await a.edit(embed = embed)


giphy = [
     'https://cdn.weeb.sh/images/r11as1tvZ.gif',
     'https://cdn.weeb.sh/images/BJO2j1Fv-.gif',
     'https://cdn.weeb.sh/images/B1rZP6b-z.gif',
     'https://cdn.weeb.sh/images/B1VnoJFDZ.gif',
     'https://cdn.weeb.sh/images/HyXTiyKw-.gif',

     'https://cdn.weeb.sh/images/SJAfH5TOz.gif',

     'https://cdn.weeb.sh/images/HJqSvaZ-f.gif',
     'https://cdn.weeb.sh/images/SJR-PpZbM.gif',
     'https://cdn.weeb.sh/images/ByI7vTb-G.gif',
     ]

@client.command()
async def kill( ctx, member : discord.Member ):    
    embed=discord.Embed(title=None,description=f"{ctx.author.mention} **killed!** {member.mention}**!**", color=discord.Color.random())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    random_link = random.choice(giphy)
    embed.set_image(url=random_link)
    
    await ctx.send(embed=embed)

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def deletechannels(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(
        title = 'Sucess',
        description = f'Channel: {channel} has been deleted',
    )
    if ctx.author.guild_permissions.administrator:
        await ctx.send(embed=mbed)
        await channel.delete()


client.run(token)


