from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

wolf = "🐺"
    
print(wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf+wolf)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "love":
        a = await message.channel.send("love")
        await a.add_reaction(wolf)
        print("a")
        check = lambda r, u: True 
        await bot.wait_for('reaction_add', check=check, timeout=60)
        print("a")
        await message.channel.send("ffck")
        print("a")
        
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
