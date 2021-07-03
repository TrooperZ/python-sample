#!/usr/bin/python
# -*- coding: utf-8 -*-
# bot.py

import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents) #useless thing

@bot.event
async def on_ready():
    print("Bot ready.")
    
@commands.command()
async def tradeunban(ctx, user: discord.User):
    guild = bot.get_guild(770006218717921330)
    try:
        await guild.unban(user)
    except:
        return await ctx.send("Unable to unban, maybe they aren't banned?")
    await ctx.send(f"Unbanned {user.mention} from tip.cc trade server")
        
    
    
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(770006218717921330) #tipcc trade, change id
    mainguild = bot.get_guild(617034883503620167) #tipcc, change id

    if member.guild == mainguild:
        return

    logchannel = bot.get_channel(860599727309717538) #log here

    if mainguild.get_member(member.id) is not None:
        await logchannel.send(f"{member} `{member.id}` joined the server, they are in the tip.cc main server, ignoring.")
    else:
        await logchannel.send(f"{member} `{member.id}` joined the server, ***THEY ARE NOT IN THE TIP.CC MAIN SERVER***, banning due to suspicion")
        await member.send("Your account has been banned from the tip.cc trading server because our system has picked the account up as a potential scammer/botter. To resolve this issue, go to discord.gg/tipcc and discuss it with one of the Server Moderators or Server Staff.")
        await guild.ban(member, reason="Possible alt/bot/scammer detected by Tip.cc Tradekeeper")

bot.run(os.getenv('DISCORD')) #bot token, do not disclose
