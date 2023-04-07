# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

def open_file(filename_var):
    filename =  open(filename_var, mode = 'r')
    return filename 


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{client.user.name} has connected to Discord!')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
            
           
        ),
        'CHARLES COME ON MAN',
         'nikolaschh NIKOLASCHHHHH',

    ]

    happy_birthday_quotes = [
        'Happy Birthday GrandMaster',
        'Happy Happy Birthday too you',
    ]


    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == 'happy birthday':
        response = random.choice(happy_birthday_quotes)
        await message.channel.send(response)
    

client.run(TOKEN)