#!/usr/bin/python
# -*- coding: utf-8 -*-
# bot.py

import discord
import os
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents) #useless thing

@bot.event
async def on_ready():
    print("Bot ready.")

@bot.event
async def on_member_join(member):
    print(member.id)
    guild = bot.get_guild(860599727309717534) #tipcc trade, change id
    mainguild = bot.get_guild(860599706434666506) #tipcc, change id

    if mainguild.get_member(member.id) is not None:
        print('This person is in tipcc')
    else:
        await guild.ban(member)
        print('Not in tipcc, banning')

bot.run(os.getenv('DISCORD')) #bot token, do not disclose
