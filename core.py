from interactions import Client, Intents, listen
from interactions import slash_command, SlashContext
from interactions import OptionType, slash_option
from interactions import Button, ButtonStyle, ComponentContext, component_callback
from interactions import Embed
import interactions

with open('discToken.txt', 'r') as file:
    token = file.read() # token hidden using .gitignore file

with open('guildToken.txt', 'r') as file:
    guild = file.read()

with open('aiToken.txt', 'r') as file:
    ai = file.read()

bot = Client(intents=Intents.DEFAULT, token=token) # defines the bot using the token
# intents are events the bot is receiving from discord

@listen() # waits for this event to be excuted
async def on_ready(): # when the bot is ready
    print("Bot is ready!")

@bot.event
async def on_start():
    await bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name='/help', type=interactions.PresenceActivityType.WATCHING)]))

@slash_command(
    name="meow",
    description="first command woo",
) # normal command
async def meow(ctx: SlashContext):
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


# @slash_command(
#     name="base",
#     description="My command base",
#     group_name="group",
#     group_description="My command group",
#     sub_cmd_name="command",
#     sub_cmd_description="My command",
#     scopes=[guild]
# )
# async def my_command_function(ctx: SlashContext):
#     await ctx.send("Hello World") # sub function

@slash_command(
    name="ping",
    description="returns the bots ping",
    scopes=[guild]
)
async def ping(ctx: SlashContext):
    await ctx.send(f"ping: {bot.latency * 1000}") # random command

@slash_command(
    name="help",
    description="help command for the bot",
    scopes=[guild]
)
async def help(ctx: SlashContext):
    components = [
    Button(
        style=ButtonStyle.GRAY,
        label="Misc",
        custom_id="miscHelpButton",
        disabled=False
    ),
    Button(
        style=ButtonStyle.GREEN,
        label="Stocks",
        custom_id="stocksHelpButton",
        disabled=False
    ),
    Button(
        style=ButtonStyle.BLUE,
        label="AI",
        custom_id="AIHelpButton",
        disabled=False
    ),
    Button(
        style=ButtonStyle.BLURPLE,
        label="VC",
        custom_id="vcHelpButton",
        disabled=False
    )
    ]

    await ctx.send("what do you need help with homie", components=components)

# help buttons
@component_callback("miscHelpButton")
async def misc_help_button(ctx: ComponentContext):
    components= [Button(
        style=ButtonStyle.GREEN,
        label="Stocks",
        custom_id="stocksHelpButton",
        disabled=False
    ),
    Button(
        style=ButtonStyle.BLUE,
        label="AI",
        custom_id="AIHelpButton",
        disabled=False
    ),
    Button(
        style=ButtonStyle.BLURPLE,
        label="VC",
        custom_id="vcHelpButton",
        disabled=False
    )
    ]
    
    embed = Embed()

    embed.set_author(name='Miscellaneous Commands')
    embed.add_field(name='/ping', value='returns the ping of the bot', inline=False)
    embed.add_field(name='/meow',value='meow',inline=False)
    embed.add_field(name='/num (number)', value='returns a number that the bot loves', inline=False)
    embed.set_footer(text='you are hot for using this bot <3')
    await ctx.send(embeds=embed, components=components)
    

@component_callback("stocksHelpButton")
async def stocks_help_button(ctx: ComponentContext):
    components= [
        Button(
            style=ButtonStyle.GREEN,
            label="Stocks",
            custom_id="stocksHelpButton",
            disabled=False
        ),
        Button(
            style=ButtonStyle.BLUE,
            label="AI",
            custom_id="AIHelpButton",
            disabled=False
        ),
        Button(
            style=ButtonStyle.BLURPLE,
            label="VC",
            custom_id="vcHelpButton",
            disabled=False
        )
        ]

    embed = Embed()

    embed.set_author(name="Stock Commands")
    embed.add_field(name="/stock_definitions", value='provides general definitions on stock data', inline=False)
    embed.set_footer(text='get your money up 🤑')

    await ctx.send(embeds=embed, components=components)

@component_callback("vcHelpButton")
async def vc_help_button(ctx: ComponentContext):
    await ctx.send("working in progress :warning:")

@component_callback("AIHelpButton")
async def AI_help_button(ctx: ComponentContext):
    await ctx.send("working in progress :warning:")


    # embed = Embed()

    # embed.set_author(name='Stock Definitions')
    # embed.add_field(name='Open', value='the price the stock opened at', inline=False)
    # embed.add_field(name='High',value='the highest price during the day',inline=False)
    # embed.add_field(name='Low', value='the lowest price during the day', inline=False)
    # embed.add_field(name='Close', value='the closing price on the trading day', inline=False)
    # embed.add_field(name='Volume', value='how many shares were traded')
    # embed.set_footer(text='you are hot for using this bot <3')
    # await ctx.send(embeds=embed)
    

bot.load_extension("cogs.stock") # loading stock cog
bot.start() # starts bot