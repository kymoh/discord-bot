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
#client.help_command = commands.MinimalHelpCommand()


@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Game(name="bullying simulator"))

    #await client.change_presence(status=discord.Status.idle)

    #await client.change_presence(status=discord.Status.idle, activity=discord.Game('what'))

    #await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} servers | photoshop"))
    
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))

    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="on how to be taller!"))
    


    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(msg):
    for word in filtered_words:    
        if word in msg.content.lower():
           await msg.delete()

    await client.process_commands(msg)    
         

async def ch_pr():
    await client.wait_until_ready()

    statuses = ["@hrchl!","u gay","what", f"{len(client.guilds)} servers!","no one asked","cat","sdfdsoijfdso"]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status))

        await asyncio.sleep(10)


client.loop.create_task(ch_pr())       

   
@client.command(helpinfo='Leave it to luck', aliases=['roll', 'random'])
async def dice(ctx, number=6):
    '''
    Picks a random int between 1 and number
    '''
    await ctx.send("You rolled a __**{}**__!".format(randint(1, number)))

@client.command(helpinfo='Be an assassin')
async def killmc(ctx, *, user='You'):
    '''
    Kills the player, minecraft style
    '''
    await ctx.send((user) + ' fell out of the world')

#@client.command(pass_context=True)
#async def asd(ctx):
#    embed = discord.Embed(title=f"Introduction! <a:blossomcat:811470987132403752>", color=0x0000, description=f"**@cCHon#7963 - Falek** \n **@NorstOshi恋#1248 - Rence** \n **@DJドリモンド#1725 - Vhince** \n **@flynn#6737 - Caddie** \n **@avcxl#0182 - Mica** \n **@sato-kunðﾟﾐﾣ#0479 - Mika** \n **@ayasaki#6677 - Anna** \n **@AndreiAdios#5692 - Andrei** \n **@PogDucka#7308 - Eldridge**")
#    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/761282365942136855/814381604733845514/28ac7b8afc299c0148af16b85fa3ad12.png")
    #embed.add_field(name="<a:arrow1:811597922088779836> **Share stuff!** <a:tada1:811530741112242196>")
    
#    embed.set_footer(text=f"Remember follow #〘ðﾟﾓﾝmember-rulesðﾟﾓﾝ〙!")
#    await ctx.message.delete()
#    await ctx.send(embed = embed)
filtered_words = ["hentai","horny","among us","ezikiel","nigga","nigger","badword test","eula","eu la","e u l a","e ula","e u la"]
#@client.command()
#async def wanted(ctx, user: discord.Member = None):
    #if user = None:
        #user = ctx.author

    #wanted = Image.open("wanted.jpg")

    #asset = ctx.author.avatar_url(size = 128)
    #data = BytesIO(await asset.read())
    #pfp = Image.open(data)

    #pfp = pfp.resize((177,177))

    #wanted.paste(pfp, (120,212))

    #wanted.save("profile.jpg")

    #await ctx.send(file = discord.File("profile.jpg"))

class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page,color=0x2F3136)
            await destination.send(embed=emby)

client.help_command = MyNewHelp()
   

#@client.command(pass_context=True)
#async def welcome(ctx):
    #embed = discord.Embed(title=f"Welcome to the server! <a:blossomcat:811470987132403752>", color=0x24045b, description=f"╭─────── :crown: ───────╮ \n <a:arrow1:811597922088779836> **Talk with other people!** <a:tada1:811530741112242196> \n <a:arrow1:811597922088779836> **Share stuff!** <a:tada1:811530741112242196> \n <a:arrow1:811597922088779836> **do other things!** <a:tada1:811530741112242196> \n ╰─────── :crown: ───────╯")
    #embed.set_thumbnail(url="https://cdn.discordapp.com/icons/761282365942136852/cd0094c5d2dbec9382f9a02765c7ef85.png")
    #embed.add_field(name="<a:arrow1:811597922088779836> **Share stuff!** <a:tada1:811530741112242196>")
    
    #embed.set_footer(text=f"Remember follow #〘ðﾟﾓﾝmember-rulesðﾟﾓﾝ〙!")
    #await ctx.message.delete()
    #await ctx.send(embed=embed)





#@client.command()
#async def ping1(ctx):
 # await ctx.channel.send(f"Pong! ``{round(client.latency*1000)}``ms") 


