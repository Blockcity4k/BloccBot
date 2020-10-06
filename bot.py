import os
import random
import time

import discord
from dotenv import load_dotenv

# 1
from discord.ext import commands
from discord.ext.commands import has_permissions

load_dotenv()
TOKEN = 'NzYwNTY2NjI2Mzg2MDUxMDgz.X3N63g.rw0qA5KMUNqPFYB6uY-z5kJmX54'

# 2
bot = commands.Bot(command_prefix='!')

randomGifs1 = [
    'https://cdn.discordapp.com/attachments/760622533090344991/760934057525116948/20200923_130642.jpg',
    'https://cdn.discordapp.com/attachments/760567491050471487/760958689837842432/ezgif-6-064ba6eef7fe.gif',
    'https://cdn.discordapp.com/attachments/760567491050471487/760959039533613126/IMG_20200919_183955585.jpg',
    'https://cdn.discordapp.com/attachments/760567491050471487/760959187982221362/Screenshot_20200920-010429.png',
    'https://cdn.discordapp.com/attachments/760622533090344991/760936180472086599/fundy.jpg',
    'https://media.discordapp.net/attachments/746215515378417674/755998732495093840/tenor_4.gif',
    'https://media.discordapp.net/attachments/489624797362257920/750720050008293519/image0-13-2.gif',
    'https://cdn.discordapp.com/attachments/760622533090344991/761731000828297226/tenor.gif',
    'https://cdn.discordapp.com/attachments/760622533090344991/761731002221068290/tenor_3.gif',
    'https://cdn.discordapp.com/attachments/760622533090344991/761731002091307038/tenor_1.gif',
    'https://cdn.discordapp.com/attachments/760622533090344991/760936207222833262/118507869_119861702949908_6367706972145126506_n.jpg',
]
randomTitle1 = [
    'Every 60 seconds in Africa, a minute passes.',
    'In Sweden, it is forbidden to break the laws',
    '@dantdm I got ur book:yum:',
    "Don't fuck a fish. -Andy",
    'bitch help im in vrchat and trying to work vr',
    'BLOOD FOR THE BLOOD GOD',
    "Don't kill him, unless you want to.",
    'get gingerisoverparty trending',
    'WE DID IT REDDIT',

]
randomColor1 = [
    '#FFFFFF',
    '#C0C0C0',
    '#808080',
    '#000000',
    '#FF0000',
    '#800000',
    '#FFFF00',
    '#808000',
    '#00FF00',
    '#008000',
    '#00FFFF',
    '#008080',
    '#0000FF',
    '#000080',
    '#FF00FF',
    '#800080',
]

deathThreats = [
    'shut the fuck up',
    'go kill yourself',
    'shove yourself into a 1000 horsepower paper shredder rn',
    'go fuck yourself',
    'didnt ask',
    'fuck off',
    'I will literally beat you to the death',
    'i',
    'im going to defenestrate you',
    'I am going to castrate you and every single other part of your body too',
    'I will come full force at you from behind with a 56788 inch horse cock and split you in half literally through sexual manner',
    'i will personally come to your house and run you over with a PNEUMATIC ROLLERS CW34 OPERATING WEIGHT - STANDARD MACHINE EMPTY 22050 lb OPERATING WEIGHT - MAXIMUM BALLAST 59525 lb COMPACTION WIDTH 82 in',
    (
        'cool now please die\n'
        'I dont want to hear a word from you'
    ),
    (
        'Go kill your self\n'
        'Woops'
    ),
]

welcome = discord.utils.get(bot.get_all_channels(), name='welcome')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

#@bot.event
#async def on_member_join(member):
#    role = discord.utils.get(member.server.roles, id='760606982209142845')
#    await member.add_role(role)

@bot.command(name = 'create_channel', help = 'creates channel')
@has_permissions(administrator=True)
async def create_channel(ctx, channel_name = 'channelname'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name)
    if not existing_channel:
        await ctx.send(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        time.sleep(1)
        await ctx.channel.purge(limit=2)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
        time.sleep(1)
        await ctx.channel.purge(limit=2)


@bot.command(name = 'stupid', help = 'tells you how much you should kill yourself')
async def stupid1(ctx):
    response = random.choice(deathThreats)
    await ctx.send(response)

@bot.command(name = 'imissfundy', help = 'i miss fundy')
async def fundy1(ctx):
    response = 'https://twitch.tv/fundylive'
    await ctx.send(response)

@bot.command(name = 'rolldice', help = 'rolls dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name = 'clear', help = 'deletes messages')
@has_permissions(manage_messages=True)
async def purse(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=amount + 1)
    deleted = deleted - 1
    msg = await ctx.send(f"Deleted {len(deleted)} message (s)")
    time.sleep(2)
    await msg.delete()

@bot.command(name = 'gifs', help = 'a random picture sent by the beta testers')
async def gif(ctx):
    randomGifs = random.choice(randomGifs1)
    randomTitle = random.choice(randomTitle1)
    randomColor = random.choice(randomColor1)
    embed = discord.Embed(title=randomTitle)
    embed.set_image(url=randomGifs)
    await ctx.send(embed=embed)

@bot.command(name = 'say', help = 'make the bot say whatever you want')
async def sayy(ctx, *, amount: str):
    if amount == ("!say"):
        deathThreat = random.choice(deathThreats)
        await ctx.send(deathThreat)
    else:
        said = amount
        await ctx.channel.purge(limit=1)
        await ctx.send(said)

@bot.command(name = 'unclasico', help = 'un clasico')
async def say(ctx):
    embed = discord.Embed(title='UN CLASICO')
    embed.set_image(url='https://cdn.discordapp.com/attachments/760622533090344991/761730996441579520/tenor_2.gif')
    await ctx.send(embed=embed)

bot.run(TOKEN)