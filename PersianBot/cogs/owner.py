import os, sys, discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shutdown")
    async def shutdown(self, context):
        if context.message.author.id in config.OWNERS:
            embed = discord.Embed(
                description="Shutting down. Bye! :wave:",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await self.bot.logout()
            await self.bot.close()
        else:
            embed = discord.Embed(
                title="Error!",
                description="Shoma permission baraye estefade as in command ra nadarid !",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.command(name="say", aliases=["echo"])
    async def say(self, context, *, args):
        if context.message.author.id in config.OWNERS:
            await context.send(args)
        else:
            embed = discord.Embed(
                title="Error!",
                description="Shoma permission baraye estefade as in command ra nadarid !",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.command(name="embed")
    async def embed(self, context, *, args):
        if context.message.author.id in config.OWNERS:
            embed = discord.Embed(
                description=args,
                color=0x00FF00
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="Shoma permission baraye estefade as in command ra nadarid !",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.group(name="blacklist")
    async def blacklist(self, context):
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                title=f"Ta be hal {len(config.BLACKLIST)} nafar dar blacklist darim",
                description=f"{config.BLACKLIST}",
                color=0x0000FF
            )
            await context.send(embed=embed)

    @blacklist.command(name="add")
    async def blacklist_add(self, context, member: discord.Member):
        if context.message.author.id in config.OWNERS:
            userID = member.id
            try:
                config.BLACKLIST.append(userID)
                embed = discord.Embed(
                    title="User be black list ezafe shod",
                    description=f"**{member.name}** ba movafaghiyat be black list ezafe shod !",
                    color=0x00FF00
                )
                embed.set_footer(
                    text=f"Tedad {len(config.BLACKLIST)} users dar blacklist darim"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"Dar hale ezafe kardan **{member.name}** be black list khatayee rooy dad doobare talash koonid.",
                    color=0xFF0000
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="Shoma permission baraye estefade as in command ra nadarid !",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @blacklist.command(name="remove")
    async def blacklist_remove(self, context, member: discord.Member):
        if context.message.author.id in config.OWNERS:
            userID = member.id
            try:
                config.BLACKLIST.remove(userID)
                embed = discord.Embed(
                    title="User as blacklist kharej shod",
                    description=f"**{member.name}** ba movafaghiyat as black list kharej shod.",
                    color=0x00FF00
                )
                embed.set_footer(
                    text=f"Tedad {len(config.BLACKLIST)} users dar blacklist darim"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"Dar hale daravardan **{member.name}** as blacklist moshkely pish amad.",
                    color=0xFF0000
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="Shoma permission baraye estefade as in command ra nadarid !",
                color=0x00FF00
            )
            await context.send(embed=embed)





def setup(bot):
    bot.add_cog(owner(bot))