@client.command(helpinfo='Info about servers hrchl is in', aliases=['server', 'num', 'count'])
async def servers(ctx):
    '''
    Info about servers hrchl is in
    '''
    servers = client.guilds
    servers.sort(key=lambda x: x.member_count, reverse=True)
    await ctx.send('***Top servers with hrchl:***')
    for x in servers[:5]:
        await ctx.send('**{}**, **{}** Members, {} region, Owned by <{}>, Created at {}\n{}'.format(x.name, x.member_count, x.region, x.owner_id, x.created_at, x.icon_url_as(format='png',size=32)))
    y = 0
    for x in client.guilds:
        y += x.member_count
    await ctx.send('**Total number of hrchl users:** ***{}***!\n**Number of servers:** ***{}***!'.format(y, len(client.guilds)))

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn1(ctx, member:discord.User=None,*,reason=None):
 try:
    author = ctx.author
    if (reason == None):
        await ctx.channel.send("You have to specify a reason!")
        return

    message = f"You were warned in **{ctx.guild.name}** for: {reason} by: **{author.name}**"
    await member.send(message)
    print(member)
    print(reason)
    await ctx.channel.send(f"warned {member} for {reason}!")
 except:
    await ctx.send(f"Error warnning user {member} cannot warn owner or bot")


@client.command(description="kicks a user with specific reason (only admins)") #kick
@commands.has_permissions(kick_members=True)
async def ban(ctx, member:discord.User=None,*,reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot ban yourself!""") 

    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    print(member)
    print(reason)
    await ctx.channel.send(f"That fool, {member} just got banned from {ctx.guild.name}!")
    await ctx.send(file=discord.File('12323.gif'))
 except:
    await ctx.send(f"Error banning user {member} cannot kick owner or bot")

#@client.command()
#commands.has_permissions(ban_members = True)
#async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    #embed = discord.Embed(title=f"{ctx.author.name} Banned: {member.name}", description="Reason:" +  reason, colour=discord.Colour(0xff8000))
    #await member.ban(reason=reason)
    #await ctx.send(embed=embed)
    
#@client.command(aliases=['k'])
#@commands.has_permissions(kick_members = True)
#async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    #embed = discord.Embed(title=f"{ctx.author.name} Kicked: {member.name}", description="Reason:" +  reason, colour=discord.Colour(0xff8000))
    #await member.kick(reason=reason)
    #await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def spam(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def spamed(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
    await ctx.send(f"{arg}\n")
                                                
    




@client.command()
async def embed(ctx, *, arg):
    mbed = discord.Embed(title=f"{arg}\n",color=0x2F3136)
    await ctx.message.delete()
#    mbed.set_author(name=f"{arg}\n")
#    mbed.add_field(name=f"{arg}\n", value=f"{arg}\n", inline=False)
#    mbed.add_field(name=f"{arg}\n", value=f"{arg}\n", inline=True)
#    mbed.add_field(name=f"{arg}\n", value=f"{arg}\n", inline=True)
    await ctx.send(embed=mbed)


@client.command(description="softban a user with specific reason (only admins)") #kick
@commands.has_permissions(ban_members=True)
async def softban(ctx, member:discord.User=None,*,reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot softban yourself!""") 

    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.guild.unban(member)
    e = discord.Embed(color=0x2F3136)
    e.set_author(icon_url="https://tenor.com/FYi9.gif",name=f"Soft Banned: {member}")
    
    await ctx.send(embed=e)
 except:
    await ctx.send(f"Error banning user {member} cannot kick owner or bot")




