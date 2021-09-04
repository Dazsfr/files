import discord
from discord import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'bb!lsgddownloadlinksprivatecode299938879103288743909183899123889912988739912':
        await message.delete()
        embed = discord.Embed(title="LSGD Download Links", colour=discord.Colour(0x8d7fca), description="[Site link](https://lsgd.tk/)\n\nLinks:")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/864473934081425449/0bb16fe249888b8254ba0c38e58ab9cd.webp?size=128")
        embed.set_author(name="LSGD", url="https://discord.com/invite/FwZjRqbxT3", icon_url="https://cdn.discordapp.com/icons/864473934081425449/0bb16fe249888b8254ba0c38e58ab9cd.webp?size=128")
        embed.set_footer(text="For DeXotik", icon_url="https://cdn.discordapp.com/avatars/665339590487572513/a_383ab79f6143557d3acebb37d3785422.webp?size=128")

        embed.add_field(name="<:Android:883802942656897115> Android:", value="[Download](https://lsgd.tk/download/lsgd.apk)")
        embed.add_field(name="🪟 Windows:", value="[Download](https://lsgd.tk/download/lsgd.zip)")
        embed.add_field(name="<:vk:883803395180355676> VK Group:", value="[Visit](https://vk.com/lsgd_server)")

        await message.channel.send(embed=embed)

client.run('')