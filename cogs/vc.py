from interactions import Extension, slash_command, SlashContext
from interactions import Client, Intents, listen
from interactions import OptionType, slash_option
from interactions.api.voice.audio import AudioVolume
import interactions
import asyncio
import wavelink

class vc(Extension):
    with open('guildToken.txt', 'r') as file:
        guild = file.read()

    def __init__(self, bot):
        self.bot = bot

    @listen()
    async def on_ready(self):
        print("stock cog ready")

    @slash_command(
        name="record",
        description="records audio",
        scopes=[guild]
    )
    async def record(self, ctx: SlashContext):
        voice_state = await ctx.author.voice.channel.connect()

        # Start recording
        await voice_state.start_recording()
        await asyncio.sleep(10)
        await voice_state.stop_recording()
        await ctx.send(files=[interactions.File(file, file_name="user_id.mp3") for user_id, file in voice_state.recorder.output.items()])