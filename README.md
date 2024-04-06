All Purpose Discord Bot
--
The main purpose of this project is to test a lot of features through the medium of discord's bot capabilities in Python. The goal is to cram as many useful tools in this bot, ranging from artificial intelligence (i.e. the stock prediction feature), to ethical hacking tools (i.e. OSINT data collection tools). 

Jumps to each section:

- [General Discord Bot Functionalities](#general-discord-bot-functionalities)
- [AI Features](#ai-features)
- [Ethical Hacking Features](#ethical-hacking-features)


*Note: The discord bot is written using `interactions.py` instead of `discord.py`. No real reason as to why, I just find it easier lmao.*

this is a W.I.P. portfolio project, so if you're watching this hello! i appreciate any comments, feedback or advice on this project as it develops.

## General Discord Bot Functionalities
- to be filled

## AI Features
- [Stocks](#stocks)




### Stocks
`/stock_definitions`

simply provides definitions on the values that `/stocks` provides

`/stocks`

provides stock data on stocks the user selects; at the moment there are only 5 stocks, which are FAANG stocks. the plan is to provide up to 25 stocks in different industries as well as an option to select different time periods.

## Ethical Hacking Features
- [sherlock (username colleciton)](#sherlock)

### sherlock
**discord usage:** `/sherlock {username}`

this will get all the accounts linked to the username the user has provided

*note: this command is kinda limited at the moment since i'm still figuring out a way to provide more than 25 accounts in an embed due to discord's 25 field limit*
