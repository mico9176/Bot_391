from discord.ext import commands

class ScheduleTracker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hasSetDate = False
        self.scheduleDate = {
            "day": 0,
            "month": "January",
            "year": 2021
        }
        self.scheduleList = []
        self.display_message = ""

    @commands.command(name="set")
    @commands.has_permissions(administrator=True)
    async def setScheduleDate(self, ctx, day: int, month, year: int):
        if (self.hasSetDate == False):
            self.scheduleDate["day"] = day
            self.scheduleDate["month"] = month
            self.scheduleDate["year"] = year

            self.hasSetDate = True

            await ctx.send(f"```Bot_391: Date of Schedule is set to {day} {month} {year}```")
        else:
            await ctx.send("```Bot_391: Date of Schedule already set. Please delete previous schedule first!```")

    @commands.command(name="add")
    @commands.has_permissions(administrator=True)
    async def addToScheduleList(self, ctx, time: int, description, link = ""):
        temp = {
            "time": time,
            "description": description,
            "link": link
        }

        self.scheduleList.append(temp)

        await ctx.send(f"```Bot_391: Added \"{description}\" with time {time}```")

    @commands.command(name="clear")
    @commands.has_permissions(administrator=True)
    async def clearSchedule(self, ctx):
        self.hasSetDate = False
        self.scheduleDate = {}
        self.scheduleList = []

        await ctx.send("```Bot_391: Schedule parameters successfully cleared```")

    @commands.command(name="view")
    async def viewSchedule(self, ctx):
        self.display_message = f"```Schedule for "

        for i in self.scheduleDate:
            self.display_message += str(self.scheduleDate[i])
            self.display_message += " "

        self.display_message += "\n\n"

        for i in self.scheduleList:
            for k in i:
                self.display_message += f"{i[k]} | "
            self.display_message += "\n"

        self.display_message += "```"

        await ctx.send(self.display_message)

def setup(bot):
    bot.add_cog(ScheduleTracker(bot))
