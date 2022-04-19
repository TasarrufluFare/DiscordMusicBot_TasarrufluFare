import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
'''
   Genel Komutlar
   -tf help - Bütün mevcut komutları gösterir.
   -tf p <anahtarkelime> - Şarkıyı yutuptan bulur ve çalar.
   -tf q - Müzik listesini gösterir.
   -tf skip - Şarkıyı atlar.
   -tf clear - Sırayı temizler.
   -tf leave - Botun bağlantısını keser.
   -tf pause - Çalan şarkıyı duraklatır.
   -tf resume - Duraklatılmış şarkıyı devam ettirir.       
'''
"""
        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_read(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name="help", help="Bütün mevcut komutları gösterir.")
    async def help(self, ctx):
        await ctx.send(self.help_message)
