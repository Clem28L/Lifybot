import discord
from discord.ext import commands
import logging
import datetime
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.utils.manage_components import *
import json


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
warnings = {}
slash = SlashCommand(bot, sync_commands=True)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():


    activity = discord.Game(name="Bot developpé par L28C#4703 | Pour plus d'infos venir MP ", type=2)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Le bot est prêt.")
    fichier = open("data.txt", "a")
    fichier.write("\nbot en ligne à " + str(datetime.datetime.now()))
    fichier.close()
    embed = discord.Embed(
        title= "Le bot est prét à l'utilisation" ,
        description="LifyBot est la pour vous protégé",
        colour= discord.Colour.blue()
    )
    await bot.get_channel(842020507934916652).send(embed=embed)

@bot.event()
async def on_member_join(member):
    with open('file.json', 'r') as file:
        data = json.load(file)

    buttons = [
        create_button(
            style=ButtonStyle.blue,
            label=data["responsecorecte1"],
            custom_id ="oui"
        ),
        create_button(
            style=ButtonStyle.green,
            label=data["responseincorecte1"],
            custom_id="non"
        )
    ]
    action_row = create_actionrow(*buttons)

    fait_choix = await ctx.send(data["question1"], components=[action_row])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    button_ctx = await wait_for_component(bot, components=action_row, check=check)
    if button_ctx.custom_id == "oui":
        await button_ctx.edit_origin(content=await choix2(ctx, user))
    else:
        await button_ctx.edit_origin(content="nop")



async def choix2(ctx, user ):
    with open('file.json', 'r') as file:
        data = json.load(file)

    buttons = [
        create_button(
            style=ButtonStyle.blue,
            label=data["responsecorecte2"],
            custom_id ="oui"
        ),
        create_button(
            style=ButtonStyle.green,
            label=data["responseincorecte2"],
            custom_id="non"
        )
    ]
    action_row = create_actionrow(*buttons)
    fait_choix = await ctx.send(data["question2"], components=[action_row])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    button_ctx = await wait_for_component(bot, components=action_row, check=check)
    if button_ctx.custom_id == "oui":
        await button_ctx.edit_origin(content="bravoooo ton grade a bien été ajouté")
        Role = discord.utils.get(user.guild.roles, name="test")
        await .add_roles(Role)
    else:
        await button_ctx.edit_origin(content="nop nop")


bot.run("ODc1MzcxMDY0OTY2OTA1ODc3.YRUi1Q.kTI13R5DF30E-CJseyqYNc_Q7AM")