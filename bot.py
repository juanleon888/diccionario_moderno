import discord
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$commands'):
        await message.channel.send('estos son mis comandos: $hello, $smile, $coin, $dice, $bye, $pass,')
    elif message.content.startswith('$hello'):
        await message.channel.send('Hola soy ramen bot!, prueba $commands ')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(gen_coin())
    elif message.content.startswith('$dice'):
        await message.channel.send('dados de 1 a 6 caras')
        await message.channel.send(gen_dice())
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
#errores de double y secret
    # elif message.content.startswith('$double'):
    #     await message.channel.send(double_letter("Juan"))
    elif message.content.startswith('$secret'):
        await message.channel.send(secret_function(1,2))
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")


client.run("")
