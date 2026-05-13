import random
import asyncio

async def hello(message,args,client):
    user=message.author.display_name
    await message.channel.send(f"Hello {user} ^^")

async def choose(message,args,client):
    
    if not args:
        await message.channel.send("Gimme choices first hmph hmph")
        return

    choices=" ".join(args).split(",")
    # if choice.strip() removes empty choices
    choices=[choice.strip() for choice in choices if choice.strip()]
    ans=random.choice(choices)

    await message.channel.send(f"I choose {ans}!")

async def invite(message,args,client):

    if not message.author.voice:
        await message.channel.send("Join a VC first ;-;")
        return
    
    if not message.mentions:
        await message.channel.send("Who do I invite ;-;")
        return
    
    vc=message.author.voice.channel

    mentioned= ", ".join(user.mention for user in message.mentions)

    invite= await vc.create_invite()

    await message.channel.send(f"{mentioned} join vc fas fas\n{invite.url}")

async def summon(message,args,client):

    if not message.mentions:
        await message.channel.send("Who do I summon ;-;")
        return
    
    target=message.mentions[0]

    await message.channel.send("Conjuring up ingredients for the holy summon...")

    def check(m):
        return m.author==target and m.channel==message.channel
    
    attempts=0

    while True:

        await message.channel.send(f"{target.mention} where art thouuuu")

        try:
            await client.wait_for("message",timeout=10,check=check)
            await message.channel.send(f"My job here is done \:)")
            break
        except asyncio.TimeoutError:
            attempts+=1
            if(attempts>=6):
                await message.channel.send("I give up \:(")
                break
            else:
                pass
