import discord #Importazione dipendenze
import logging
import discord.ext
from discord.ext import tasks
from discord.ext import commands
from discord import Embed
from discord.ext.forms import Form
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
bot = commands.Bot(command_prefix='>')

logger = logging.getLogger('discord')#Generatore log "discord.log"
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(client))#Info Console
    
    activity = discord.Game(name="Guardando The Loading... Kingdom ", type=3)#Attività del bot
   
    await client.change_presence(status=discord.Status.online, activity=activity)#Attività del bot (Non Toccare)


@client.event
async def on_message(message):#Comandi
      
    if message.author == client.user:return
    
    if message.content.startswith('>help'):#i comandi del server (Help)
        embedVar = discord.Embed(title="Elenco Comandi", description="Prefix `>`", color=0x1613e8)
        embedVar.add_field(name="`>`regole", value="Mostra le regole", inline=True)
        embedVar.add_field(name="`>`verifica", value="Crea un semplice embed di verifica", inline=True)
        embedVar.add_field(name="`>`upordown", value="Controlla Se il bot è online", inline=True)
        embedVar.add_field(name="`>`Ciao", value="Controlla Se Tutto Funziona Bene", inline=True)
        embedVar.add_field(name="`>`me", value="Controlla Se Tutto Funziona Bene", inline=True)
        embedVar.add_field(name="`>`💡", value="Luce", inline=True)
        embedVar.set_footer(text="Developed By Fredbear07", icon_url="https://i.imgur.com/kPODHwt.gif")
        await message.channel.send(embed=embedVar)
        
    if message.content.startswith('>regole'):#le regole del server
        embedVar = discord.Embed(title="Regole", description="Regole", color=0x1613e8)
        embedVar.add_field(name="1. Non insultare gli altri membri", value="**Pena Warn**", inline=True)
        embedVar.add_field(name="2. La pornografia è ammessa solo nella chat NSFW", value="**Pena Ban**", inline=True)
        embedVar.add_field(name="3. Pedo e gore non sono ammessi nemmeno nella chat NSFW", value="**Pena Ban**", inline=True)
        embedVar.add_field(name="4. Tutte le stanze hanno una utilità specifica", value="**Pena Warn**", inline=True)
        embedVar.add_field(name="5. È vietato disturbare con rumori assordanti/fastidiosi e utilizzare modificatori di voce", value="**Pena Warn**", inline=True)
        embedVar.add_field(name="6. E vietato discutere con staff per ban altrui", value="**Pena temp Ban 1 Settimana**", inline=True)
        embedVar.set_footer(text="Developed By Fredbear07", icon_url="https://i.imgur.com/kPODHwt.gif")
        await message.channel.send(embed=embedVar)
    
    if message.content.startswith('>verifica'):#la verifica del server
        embedVar = discord.Embed(title="Identificati", description="Clicca ✅ Per Identificarti", color=0x1613e8)
        embedVar.set_footer(text="Developed By Fredbear07", icon_url="https://i.imgur.com/kPODHwt.gif")
        await message.channel.send(embed=embedVar)

    if message.content.startswith('>aw'):#comando di test per gli embed (da Rimuovere)
        embedVar = discord.Embed(title="Verifica", description="Clicca ✅ per verificarti", color=0x1613e8)
        embedVar.set_footer(text="Developed By Fredbear07", icon_url="https://i.imgur.com/MaYzufS.gif")
        await message.channel.send(embed=embedVar)
 
    
    if message.content.startswith('>upordown'):#comando di test per le emoji (Da Rimuovere)
        await message.channel.send('Se hai ricevuto questo messaggio il bot è Up! <:stella:833977385274966027>')

    if message.content.startswith('>Ciao'):#comando di test (Da Rimuovere)
        await message.channel.send('Ciao!')

    if message.content.startswith('>me'):#comando di test (Da Rimuovere)
        await message.channel.send('me!')
    
    if message.content.startswith('UniverseHubBot'):#comando di test (Da Rimuovere)
        await message.channel.send('Il mio prefix è `>`')

    if message.content.startswith('>💡'):#comando di test (Da Rimuovere)
        await message.channel.send('<@759400024966299689>!')
    
     
client.run('TOKEN')
