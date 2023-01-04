import os
import keep_alive
import asyncio
import json
import os
import random
import time
import colorama
import discord
import numpy
import requests
from colorama import Fore
from discord.ext import commands
from discord.utils import get

with open('config.json') as f:
    config = json.load(f)
    
token = os.environ.get('token')
    
bot = commands.Bot('.', description='zzz', self_bot=True)


def Clear():
    os.system('cls')


Clear()

def Init():
    try:
        bot.run(token, bot=False, reconnect=True)
        os.system(f'title (Activity Statuses)')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"
              + Fore.RESET)
        os.system('pause >NUL')





async def ready():
  await bot.wait_until_ready()
  print("Streaming.")

  statuses = ["murda.lol", "dying", "murder", "@hillmurder", "@shecutsmurder"]


  while not bot.is_closed():
  
       status = random.choice(statuses)

       await bot.change_presence(status= discord.Status.do_not_disturb, activity = discord.Streaming(name = status, url = "https://twitch.tv/murder"))

       await asyncio.sleep(3)


bot.loop.create_task(ready())


keep_alive.keep_alive()

if __name__ == '__main__':
    Init()
