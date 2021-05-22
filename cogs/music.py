import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def joinChannel(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            await channel.connect()

        await ctx.send(f"```Bot_391: Successfully connected to {channel}```")


    @commands.command(name="leave")
    async def leaveChannel(self, ctx):
        for x in self.bot.voice_clients:
            if (x.guild == ctx.message.guild):
                await x.disconnect()
                await ctx.send(f"```Bot_391: Successfully disconnected```")
                return

        await ctx.send("```Bot_391: Bruh I'm not even part of a voice channel yet ;-;```")


def setup(bot):
    bot.add_cog(Music(bot))
