import discord
from discord.ext import commands
import webserver
from webserver import keep_alive

bot = commands.Bot(
    command_prefix='',
    activity=discord.Activity(
        application_id=874469380765913109,
        name='EO Community',
        type=discord.ActivityType.watching,
        state='In Group',
        details='Early OG Community',
        assets={'large_image':'874485178242854993'}),
    self_bot=True)

keep_alive()
bot.run("Token Discord", bot=False)
