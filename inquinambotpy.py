import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
    #await send("Il bot è acceso, scrivi lista per avere la lista dei comandi")


@bot.command()
async def lista(ctx):
    await ctx.send("Ecco una lista di comandi:")
    await ctx.send("bottiglietta")
    await ctx.send("fazzoletto")
    await ctx.send("frutta")
    await ctx.send("rifiutielettronici")
    await ctx.send("libri")
    await ctx.send("quaderni")

@bot.command()
async def bottiglietta(ctx):
    await ctx.send("Va buttata nella plastica")

@bot.command()
async def fazzoletto(ctx):
    await ctx.send("Va buttato nelll'umido")

@bot.command()
async def frutta(ctx):
    await ctx.send("Va buttata nella plastica")

@bot.command()
async def rifiutielettronici(ctx):
    await ctx.send("Vanno buttati nell'indifferenziata")

@bot.command()
async def libri(ctx):
    await ctx.send("Possono essere rivenduti o vanno buttati in carta")

@bot.command()
async def quaderni(ctx):
    await ctx.send("Vanno buttati in carta")

@bot.command()
async def progetto(ctx):
    await ctx.send(gen_prog)

def gen_prog():
    lista_prg = "Astuccio bottiglia","Cestini con il cartone","Decorazioni con la carta"
    prg_name = ""   
    prg_name = random.choice(lista_prg)
    return prg_name

bot.run('token')
