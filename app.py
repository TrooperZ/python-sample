#!/usr/bin/python
# -*- coding: utf-8 -*-
# bot.py

import discord
import os
import asyncio
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents) #useless thing

@bot.event
async def on_ready():
    print("Bot ready.")
    
@bot.command(name='tradeunban')
async def tradeunban(ctx, user: discord.User):
    if not ctx.author.guild_permissions.ban_members:
        msg = await ctx.send("Restricted access.")
        await asyncio.sleep(10)
        await msg.delete()
        return
    
    guild = bot.get_guild(770006218717921330) #tipcc trade, change id
    try:
        await guild.unban(user)
    except Exception as e:
        print(e)
        return await ctx.send("Unable to unban, maybe they aren't banned? (If they are banned, check bot logs)")
    await ctx.send(f"Unbanned {user.mention} from tip.cc trade server")
    log = bot.get_channel(860599727309717538) #set this to log channel id
    await log.send(f"{ctx.author} unbanned {user} from tip.cc trade server")
        
    
    
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(770006218717921330) #tipcc trade, change id
    mainguild = bot.get_guild(617034883503620167) #tipcc, change id

    if member.guild == mainguild:
        return

    logchannel = bot.get_channel(860599727309717538) #log channel here

    if mainguild.get_member(member.id) is not None:
        await logchannel.send(f"{member} `{member.id}` joined the server, they are in the tip.cc main server, ignoring.")
    else:
        await logchannel.send(f"{member} `{member.id}` joined the server, ***THEY ARE NOT IN THE TIP.CC MAIN SERVER***, banning due to suspicion")
        try:
            await member.send("""You have been temporarily removed from the tip.cc trading server.

The trading server is exclusive for Tip.cc server users because you are not a user of the mentioned server, we temporarily removed you from the tip.cc trading server.

Once you have joined over at discord.gg/tipcc * please appeal your ban at https://discord.gg/afwSbGcEmN
*You might be subject to further verification to be able to join tip.cc main server""")
        except:
            await logchannel.send("User has dms off, couldn't dm.")
        await guild.ban(member, reason="Possible alt/bot/scammer detected by Tip.cc Tradekeeper")

bot.run(os.getenv('DISCORD')) #bot token, do not disclose
