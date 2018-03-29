import discord
import random
import linecache
import re
import asyncio
import shelve
from discord.ext import commands
import time 

prefix = '&'

des = 'Alt Gen. Is A Alt Bot!'
client = commands.Bot(description=des, command_prefix=prefix,pm_help = True)


@client.event
async def on_ready():
    print("[]I'm in")
    print('[] Name: {}'.format(client.user.name))
    
@client.event
async def on_message(message):
    if message.content == "hello":
        await client.send_message(message.channel, ':wave: ')
    elif message.content == "how i can get alts?":
        await client.send_message(message.channel, "Try to use  !altmc command :) ")
    elif message.content == "can i ask something?":
        await client.send_message(message.channel, "Sure, You can ask here if you want or try DM @KFE iAnimeZ#7970 :ok_hand: ")
    elif message.content == "Bot, how are you?":
        await client.send_message(message.channel, "I am good thanks for asking ! HF :raised_hand: ")
    elif message.content == "who want play mineact?":
        await client.send_message(message.channel, "Me,DM @KFE iAnimeZ#7970 :) ")
    
@client.command(pass_context=True)
async def Owner(ctx):
    """Shows the Owner Who Made The Bot!"""
    await client.say('Owner of the bot is <@303286549695561729>')

@client.command(pass_context=True)
async def Invite(ctx):
    """Type &Invite Gives you link inv the bot to Your server!"""
    await client.say('https://discordapp.com/oauth2/authorize?client_id=427887322374340608&permissions=0&scope=bot')

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    """Type &Kick @mention"""
    await client.kick(userName)
    await client.say("__**Successfully User Has Been Kicked!**__")

@client.command(pass_context = True)
async def Ban(ctx, userName: discord.User):
    """Type &Ban @mention"""
    await client.ban(userName)
    await client.say("__**Successfully User Has Been Banned!**__")
@client.command(pass_context=True)
async def Say(ctx, member : discord.Member = None, *, message):
    """Type &Say @mention Hello"""
    await client.send_message(member, message)

@client.command(pass_context=True)
async def purge(context, number : int):
	"""Clear a specified number of messages in the chat"""
	deleted = await client.purge_from(context.message.channel, limit=number)
	await client.send_message(context.message.channel, 'Deleted {} message(s)'.format(len(deleted)))

@client.command(pass_context=True)
async def Alts(ctx):
    """Type &Alts To see how you can get some alts!"""
    await client.say('Go to Check Channels For MC/Spotify Alts! ')


    

    
client.run('NDI3ODg3MzIyMzc0MzQwNjA4.DZrE9Q.9lrstk7Y1-QQh3L6ZpKaTQJDUqM')
