from discord import Intents
from discord.ext import commands
from tuning_forks.config import *
from tuning_forks.audio_source import PCMStream

intents = Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command(name="join", help="Tells the bot to join the voice channel")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send(
            "{} is not connected to a voice channel".format(ctx.message.author.name)
        )
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name="play", help="To play song")
async def play(ctx, num=None):
    try:
        voice_client = ctx.message.guild.voice_client
    except:
        await ctx.send("The bot is not connected to a voice channel.")
    async with ctx.typing():
        stream = PCMStream()
        if num:
            stream.change_device(int(num))
        voice_client.play(stream)
    await ctx.send("**Now playing**")


@bot.command(name="pause", help="This command pauses the song")
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name="leave", help="To make the bot leave the voice channel")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.event
async def on_message(message):
    # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
    await bot.process_commands(message)
    if str(message.content).lower() == "hello":
        await message.channel.send("Hi!")

    if str(message.content).lower() in ["swear_word1", "swear_word2"]:
        await message.channel.purge(limit=1)
