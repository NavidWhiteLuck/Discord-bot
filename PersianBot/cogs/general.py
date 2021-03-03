import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
from multiprocessing import context
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", aliases=["botinfo"])
    async def info(self, context):
        embed = discord.Embed(
            description="Created by Persian | EsfahanArmy",
            color=0xFF3371
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Owner:",
            value="Persian#5273",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"{config.BOT_PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, context):
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = discord.Embed(
            title="**Server Name:**",
            description=f"{server}",
            color=0x33C4FF
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Owner",
            value=f"{server.owner}\n{server.owner.id}"
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Member Count",
            value=server.member_count
        )
        embed.add_field(
            name="Text/Voice Channels",
            value=f"{channels}"
        )
        embed.add_field(
            name=f"Roles ({role_length})",
            value=roles
        )
        embed.set_footer(
            text=f"Created at: {time}"
        )
        await context.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Pong!",
            value=":ping_pong:",
            inline=True
        )
        embed.set_footer(
            text=f"Pong request by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="invite")
    async def invite(self, context):
        await context.send("! بهت یک پی ام دادم برو ببین !")
        await context.author.send(f"برای اضافه کردن من به سرورت روی لینک کلیک کن: https://discord.com/oauth2/authorize?client_id={APPLICATION_ID}&permissions=8&scope=bot")

    @commands.command(name="server")
    async def server(self, context):
        await context.send("! بهت یک پی ام دادم برو ببین !")
        await context.author.send("به سرور ما بپیوندید: https://discord.gg/n4YPW6jeS7")

    @commands.command(name="poll")
    async def poll(self, context, *args):
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="!یک نظر سنجی جدید ایجاد شد!",
            description=f"{poll_title}",
            color=0x00FF00
        )
        embed.set_footer(
            text=f"Poll created by: {context.message.author} • React to vote!"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    @commands.command(name="8ball")
    async def eight_ball(self, context, *args):
        answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
                   'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
                   'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
                   'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
                   'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{answers[random.randint(0, len(answers))]}",
            color=0x00FF00
        )
        embed.set_footer(
            text=f"Question asked by: {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="bitcoin")
    async def bitcoin(self, context):
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Info",
                description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                color=0x00FF00
            )
            await context.send(embed=embed)


    @commands.command(name="notifi")
    async def notifi(self, context, *args):
        notifi_title = " ".join(args)
        embed = discord.Embed(
            title="!اطلاعیه جدید ایجاد شد در صورت تایید ارسال فرمایید!",
            description=f"{notifi_title}",
            color=0x00FF00
        )
        embed.set_footer(
            text=f"Notification created by: {context.message.author} • vote to send!"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("✔")
        await embed_message.add_reaction("❌")


        embed.add_field(
            name="Pong!",
            value=":ping_pong:",
            inline=True
        )




    @commands.command(name="avatar")
    async def avatar(self, ctx,member: discord.Member = None ):

        if member is None:
            embed = discord.Embed(title="از این دستور اینطور استفاده کن: ```+avatar [member]```", colour=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            embed2 = discord.Embed(title=f"آواتار {member} !", colour=0x0000ff)
            embed2.add_field(name="آواتار متحرک ؟", value=member.is_avatar_animated())
            embed2.set_image(url=member.avatar_url)
            embed2.set_footer(text=f"Avatar requested by: {ctx.message.author} !")
            await ctx.send(embed=embed2)







        




def setup(bot):
    bot.add_cog(general(bot))