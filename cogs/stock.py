from interactions import Extension, slash_command, SlashContext
from interactions import Client, Intents, listen
from interactions import Button, ButtonStyle
import interactions
import pandas as ps
import yfinance as yf

class stock(Extension):

    with open('guildToken.txt', 'r') as file:
        guild = file.read()

    @listen()
    async def on_ready():
        print("stock cog ready")

    @slash_command(
            name="stock_definitions",
            description="shows basic stock defenitions",
            scopes=[guild]
    )
    async def stock_definitions(self, ctx: SlashContext):
        """
        embed = interactions.Embed(
            color=interactions.Color.gold()
        )

        embed.set_author(name='Stock Definitions')
        embed.add_field(name='Open', value='the price the stock opened at', inline=False)
        embed.add_field(name='High',value='the highest price during the day',inline=False)
        embed.add_field(name='Low', value='the lowest price during the day', inline=False)
        embed.add_field(name='Close', value='the closing price on the trading day', inline=False)
        embed.add_field(name='Volume', value='how many shares were traded')
        embed.set_footer(text='you are hot for using this bot <3')
        """
        
        await ctx.send("""
-Open - the price the stock opened at

-High - the highest price during the day

-Low - the lowest price during the day

-Close - the closing price on the trading day

-Volume - how many shares were traded""")
    
    @slash_command(
        name="apple_stock",
        description="shows you apple's stock",
        scopes=[guild]
    )
    async def apple_stock(self, ctx: SlashContext):
        # get stock data
        stock = yf.Ticker("AAPL")
        # get market data
        data = stock.history(period="5d")  
        # 5 days period, can be '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        await ctx.send(data.to_string(index=False))
