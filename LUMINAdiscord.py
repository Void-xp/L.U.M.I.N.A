import discord
import os
import random
from discord.ext import commands, tasks
from dotenv import load_dotenv
load_dotenv()
intents = discord.Intents.default()
intents.members = True # sert à détecter les nouveaux membres
print("Starting...")
# Logic Unit Management Intergration Network Administration
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
messages = [
    "Hi",
    "The reactor is safe",
    "Today is pizza day !!!",
    "Keep calm and code on",
    "The system is running smoothly",
    "Hello from the bot!",
    "Everything is under control",
    "Don't forget to take breaks",
    "Safety first!",
    "Check your logs regularly",
    "Time for a coffee break",
    "System update completed",
    "The mission continues",
    "Hello world!",
    "Keep your energy up",
    "Stay focused and keep going",
    "Random message activated",
    "Everything is looking good",
    "Have a great day!",
    "The bot says hi"
]

@client.event # sans ça la def(func) marche pas
async def on_ready(): # le async sére à lancer séparément la func comme le task.spawn
    print("Bot Online")
    # syncroniser les commands
    try:
        #sync
        synced = await client.tree.sync()
        print(f"Commands sync: {len(synced)}") # le f permet d'éxecuter quelque chose entre crochet dans les prints
    except Exception as e:
        print(e)
    
       # Démarre la boucle si elle n’est pas déjà lancée
    if not send_random_message.is_running():
        send_random_message.start()

    game = discord.Game("Aurora Management system")
    
    await client.change_presence(status=discord.Status.online, activity=game)


# ✅ Slash command pour envoyer un message aléatoire
@client.tree.command(name="send_random_message", description="send Rmessage")
async def randommsg(interaction: discord.Interaction):
    msg = random.choice(messages)
    await interaction.response.send_message(msg)

# ✅ Slash command pour activer/désactiver la boucle
@client.tree.command(name="set_random_message", description="set Rmessage")
async def random_messages_status(interaction: discord.Interaction, status: bool):
    if status:
        if not send_random_message.is_running():
            send_random_message.start()
            await interaction.response.send_message("✅ Rmessage online!")
        else:
            await interaction.response.send_message("⚠️ Rmessage online")
    else:
        if send_random_message.is_running():
            send_random_message.stop()
            await interaction.response.send_message("🛑 Rmessage offline !")
        else:
            await interaction.response.send_message("⚠️ Rmessage offline")

@client.event
async def on_member_join(member):
     # Envoie un message dans le salon de bienvenue
    channel = discord.utils.get(member.guild.text_channels, name="system")
    if channel:
        await channel.send(f"Welcom {member.mention}! 🎉")

@tasks.loop(minutes= 30)
async def send_random_message():
     channel = discord.utils.get(client.get_all_channels(), name="general-all-language")  
     if channel: 
         msg = random.choice(messages)
         await channel.send(msg)
     else:
         print("channel not foud :(")
     



@client.event
async def on_message(message: discord.Message):
    # empêche le bot de se déclencher lui même
    if message.author.bot:
        return
    if message.content.lower() == 'idk125': # le lower il traduit tous en minuscule si j'écris HELLO ou HelLo ça marche quand même
        channel = message.channel # crée une variable avec la channel du msg
        await channel.send(" how are u?") # répond au msg et le await et comme le task.spawn mais async peut s'attribuer que à une def
    elif message.content.lower() == "777f":
        author = message.author
        await author.send("Hi")



@client.tree.command(name="warn", description="warn a guy")
async def warn(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"Warn send to: {member}")
    await member.send("You received 1 warning, be careful next time and follow the rules!")


@client.tree.command(name="lumina", description="show lumina description")
async def show(interaction: discord.Interaction): #le interaction permet de réponddre 
    await interaction.response.send_message("Hello I'm Logic Unit Management Intergration Network Administration (L.U.M.I.N.A)")

client.run(os.getenv('DISCORD_TOKEN')) # en gros sa scan les .env et ducoup on recupere une valeur qui est dessus

