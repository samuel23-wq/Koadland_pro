import discord
import random
import os
import requests 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def coin_flip():  
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Sello"
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user} \n Si necesitas ayuda escribe "$ayuda" ')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}! \n Si necesitas ayuda escribe "$ayuda"')

@bot.command()
async def flip_coin(ctx):
    await ctx.send(f'El resultado es: {coin_flip()}!')  

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('imagenes'))  
    with open(f'imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def random_pass(ctx):
    await ctx.send(f'Hola, tu contraseña aleatoria es {gen_pass(8)}!')

@bot.command()
async def me(ctx):
    img_name = 'm_ambiente.jpg' 
    
    ruta_imagen = f'imagenes/{img_name}'
    if os.path.exists(ruta_imagen):
        with open(ruta_imagen, 'rb') as f:
            picture = discord.File(f)
            await ctx.send("Aquí tienes la imagen solicitada:", file=picture)
            await ctx.send("estos son algunos consejos para mejorar el medio ambiente")

    else:
        await ctx.send(f"Error: No encontré el archivo `{img_name}` en la carpeta 'imagenes'.")

@bot.command(name="ayuda")
async def ayuda(ctx):
    embed = discord.Embed(
        title="Guía de Comandos del Bot",
        description="Aquí tienes la lista de comandos disponibles:",
        color=discord.Color.blue()
    )

    embed.add_field(name="$hello", value="El bot te saluda.", inline=False)
    embed.add_field(name="$random_pass [n]", value="Genera una contraseña aleatoria. Ej: $random_pass 12", inline=False)
    embed.add_field(name="$duck", value="Envía una imagen aleatoria de un pato.", inline=False)
    embed.add_field(name="$flip_coin", value="Lanza una moneda.", inline=False)
    embed.add_field(name="$mem", value="Muestra una imagen aleatoria de la carpeta 'imagenes'.", inline=False)
    embed.add_field(name="$me", value="Muestra la imagen del medio ambiente.", inline=False)

    await ctx.send(embed=embed)

bot.run("token") 

