import discord, asyncio, os, sys, discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class whois(commands.Cog, name="whois"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="whois")
    async def whois(self, ctx, member:discord.Member =  None):

        if member is None:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

        embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name="درباره یوزر: ")
        embed.add_field(name="آی دی فرد:", value=member.id, inline=False)
        embed.add_field(name="یوزر نیم:",value=member.display_name, inline=False)
        embed.add_field(name="کد یوزر نیم:",value=member.discriminator, inline=False)
        embed.add_field(name="وضعیت فعلی:", value=str(member.status).title(), inline=False)
        embed.add_field(name="آخرین بازدید:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
        embed.add_field(name="تاریخ ساخت اکانت:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
        embed.add_field(name="تاریخ جوین به سرور:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
        embed.add_field(name=f"رول های فرد [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="بالا ترین رول فرد:", value=member.top_role, inline=False)
        embed.add_field(name="ربات:", value=member.bot, inline=False)
        await ctx.send(embed=embed)
        return



def setup(bot):
    bot.add_cog(whois(bot))