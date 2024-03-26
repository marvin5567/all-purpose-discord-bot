from interactions import Client, Intents, listen
from interactions import slash_command, SlashContext

with open('discToken.txt', 'r') as file:
    token = file.read() # token hidden using .gitignore file

with open('guildToken.txt', 'r') as file:
    guild = file.read()

bot = Client(intents=Intents.DEFAULT, token=token) # defines the bot using the token
# intents are events the bot is receiving from discord

@listen() # waits for this event to be excuted
async def on_ready(): # when the bot is ready
    print("Bot is ready!")

@listen()
async def on_message_create(event):
    # event is called when the bot sees a msg in a text channel
    print(f"message received: {event.message.content}")

@slash_command(
    name="meow",
    description="first command woo",
) # normal command
async def meow(ctx: SlashContext):
    await ctx.send("meow") # sends 'meow' in the channel the user aks the command in

bot.start() # starts bot