from interactions import Client, Intents, listen
from interactions import slash_command, SlashContext
from interactions import OptionType, slash_option

with open('discToken.txt', 'r') as file:
    token = file.read() # token hidden using .gitignore file

with open('guildToken.txt', 'r') as file:
    guild = file.read()

bot = Client(intents=Intents.DEFAULT, token=token) # defines the bot using the token
# intents are events the bot is receiving from discord

@listen() # waits for this event to be excuted
async def on_ready(): # when the bot is ready
    print("Bot is ready!")

@slash_command(
    name="meow",
    description="first command woo",
) # normal command
async def meow(ctx: SlashContext):
    await ctx.send("meow") # sends 'meow' in the channel the user aks the command in

@slash_command(
    name="meo",
    description="first command woo",
    scopes=[guild]
) # normal command
async def meo(ctx: SlashContext):
    await ctx.send("meow") # sends 'meow' in the channel the user aks the command in


@slash_command(
    name="num",
    description="i like this number",
    scopes=[guild]
)
@slash_option(
    name="integer_option",
    description="Integer Option",
    required=True,
    opt_type=OptionType.INTEGER
)
async def num(ctx: SlashContext, integer_option: int):
    await ctx.send(f"wow i like the number: {integer_option}") # command testing out command options

@slash_command(
    name="base",
    description="My command base",
    group_name="group",
    group_description="My command group",
    sub_cmd_name="command",
    sub_cmd_description="My command",
    scopes=[guild]
)
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World") # sub function

@slash_command(
    name="ping",
    description="returns the bots ping",
    scopes=[guild]
)
async def ping(ctx: SlashContext):
    await ctx.send(bot.latency * 1000) # random command

bot.load_extension("cogs.stock") # loading stock cog
bot.start() # starts bot