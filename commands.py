import random

async def hello(message,args):
    user=message.author.display_name
    await message.channel.send(f"Hello {user} ^^")

async def choose(message,args):
    
    if not args:
        await message.channel.send("Gimme choices first hmph hmph")
        return

    choices=" ".join(args).split(",")
    # if choice.strip() removes empty choices
    choices=[choice.strip() for choice in choices if choice.strip()]
    ans=random.choice(choices)

    await message.channel.send(f"I choose {ans}!")

async def invite(message,args):

    if not message.author.voice:
        await message.channel.send("Join a VC first ;-;")
        return
    
    vc=message.author.voice.channel

    mentioned= ", ".join(user.mention for user in message.mentions)

    invite= await vc.create_invite()

    await message.channel.send(f"{mentioned} join vc fas fas\n{invite.url}")

