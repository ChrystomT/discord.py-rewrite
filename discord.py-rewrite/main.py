import keep_alive
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '.') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
 
@client.command() 
@has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}')

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

@client.command()
@has_permissions(manage_messages = True)
async def purge(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
  
@client.command()
@has_permissions(ban_members = True)
async def unban(ctx, *, member):
  banned_users * await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  
  
  for ban_entry in banned_users:
      user = ban_entry.user
      
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}' )
        return


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))

#this runs on repl.it hence the need for a .env file which I have gotten rid of (since .env files are complicated on GitHub) to keep my bot's token from getting leaked
#fork from dartzii, https://repl.it/@templates/Discord-Bot-Python-Starter