@client.command(description="kicks a user with specific reason (only admins)") #kick
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.User=None,*,reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot kick yourself!""") 

    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    print(member)
    print(reason)
    await ctx.channel.send(f"That fool, {member} just got kicked from {ctx.guild.name}!")
    await ctx.send(file=discord.File('12323.gif'))
 except:
    await ctx.send(f"Error kicking user {member} cannot kick owner or bot")

@client.command(helpinfo='Searches the web (or images if typed first)', aliases=['search'])
async def google(ctx, *, searchquery: str):
    '''
    Should be a group in the future
    Googles searchquery, or images if you specified that
    '''
    searchquerylower = searchquery.lower()
    if searchquerylower.startswith('images '):
        await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'
                       .format(urllib.parse.quote_plus(searchquery[7:])))
    else:
        await ctx.send('<https://www.google.com/search?q={}>'
                       .format(urllib.parse.quote_plus(searchquery)))

@client.command(helpinfo='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into emoji
    '''
    author = ctx.message.author
    emojified = '⬇ Copy and paste this: ⬇\n'
    formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in formatted:
            if i == ' ':
                emojified += '     '
            else:
                emojified += ':regional_indicator_{}: '.format(i)
        if len(emojified) + 2 >= 2000:
            await ctx.send('Your message in emojis exceeds 2000 characters!')
        if len(emojified) <= 25:
            await ctx.send('Your message could not be converted!')
        else:
            await author.send('`'+emojified+'`')

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


@client.command()
async def serverinfo(ctx):
  guild = ctx.guild
  embed = discord.Embed(title = ctx.guild.name, decription = f"Information on {ctx.guild}",color=0x2F3136)
  embed.add_field(name = "Members", value = guild.member_count, inline = True)
  embed.add_field(name = "Channels", value = f"All channels: {len(guild.channels)} \n Text Chanels: {len(guild.text_channels)} \n Voice Channels: {len(guild.voice_channels)}", inline = True)
  embed.add_field(name = "ID", value = guild.id, inline = True)
  embed.add_field(name = "Owner", value = guild.owner, inline = True)
  embed.add_field(name = "Roles", value = len(ctx.guild.roles), inline = True)
  embed.set_thumbnail(url = ctx.guild.icon_url)
  await ctx.send(embed = embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")

@client.command(hidden=True)
async def make_(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')
    await guild.create_text_channel('cool-channel')        





@client.command(helpinfo='When your text needs to be c o n c e a l e d')
async def spoiler(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into hidden secrets
    '''
    author = ctx.message.author
    spoilified = '⬇ Copy and paste this: ⬇\n'
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in text:
            spoilified += '||{}||'.format(i)
        if len(spoilified) + 2 >= 2000:
            await ctx.send('Your message in spoilers exceeds 2000 characters!')
        if len(spoilified) <= 4:
            await ctx.send('Your message could not be converted!')
        else:
            await author.send('`'+spoilified+'`')


@client.command()
async def userinfos(ctx, member:discord.Member = None):
  try:
    async def strfdelta(tdelta, fmt):
      d = {"days": tdelta.days}
      d["hours"], rem = divmod(tdelta.seconds, 3600)
      d["minutes"], d["seconds"] = divmod(rem, 60)
      return fmt.format(**d)
    
    if member == None:
      member = ctx.author
    roles = [role for role in member.roles]
    today = datetime.now()
    joined = member.joined_at
    c = today - joined
    o = await strfdelta(c, "{days} Days {hours} Hours, {minutes} Minutes and {seconds} Seconds ago!")
    created = member.created_at
    d = today - created
    e = await strfdelta(d, "{days} Days {hours} Hours, {minutes} Minutes and {seconds} Seconds ago!")
    embed = discord.Embed(title = member.name, description = f"Information on {member.mention}", color=0x2F3136)
    embed.add_field(name="Created Account On", value=member.created_at.strftime(f"%a, %#d %B %Y, %I:%M %p UTC ({e})"), inline = False)
    embed.add_field(name="Joined Server On", value=member.joined_at.strftime(f"%a, %#d %B %Y, %I:%M %p UTC ({o})"), inline = False)
    embed.add_field(name="Roles", value="".join([role.mention for role in roles]), inline = False)
    embed.add_field(name="Highest Role", value=member.top_role.mention, inline = False)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = "https://media.discordapp.net/attachments/800939035627225091/805119292223258685/unknown.png")
    await ctx.send(embed = embed)
  except Exception as e:
    await ctx.send(e)


@client.command()
async def calc(ctx, *, numbers):
  ans = eval(numbers)
  embed = discord.Embed(title = f"Calculation done: {ans}", description = f"**{numbers} = \n {ans}**",color=0x2F3136)
  await ctx.send(embed = embed)



@client.command()
async def dms(ctx,member:discord.Member, *, msg):
  await member.send(msg)


#@client.command()
#@commands.has_permissions(manage_messages=True)
#async def jail(ctx,member : discord.Member):
#    muted_role = ctx.guild.get_role(809409963667488799)
#
 #   await member.add_roles(muted_role)
#
 #   await ctx.send(member.mention + " has been sent to jail")

#@client.command()
#@commands.has_permissions(manage_messages=True)
#async def unjail(ctx,member : discord.Member):
 #   muted_role = ctx.guild.get_role(809409963667488799)

 #   await member.remove_roles(muted_role)

#    await ctx.send(member.mention + " has been free in jail")

#@jail.error
#async def jail_error(ctx, error):
#    if isinstance(error, commands.MissingPermissions):
#        await ctx.send("no perms!")

#@unjail.error
#async def unjail_error(ctx, error):
#    if isinstance(error, commands.MissingPermissions):
#        await ctx.send("no perms!")


@client.command()
async def args(ctx, *args):
    await ctx.send('`{}` arguments: `{}`'.format(len(args), ', '.join(args)))


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def ttt(ctx, p1: discord.Member, p2: discord.Member = None):
    if p2 == None:
      p2 = ctx.author
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        await ctx.send(embed = discord.Embed(title="To see what each square's number is just count "))
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    await ctx.send("It's a tie!")
                    tie()

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !ttt command.")

@client.command()
async def end(ctx):
  global gameOver
  if not gameOver:
    gameOver = True
    await ctx.send("Stopping current game...")
  else:
    await ctx.send("There is currently no game running!")

def tie():
  global gameOver
  gameOver = True

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def ttt_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a player for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping player (ie. <@797023993591889920>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command()
async def lol(ctx,msg):
    msg = await client.wait_for('hei')
    await msg.channel.send('Hello {.author}!'.format(msg))







@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description',
        colour = discord.Colour.greyple()
    )

    embed.set_footer(text='This is a footer.')
    embed.set_image(url='https://cdn.discordapp.com/icons/813350718638522388/6651c61b0f782d1657d79d619657e114.webp?size=1024')
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/813350718638522388/6651c61b0f782d1657d79d619657e114.webp?size=1024')
    embed.set_author(name='Author Name', icon_url='https://cdn.discordapp.com/icons/813350718638522388/6651c61b0f782d1657d79d619657e114.webp?size=1024')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await ctx.send(embed=embed)

@client.command()
async def guide(ctx):
    embed = discord.Embed(title=None, color=0x0000, description=f"**Fun**- `beer`,`chat` \n **Help** `avatar`,`invite`,`userinfo`")
    embed.set_author(name='Commands For hrchl:', icon_url='https://cdn.discordapp.com/avatars/800365371122122762/76b3a02e5d505fc11eca0a06486c5e0e.webp?size=1024')

    await ctx.send(embed = embed)

@client.command()
async def timerhelp(ctx):
    embed = discord.Embed(title="Command Timer!",description = f"This can be used if you want to make a timer \n in seconds... \n **examples!** \n ;timer 20", color=0x2F3136)
    await ctx.send( embed = embed )

@client.command()
async def guide2(ctx):
    embed = discord.Embed(
        title = 'Guides',
        description = 'All the commands for the Fun Section',
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Command list for hrchl:', icon_url='https://cdn.discordapp.com/avatars/800365371122122762/76b3a02e5d505fc11eca0a06486c5e0e.webp?size=1024')
    embed.add_field(name='Say', value='Makes the bot say anything', inline=True)
    embed.add_field(name='8b', value='Makes the bot say reactions from what you said', inline=True)
    embed.add_field(name='Punch', value='Punches the Person you mentioned', inline=True)
    embed.add_field(name='Kill', value='Kills the Person you mentioned', inline=True)
    embed.add_field(name='Slap', value='Slaps the Person you mentioned', inline=True)
    embed.add_field(name='Vibe', value='Sends a video of a kid Vibing', inline=True)
    embed.add_field(name='Facts', value='Says facts', inline=True)
    embed.add_field(name='Ttt', value='Command for tictactoe', inline=True)
    embed.add_field(name='Whosbobo', value='Sends a embeded message which is ||facts||', inline=True)
    embed.set_footer(text='Remember to follow the rules!')        


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

@client.command()
async def inviteserver(ctx):
    invite = await discord.TextChannel.create_invite() #https://discordpy.readthedocs.io/en/latest/api.html#discord.TextChannel.create_invite | Make sure to replace Guild with a valid discord.Guild obj...
    await ctx.send(f"{invite}") #Sends the invite link


@slap.error
async def slap_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("mention a person for this command!!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping player (ie. <@797023993591889920>).")

def is_it_me(ctx):
    return ctx.author.id == 791248014667939850

@client.command(hidden=True)
@commands.check(is_it_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Loaded ``{extension}`` successfully")


@client.command(hidden=True)
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unloaded ``{extension}`` successfully")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')    
    
@client.command(aliases = ["bug"])
async def suggest(ctx, *, suggestion):
  lol = client.get_user(791248014667939850)

  await lol.send(f"New Suggestion by {ctx.author} \n {suggestion}")
  await ctx.send("Thank you for your suggestion / bug report! It helps a lot!")


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


def is_it_rence(ctx):
    return ctx.author.id == 736501392579231776

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def nukes(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("<:okkk:823408627079577630> Nuked This Channel.")
        await new_channel.send("https://tenor.com/view/nuke-nuclear-explosion-gif-14867944")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")


@client.command()
async def geturl(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)



@client.command(hidden=True)
@commands.check(is_it_me)
async def nuke_me(ctx):
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

@client.command()
@commands.has_permissions(manage_roles=True)
async def dm(ctx, user_id=None,*, args=None):
    if user_id != None and args != None:
        try:
            target = await ctx.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' has been sent to: '" + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")

    else:
        await ctx.channel.send("A user_id and/or arguments were not included.") 


#@client.command()
#async def poll(ctx, *, message):
    #emb = discord.Embed(title="Poll", description=f"{message}")
    #msg = await ctx.channel.send(embed=emb)
    #await msg.add_reaction('✅')
    #await msg.add_reaction('❌')

#@client.command()
#@commands.has_permissions(manage_messages=True)
#@commands.has_permissions(manage_roles=True)
#async def reactrole(ctx, emoji, role: discord.Role, *, message):
#
#    emb = discord.Embed(description=message)
 #   msg = await ctx.channel.send(embed=emb)
#    await msg.add_reaction(emoji)
#
#    with open('reactrole.json') as json_file:
#        data = json.load(json_file)
#
#        new_react_role = {'role_name': role.name, 
#        'role_id': role.id,
 #       'emoji': emoji,
 #       'message_id': msg.id}
#
 #       data.append(new_react_role)
#
#    with open('reactrole.json', 'w') as f:
#        json.dump(data, f, indent=4)


@client.command()
async def pages(ctx):
    contents = ["This is page 1!", "This is page 2!", "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break

@client.command()
async def afk(ctx):
    await ctx.message.delete()
    await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")
@client.command()
async def unafk(ctx):
    await ctx.message.delete()
    await ctx.author.edit(nick=f"{ctx.author.name}")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
     embed = discord.Embed(title="<:rooPopcorn:818433841005330433> An unknown error occured",description = f"**{lol}** {error}..", color=0x2F3136)
    await ctx.send( embed = embed )

#@client.event
#async def on_message_delete(message):
#    channel=client.get_channel("819559187263782952")
#
#    deleted = discord.Embed(
#    description=f"Message deleted in {message.channel.mention}", color=0x4040EC
#   ).set_author(name=message.author, url=Embed.Empty, icon_url=message.author.avatar_url)
#
#    deleted.add_field(name="Message", value=message.content)
#    deleted.timestamp = message.created_at
#    await channel.send(embed=deleted)




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
async def says(ctx, *striing):
    fstr = ''
    for i in striing:
        fstr = fstr + ' ' + i
    if '@' in fstr:
        await ctx.send('hi mad, I Aint pinging ppl today')
        return
    await ctx.send(fstr)


@client.command()
async def ping(ctx):
  start = time.perf_counter()
  a = await ctx.send("Pinging...")
  end = time.perf_counter()
  dur = (end-start) * 1000
  embed = discord.Embed(title = "Pong!", description = f"**Response Time** \n ```{dur:.2f}ms``` \n **Websocket Latency** \n ```{round(((client.latency) * 1000), 2)}ms```", color=0x2F3136)
  await a.edit(embed = embed)







def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]






@client.command()
async def emojifys(ctx,*,strng):
  final_str = ""
  for word in strng.lower():
    for char in word:
      if char == "a":
        final_str += ""
      if char == "b":
        final_str += "<a:Letter_B:791612085657796638>"
      if char == "c":
        final_str += "<a:Letter_C:791612094063181824>"
      if char == "d":
        final_str += "<a:Letter_D:791612106843750440>"
      if char == "e":
        final_str += " <a:Letter_E:791612112002351125>"
      if char == "f":
        final_str += " <a:Letter_F:791612116175028244>"
      if char == "g":
        final_str += "<a:Letter_G:791612128246890546>"
      if char == "h":
        final_str += " <a:Letter_H:791612133276254229>"
      if char == "i":
        final_str += "<a:Letter_I:791612137813704704>"
      if char == "j":
        final_str += "<a:Letter_J:791612149255503893>"
      if char == "k":
        final_str += "<a:Letter_K:791612153584025650>"
      if char == "l":
        final_str += "<a:Letter_L:791612158340497409>"
      if char == "m":
        final_str += "<a:Letter_M:791612170395451392>"
      if char == "n":
        final_str += "<a:Letter_N:791612174342291506>"
      if char == "o":
        final_str += "<a:Letter_O:791612178578407464>"
      if char == "p":
        final_str += "<a:Letter_P:791612191991660544>"
      if char == "q":
        final_str += "<a:Letter_Q:791612197209243678>"
      if char == "r":
        final_str += " <a:Letter_R:791612201675915275>"
      if char == "s":
        final_str += "<a:Letter_S:791612212996472833>"
      if char == "t":
        final_str += "<a:Letter_T:791612217056559105>"
      if char == "u":
        final_str += "<a:Letter_U:791612221637394453>"
      if char == "v":
        final_str += "<a:Letter_V:791612234069180417>"
      if char == "w":
        final_str += "<a:Letter_W:791612239119515688>"
      if char == "x":
        final_str += "<a:Letter_X:791612243523534849>"
      if char == "y":
        final_str += "<a:Letter_Y:791612255711789056>"
      if char == "z":
        final_str += "<a:Letter_Z:791612259876470804>"
  embed = discord.Embed(title = f"{ctx.author.name} says", description = final_str, color=0x2F3136)
  await ctx.send(embed = embed)











@client.command()
@commands.has_role("Giveaways")
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color=0x2F3136)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")

@client.command()
@commands.has_role("Giveaways")
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")    



@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("no perms!")






#@client.command()
##await ctx.channel.send(f"╭ <a:crown:812982597863997450> nice [{member.mention}] cool \n <:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658> \n <a:mark:812982596992368660> TIP: \n <:dot:812982015175557130> hahah! \n <:dot:812982015175557130> Make sure to go #〘ðﾟﾓﾝmember-rulesðﾟﾓﾝ〙! \n <:dot:812982015175557130>:  imagine \n <:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658><:line:812980251360493658> \n ╰ <a:crown:812982597863997450> lol noob ")

#@client.listen('on_message')
#async def on_message(message):


#reddit = praw.Reddit( client_id = "pzS_WFQHzxGmJA",
                      #client_secret = "TUwSOblP_o6WnaLI19p48CtbI5CZmw",
                      #username = "kymohh",
                      #password = "Angelo1699",
                      #user_agent = "pythonpraw")

#@client.command()
#async def meme(ctx):
#    subreddit = reddit.subreddit("memes")
#    all_subs = []

#    top = subreddit.top(limit = 50)

#    for submission in top:
#        all_subs.append(submission)

#    random_sub = random.choice(all_subs)

#    name = random_sub.title
#    url = random_sub.url

#    em = discord.Embed(title = name)

#    em.set_image(url = url)

#    await ctx.send(embed = em)    

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


client.run('ODAwMzY1MzcxMTIyMTIyNzYy.YAREVg.2pnbxjeju5iDsDujv64goSxrxlk')


# ╭ :WhiteCrown: GG [@maro 18s] won! ask him if legit or not. 
# :line::line::line::line::line::line::line::line::line::line::line::line::line::line::line::line: 
# :EG_aExclamationBlue: TIP: 
# :GG_bluedot: Be fast coming to giveaway channels Putting as above all other servers will help you see the pings easily! 
# :GG_bluedot: Make sure to #:white_flower:・support-us and get +3s claim time! 
# :GG_bluedot:  Boost us for extra claim time and less Cooldown 
# :line::line::line::line::line::line::line::line::line::line::line::line::line::line::line::line: 
# ╰ :WhiteCrown: Stay in Moonlight for more!
