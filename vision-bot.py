import discord
import requests
import asyncio

client = discord.Client()
requests.packages.urllib3.disable_warnings()
url = "https://127.0.0.1:2999/liveclientdata/playerlist"
champions = []
vision = []

@client.event
async def on_ready():
    print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$game'):
        try:
            replace = False
            #counter = 0
            while True:
                checkVision()
                msg = ""
                embedVar = discord.Embed(title="Vision Score", color=0x00ff00)
                #embedVar.add_field(name="counter", value=counter, inline=False)
                for i in range(len(champions)):
                    msg += f"Champion: {champions[i]}\nVision Score: {vision[i]}\n\n"
                    embedVar.add_field(name=champions[i], value=vision[i], inline=False)
                if replace == True:
                    await post.edit(embed=embedVar)
                else:
                    post = await message.channel.send(embed=embedVar)
                    replace = True
                #counter += 1
                print(champions)
                print(vision)
                await asyncio.sleep(10)
        except Exception as e:
            if "WinError 10061" in str(e):
                print("No game instance")
                await message.channel.send("No game instance")
            print(e)


def checkVision():
    vision.clear()
    champions.clear()
    req = requests.get(url, verify=False)
    for line in str(req.text).split('\n'):
        if '\"championName\":' in line:
            champions.append(line.split(':')[1].strip().split('\"')[1].strip('\"'))
        if '\"wardScore\":' in line:
            vision.append(line.split(':')[1].strip())

client.run('redacted-token')
