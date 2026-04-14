from datetime import datetime, timezone
import os 
import discord 
from discord import app_commands 
from dotenv import load_dotenv


load_dotenv() 


TOKEN = os.getenv("DISCORD_TOKEN") 


class MyClient(discord.Client): 
    def __init__(self): 
        intents = discord.Intents.default() 
        super().__init__(intents=intents) 
        self.tree = app_commands.CommandTree(self) 
    
    
    async def setup_hook(self): 
        synced = await self.tree.sync() 
        print(f"Comandi sincronizzati: {len(synced)}") 
        
client = MyClient() 

@client.tree.command( name="remind30mins", description="Sends a reminder 30 minutes before the event starts." ) 
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def remind(interaction: discord.Interaction): 
    await interaction.response.send_message( "# 30 MINUTES REMINDER\n\n@everyone",allowed_mentions=discord.AllowedMentions(everyone=True) ) 


events = {
    0: "No",
    1: "<t:1765485000:t>",
    2: "No",
    3: "<t:1770139800:t>",
    4: "<t:1765485000:t>",
    5: "<t:70200:t>",
    6: "<t:70200:t>",      
}

@client.tree.command( name="battle_time", description="Prints out the times battle for the current day" )
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True) 
async def battleTime(interaction: discord.Interaction): 
    
    today = datetime.now(timezone.utc).weekday()
    battleTime = ""

    if today == 0 or  today == 2:
        battleTime = "# No battle today! ): \n\n@everyone" 

    else:

        battleTime = events[today]

    await interaction.response.send_message( f"# BATTLE AT: {battleTime}!\n WHOS GONNA JOIN?\n\n@everyone" ,allowed_mentions=discord.AllowedMentions(everyone=True), delete_after=120) 




client.run(TOKEN)