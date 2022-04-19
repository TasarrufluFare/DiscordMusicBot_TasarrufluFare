import discord
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix="-tf ")

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Farelerle"))


#bot.run(os.getenv("TOKEN"))

bot.run("Token here")
