import discord
import string
from sylcnt import *
punct = string.punctuation

client = discord.Client()

conf = open("pyku.conf", "r")
token = conf.readline().replace('token:', '').strip(string.whitespace)
channel = conf.readline().replace('channel:', '').strip(string.whitespace)
conf.close()
print(token)
print(channel)
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.channel.name == channel:
        haiku = message.content.split("\n")
        if len(haiku) == 3:
            haiku0 = haiku[0].split(" ")
            haiku1 = haiku[1].split(" ")
            haiku2 = haiku[2].split(" ")
            x = 0
            syb0 = 0
            for i in haiku0:
                print(haiku0[x] + ":" + str(nsyl(haiku0[x].strip(punct))[0]))
                syb0 += nsyl(haiku0[x].strip(punct))[0]
                if nsyl(haiku0[x].strip(punct))[0] == 0:
                    syb0 += gsyl(haiku0[x].strip(punct))
                    print("guess:" + haiku0[x] + ":" + str(gsyl(haiku0[x].strip(punct))))
                x += 1
            print("total 0")
            print(syb0)
            x = 0
            syb1 = 0
            for i in haiku1:
                print(haiku1[x] + ":" + str(nsyl(haiku1[x].strip(punct))[0]))
                syb1 += nsyl(haiku1[x].strip(punct))[0]
                if nsyl(haiku1[x].strip(punct))[0] == 0:
                    syb1 += gsyl(haiku1[x].strip(punct))
                    print("guess:" + haiku1[x] + ":" + str(gsyl(haiku1[x].strip(punct))))
                x += 1
            print("total 1")
            print(syb1)
            x = 0
            syb2 = 0
            for i in haiku2:
                print(haiku2[x] + ":" + str(nsyl(haiku2[x].strip(punct))[0]))
                syb2 += nsyl(haiku2[x].strip(punct))[0]
                if nsyl(haiku2[x].strip(punct))[0] == 0:
                    syb2 += gsyl(haiku2[x].strip(punct))
                    print("guess:" + haiku2[x] + ":" +  str(gsyl(haiku2[x].strip(punct))))
                x += 1
            print("total 2")
            print(syb2)
            if syb0 == 5 & syb1 == 7 & syb2 == 5:
                print("good one")
            else:
                print("not good: wrong syllable count")
                await client.delete_message(message)
        else:
            print("not good: line error")
            await client.delete_message(message)

client.run(token)
