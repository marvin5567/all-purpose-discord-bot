from interactions import Extension, slash_command, SlashContext
from interactions import Client, Intents, listen
from interactions import Button, ButtonStyle, ComponentContext, component_callback
from interactions import StringSelectMenu
from interactions import Embed
from interactions import OptionType, slash_option
import interactions
import sherlock
import subprocess
import os

class ethicalHacking(Extension):
    with open('guildToken.txt', 'r') as file:
        guild = file.read()

    @slash_command(
        name="sherlock",
        description="returns the usernames of the desired user",
        scopes=[guild]
    )
    @slash_option(
    name="username",
    description="the username the user is sending",
    required=True,
    opt_type=OptionType.STRING
    )  
    async def find_username(self, ctx: SlashContext, username):
        
        embed = Embed()

        msg = await ctx.send('⌛ please wait while i look for this username')
        
        # get the current working directory
        current_directory = os.getcwd()

        # changing to the dir sherlock is in
        os.chdir("..")
        os.chdir("..") # i have to back out twice since the folder the project is in is inside a folder
        os.chdir('C:/Users/Owner/Desktop/sherlock')

        subprocess.run(['powershell', 'python sherlock ' + username], shell=False) # running python sherlock command

        # access sherlock text file containing accounts
        file1 = open(username+'.txt', 'r')
        Lines = file1.readlines()

        for count, line in enumerate(Lines): # loop through text files
            if count == len(Lines): # this is to void the last line in the text file
                break
            else:
                embed.add_field(name=str(count + 1), value=line.strip(), inline=False)
            

        embed.set_author(name=f"{username}'s accounts")

        await msg.edit(embeds=embed)
        await ctx.send(ctx.author.mention + " done!")

        os.chdir(current_directory) # cleaning up process by going back to root directory

        # embed still needs to be cleaned up
        # cut last line since it only reports how many sites have been detected




