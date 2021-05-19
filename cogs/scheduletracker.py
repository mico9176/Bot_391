from discord.ext import commands

class ScheduleTracker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hasSetDate = False
        self.scheduleDate = {}
        self.scheduleList = []

    @commands.command(name="set")
    @commands.has_permissions(administrator=True)
    async def setScheduleDate(self, ctx, day: int, month, year: int):
        if (self.hasSetDate == False):
            self.scheduleDate["day"] = day
            self.scheduleDate["month"] = month
            self.scheduleDate["year"] = year

            self.hasSetDate = True

            await ctx.send("```Bot_391: Date of Schedule is set to {} {} {}```".format(day, month, year))
        else:
            await ctx.send("```Bot_391: Date of Schedule already set. Please delete previous schedule first!```")

    @commands.command(name="clear")
    @commands.has_permissions(administrator=True)
    async def clearSchedule(self, ctx):
        self.hasSetDate = False
        self.scheduleDate = {}
        self.scheduleList = []

        await ctx.send("```Bot_391: Schedule parameters successfully cleared```")

def setup(bot):
    bot.add_cog(ScheduleTracker(bot))
