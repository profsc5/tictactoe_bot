#SISYPHUS 

import discord
import os
import tictactoe
from dotenv import load_dotenv
number= int()
victory_message=str()
client = discord.Client()
load_dotenv(".env")


def victory():   
        if tictactoe.victory_for()== "Tie":
            victory_message = "TIE!"
        else:
            victory_message = "Victory for " + tictactoe.victory_for() + " <:crown:921428240273408023>" 
        return victory_message


def restart():
    tictactoe.board = tictactoe.reset_game()
    tictactoe.make_list_of_free_fields()
    return tictactoe.display_board()


def move(messageP):
    cnt = int(0)
    for x in messageP.content:
        if type(x) is str:
            try:
                number = int(x)
                cnt+=1
            except:
                continue  
    if cnt == 1:
        tictactoe.make_list_of_free_fields()
        tictactoe.enter_move(number)
        tictactoe.make_list_of_free_fields()
        tictactoe.draw_move()
        tictactoe.make_list_of_free_fields()
        if tictactoe.victory_for() is not None:
            return victory()       
        return tictactoe.display_board()
    else:
        return "That doesn't seem right <:pensive:921421036916965436>"
  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("*board"):
        await message.channel.send(tictactoe.display_board())

    elif message.content.startswith("*mv"):
        await message.channel.send(move(message))

    elif message.content.startswith("*commands"):
        with open("commands.txt") as commands:
            await message.channel.send(commands.read())

    elif message.content.startswith("*r"):
        await message.channel.send(restart())
    
        

client.run(os.getenv("TOKEN"))