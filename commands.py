async def hello(message,args):
    user=message.author.display_name
    await message.channel.send(f"Hello {user}!")