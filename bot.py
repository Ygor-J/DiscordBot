import discord # type: ignore
import time, os, sys

TOKEN = 'ODc2MjM5ODc0Mjg0NDc0NDM4.YRhL-Q.XEqD2O7_OcAyCnCEA5-XNhDVnhQ'

def main():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('You have logged in as {}'.format(client.user))

    @client.event
    async def on_message(message):
        if client.user == message.author:
            return
        if message.content == 'Responda':
            await message.channel.send('Respondido. Pronto!?')
        else:
            await message.channel.send('Digite "Responda" para eu responder')

    client.run(TOKEN)

main()