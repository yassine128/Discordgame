import random
import discord
from discord.ext import commands
import sys
import math

client = discord.Client()
@client.event #event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    decision = random.randint(1,4)
    #################-- Human Rock --#############
    if "!grps rock" in message.content.lower() and decision == 1:
        await message.channel.send("it's a tie")
    if "!grps rock" in message.content.lower() and decision == 2:
        await message.channel.send("Bot win (bot=paper, Human=rock)")
    if "!grps rock" in message.content.lower() and decision == 3:
        await message.channel.send("it's a tie")
    #################-- Human paper --############# 
    if "!grps paper" in message.content.lower() and decision == 2:
        await message.channel.send("it's a tie")
    if "!grps paper" in message.content.lower() and decision == 1:
        await message.channel.send("Human win (bot=rock, Human=paper)")
    if "!grps paper" in message.content.lower() and decision == 3:
        await message.channel.send("Bot win (bot=scissors, Human=paper)")
    #################-- Human scissors --#############
    if "!grps scissors" in message.content.lower() and decision == 3:
        await message.channel.send("it's a tie")
    if "!grps scissors" in message.content.lower() and decision == 2:
        await message.channel.send("Human win (bot=paper, Human=scissors)")
    if "!grps scissors" in message.content.lower() and decision == 1:
        await message.channel.send("Bot win (bot=rock, Human=scissors)")
    
    if "!gminesweeper" in message.content.lower():
        x = 9
        y = 9 
        chance = 0.3
        #helper to populate filled arrays
        def create2D(rowCount, colCount, value=None):
            a = [None] * rowCount
            for row in range(rowCount):
                a[row] = [value] * colCount
            return a
        #helper for numeric notes
        def emote(i):
            switcher={
                0:":zero:",
                1:":one:",
                2:":two:",
                3:":three:",
                4:":four:",
                5:":five:",
                6:":six:",
                7:":seven:",
                8:":eight:",
                9:":nine:"
            }
            return switcher.get(i,"")
        #build the arrays
        mines = create2D(x+2,y+2,False)
        solution = create2D(x+2,y+2,0)
        #seed the mines
        for m in range (1,x+1):
            for n in range (1,y+1):
                mines[m][n] = (random.random() < chance)
        #calculate adjacent mines
        for m in range (1,x+1):
            for n in range (1,y+1):
                for mm in range (m-1,m+2):
                    for nn in range (n-1,n+2):
                        if mines[mm][nn]:
                            solution[m][n] += 1
        #build our string
        output = ""
        for m in range(1, x+1):
            for n in range(1, y+1):
                if mines[m][n]:
                    output += "||:bomb:||"
                else:
                    output += "||" + emote(solution[m][n]) + "||"
            output += "\n"  
        #print it
        await message.channel.send(output)
    if "!gcreator" in message.content.lower():
        await message.channel.send("My amazing creator is Yassine Seddaoui Aka Cursedbuddy ||:sunglasses:||")
client.run("NjY3ODc4OTMzMTg1ODIyNzIx.XiJJBg.1_CUaekoQBhqW3eRB0UQ4oRBWhc")
#1 = rock
#2 = paper 
#3 = scissors

#Id: 667878933185822721
#Token: NjY3ODc4OTMzMTg1ODIyNzIx.XiJJBg.1_CUaekoQBhqW3eRB0UQ4oRBWhc
#permission: 522304
#https://discordapp.com/oauth2/authorize?client_id=667878933185822721&scope=bot&permissions=522304
