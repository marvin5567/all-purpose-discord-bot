from interactions import Extension, slash_command, SlashContext
from interactions import Client, Intents, listen
from interactions import OptionType, slash_option
from interactions.api.voice.audio import AudioVolume
import wavelink

class vc(Extension):
    with open('guildToken.txt', 'r') as file:
        guild = file.read()

    def __init__(self, bot):
        self.bot = bot

    @listen()
    async def on_ready(self):
        print("stock cog ready")

    @listen()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @listen()
    async def on_wavelink_track_end(self, player: wavelink.Player, track: wavelink.YouTubeTrack, reason):
        ctx = player.ctx
        vc: player = ctx.voice_state

        if vc.loop:
            return await vc.play(track)

        next_song = vc.queue.get()
        await vc.play(next_song)
        await ctx.send(f'Now playing: {next_song.title}')

    @slash_command(
        name="play",
        description="plays the users desired song",
        scopes=[guild]
    )
    @slash_option("search", 
                  "The song to play", 
                  3, 
                  True)
    async def play(self, ctx: SlashContext, *, search: str):
        if not ctx.voice_state:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_state

        tracks = await wavelink.YouTubeTrack.search(search)
        if vc.queue.is_empty and vc.is_playing:
            await vc.play(tracks)
            await ctx.send(f'Now playing: {tracks.title}')
        else:
            await vc.queue.put_wait(tracks)
            await ctx.send(f'Added {tracks.title} to the queue!')
        vc.ctx = ctx
        setattr(vc, "loop", False)

    @slash_command(
        name="pause",
        description="pauses the song that is currently playing",
        scopes=[guild]
    )
    async def pause(self, ctx: SlashContext):
        if ctx.voice_state is None:
            return await ctx.send("Not connected to a voice channel.")
        else:
            await ctx.voice_state.pause()
            await ctx.send(f'Paused :pause_button:')

    @slash_command(
        name="resume",
        description="resumes the song that is currently playing",
        scopes=[guild]
    )
    async def resume(self, ctx: SlashContext):
        if ctx.voice_state is None:
            return await ctx.send("Not connected to a voice channel.")
        else:
            vc: wavelink.Player = ctx.voice_state

        await vc.resume()
        await ctx.send("Resumed")
    
    @slash_command(
        name="stop",
        description="stops the song that is currently playing",
        scopes=[guild]
    )
    async def stop(self, ctx: SlashContext):
        """Stops and disconnects the bot from voice"""
        if ctx.voice_state is None:
            return await ctx.send("Not connected to a voice channel.")
        else:
            await ctx.voice_state.stop()
            await ctx.send(f'Stopped :stop_sign:')