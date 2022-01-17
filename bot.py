# bot.py
import os
import discord
import random
import time
import string
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

TOKEN=os.getenv('DISCORD_TOKEN')

TEST=True
#
if TEST:
    alert_channels=[930167379080663071]
else:
    alert_channels=[905998288568868885, 924488314801750016]
#bot test
#Trigger, other server

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready to be used')
   # after it is ready do it
    for guild in bot.guilds:
        print(guild)
        print(guild.id)


@bot.command(name='sbuy')
@commands.has_role('Trigger')
async def buy_order(ctx, coin, entry, stoploss, tp1, tp2, tp3, comments=None, image=None):
    desc="<:coin:932390127257415700> **Coin:** "+coin+"\n"
    desc+="<:door:932084054877155388> **Entry:** "+entry+"\n"
    desc+="\n\n<:chart_with_downwards_trend:932081529079857273> **SL:** "+str(stoploss)
    desc+="\n"+"<:chart_with_upwards_trend:932080615170400317> **TP1: **"+str(tp1)+"\n"+"<:chart_with_upwards_trend:932080615170400317> **TP2: **"
    desc+=str(tp2)+"\n"+"<:chart_with_upwards_trend:932080615170400317> **TP3: **"+str(tp3)+"\n"
    if(comments != None):
        desc=desc+"\n<:notepad_spiral:932085365538422844> **Comments**: "+comments
    embed=discord.Embed(title="New Spot position", description=desc, color=0x00FF00)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Trigger Alerts | "+today_date, icon_url="https://i.imgur.com/SlVtvWL.jpg")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                await channel.send(ctx.message.guild.default_role, embed=embed)
   
@bot.command(name='fbuy')
@commands.has_role('Trigger')
async def buy_order(ctx, coin, leverage, entry, stoploss, tp1, tp2, tp3, comments=None, image=None):
    desc="<:coin:932390127257415700> **Coin:** "+coin+"\n"
    desc+="<:door:932084054877155388> **Entry:** "+entry+"\n"+"<:warning:932400617794719795> **Leverage: **"+leverage
    desc+="\n\n<:chart_with_downwards_trend:932081529079857273> **SL:** "+str(stoploss)
    desc+="\n"+"<:chart_with_upwards_trend:932080615170400317> **TP1: **"+str(tp1)+"\n"+"<:chart_with_upwards_trend:932080615170400317> **TP2: **"
    desc+=str(tp2)+"\n"+"<:chart_with_upwards_trend:932080615170400317> **TP3: **"+str(tp3)+"\n"
    if(comments != None):
        desc=desc+"\n<:notepad_spiral:932085365538422844> **Comments**: "+comments
    embed=discord.Embed(title="New Futures position", description=desc, color=0x00FF00)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Trigger Alerts | "+today_date, icon_url="https://i.imgur.com/SlVtvWL.jpg")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                await channel.send(ctx.message.guild.default_role, embed=embed)

@bot.command(name='strim')
@commands.has_role('Trigger')
async def sell_order(ctx, coin, tp, perc, sl, image=None):
    desc="<:coin:932390127257415700> **Coin:** "+coin+"\n"
    desc+="<:white_check_mark:932093519055712298> TP"+tp+" hit, sell "+perc+"%"+", set SL to "+sl+"\n"
    embed=discord.Embed(title="Trim Spot position", description=desc, color=0xFF5733)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Trigger alerts | "+today_date, icon_url="https://i.imgur.com/SlVtvWL.jpg")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                await channel.send(ctx.message.guild.default_role, embed=embed)

@bot.command(name='ftrim')
@commands.has_role('Trigger')
async def sell_order(ctx, coin, tp, perc, sl, image=None):
    desc="<:coin:932390127257415700> **Coin:** "+coin+"\n"
    desc+="<:white_check_mark:932093519055712298> TP"+tp+" hit, sell "+perc+"%"+", set SL to "+sl+"\n"
    embed=discord.Embed(title="Trim Futures position", description=desc, color=0xFF5733)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Trigger alerts | "+today_date, icon_url="https://i.imgur.com/SlVtvWL.jpg")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                await channel.send(ctx.message.guild.default_role, embed=embed)

@bot.command(name='msg')
@commands.has_role('Trigger')
async def message(ctx, txt, image=None):
    embed=discord.Embed(description=txt, color=0xFFFFFF)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Trigger Alerts | "+today_date, icon_url="https://i.imgur.com/SlVtvWL.jpg")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                await channel.send(ctx.message.guild.default_role, embed=embed)

bot.run(TOKEN)
