from interactions import Extension, slash_command, SlashContext
from interactions import Client, Intents, listen
from interactions import Button, ButtonStyle, ComponentContext, component_callback
from interactions import StringSelectMenu
from interactions import Embed
import interactions
import pandas
import json
import yfinance as yf

def dataParser(data):

    embed = Embed()
    embed.set_author(name="Stock Data")

    parsed = data.to_json(index=False)
    meow = json.loads(parsed)

    for key in meow['Open']:
        open_value = meow['Open'][key]
        print(f'Timestamp: {key}, Open Value: {open_value}')
        embed.add_field(name="Open: ", value=str(open_value), inline=False)

    for key in meow['High']:
        open_value = meow['High'][key]
        print(f'Timestamp: {key}, Open Value: {open_value}')
        embed.add_field(name="High: ", value=str(open_value), inline=False)
    
    for key in meow['Low']:
        open_value = meow['Low'][key]
        print(f'Timestamp: {key}, Open Value: {open_value}')
        embed.add_field(name="Low: ", value=str(open_value), inline=False)

    for key in meow['Close']:
        open_value = meow['Close'][key]
        print(f'Timestamp: {key}, Open Value: {open_value}')
        embed.add_field(name="Close: ", value=str(open_value), inline=False)
    
    for key in meow['Volume']:
        open_value = meow['Volume'][key]
        print(f'Timestamp: {key}, Open Value: {open_value}')
        embed.add_field(name="Volume: ", value=str(open_value), inline=False)

    return embed

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
        embed = Embed()

        embed.set_author(name='Stock Definitions')
        embed.add_field(name='Open', value='the price the stock opened at', inline=False)
        embed.add_field(name='High',value='the highest price during the day',inline=False)
        embed.add_field(name='Low', value='the lowest price during the day', inline=False)
        embed.add_field(name='Close', value='the closing price on the trading day', inline=False)
        embed.add_field(name='Volume', value='how many shares were traded')
        embed.set_footer(text='you are hot for using this bot <3')
        
        await ctx.send(embeds=embed)
    
    @slash_command(
        name="stocks",
        description="shows you stock data",
        scopes=[guild]
    )
    async def stocks(self, ctx: SlashContext):
        FAANG = [
        Button(
            style=ButtonStyle.BLUE,
            label="Facebook (Meta)",
            custom_id="metaStockButton",
            disabled=False
        ),
        Button(
            style=ButtonStyle.GREEN,
            label="Amazon",
            custom_id="amazonStockButton",
            disabled=False
        ),
        Button(
            style=ButtonStyle.GREY,
            label="Apple",
            custom_id="appleStockButton",
            disabled=False
        ),
        Button(
            style=ButtonStyle.RED,
            label="Netflix",
            custom_id="netflixStockButton",
            disabled=False
        ),
        Button(
            style=ButtonStyle.GREEN,
            label="Google (Alphabet)",
            custom_id="googleStockButton",
            disabled=False
        )
        ]

        await ctx.send("Select stock data:", components=FAANG)
        # Microsoft, Tesla, 
        # Cryptocurrencies
        
    # FAANG companies
    @component_callback("appleStockButton")
    async def apple(self, ctx: ComponentContext):
        # get stock data
        stock = yf.Ticker("AAPL")
    
        # get market data
        data = stock.history(period='1d')
        await ctx.send(embed=dataParser(data))

    @component_callback("metaStockButton")
    async def meta(self, ctx: ComponentContext):
        # get stock data
        stock = yf.Ticker("META")
        # get market data
        data = stock.history(period="1d")  
        # 5 days period, can be '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        await ctx.send(embed=dataParser(data))

    @component_callback("netflixStockButton")
    async def netflix(self, ctx: ComponentContext):
        # get stock data
        stock = yf.Ticker("NFLX")
        # get market data
        data = stock.history(period="1d")  
        # 5 days period, can be '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        await ctx.send(embed=dataParser(data))
    
    @component_callback("amazonStockButton")
    async def amazon(self, ctx: ComponentContext):
        # get stock data
        stock = yf.Ticker("AMZN")
        # get market data
        data = stock.history(period="1d")  
        # 5 days period, can be '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        await ctx.send(embed=dataParser(data))
    
    @component_callback("googleStockButton")
    async def google(self, ctx: ComponentContext):
        # get stock data
        stock = yf.Ticker("GOOG")
        # get market data
        data = stock.history(period="1d")  
        # 5 days period, can be '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        await ctx.send(embed=dataParser(data))
    