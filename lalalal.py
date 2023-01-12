import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import urllib.request

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    
    
    
    
@client.command()
async def poll(ctx, *, message=None):

        if message == None:
                await ctx.send(f'Cannot create a poll with no message!')
                return

        questions = [
            f"Which channel should your poll be sent to?"
        ]
        answers = []

        def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
                await ctx.send(i)

                try:

                      msg = await client.wait_for('message', timeout=30.0, check=check)
                
                except asyncio.TimeoutError:
                        await ctx.send("Setup timed out, please be quicker next time!")
                        return
                else:
                        answers.append(msg.content)

        try:
                c_id = int(answers[0][2:-1])
        except:
                await ctx.send(
                    f"You didn't mention a channel properly, please format like {ctx.channel.mention} next time."
                )
                return

        channel = client.get_channel(c_id)


        embed = discord.Embed(title="Poll", description=f'{message}')
        message = await channel.send(embed=embed )

        await message.add_reaction('👍')
        await message.add_reaction('👎')    
