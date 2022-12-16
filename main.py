import discord
from discord.ext import commands
import os



token = "MTAzNDg2MTE1OTE3OTg5ODkyMA.G9tuqN.Of0Tm6sDHA_tDjgrMn0G1FIK49N2AjRTuiTvKU"
client = commands.Bot(command_prefix="",intents=discord.Intents.all())
cringelist = {"fuck","shit","heil","cum","sex","amogus","sus","<@723575757527449661>","hitler","kill","🖕","💀","@everyone","balls","baller","stop","wtf","daddy","die","death","dead"}
@client.event
async def on_ready():
    print("cool login as {0.user}".format(client) )



@client.event 
async def on_message(message):
    ctx = await client.get_context(message)
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    skullhim = False
    for i in cringelist:
        if user_message.lower().find(i) >= 0:
            skullhim = True
    print(f'Message {user_message} by {username} on {channel}')
    if skullhim == True:
        await message.add_reaction("💀")
    if ctx.valid:
        await client.invoke(ctx)

client.run(token)