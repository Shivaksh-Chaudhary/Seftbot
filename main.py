import discord
from discord.ext import commands
from pypresence import Presence
import asyncio
import random
import time
import os
import pickle


#with open('token.txt' , 'r') as file:
#    token = file.read().strip()
    

    
    
bot = commands.Bot(command_prefix='s.' , self_bot = True)



afkMode = False
afkLogs = []

 # nigga



# why 
 

specified_user_id = 68648000084063003
specified_user_id_two = 1190313847739916289
reaction_emoji = '🏴‍☠️'

client_id = 1190313847739916289

active_responders = {}

responses = ["you looks so ass even your mom don't love you","you lifeless homeless bitchless nigga","you are a black ass nigga trying to be cool","suck my dick nigga","bitch I hoed you","you slut ass dickless kid","dork I'll kill you","my lost sperm","semen licker","you broke ass work at 9/11 and your mom sell herself 24/7 to pay your debt","bitchass","faggot","femboy","shit licker","dickhead nigga","brainrotted kid","I cooked you motherfucking ass","you pedophile ass trying to hit on kids","illiterate kid","you weak af nigga","I'll rip you off","I raped your whole bloodline","dick sucker","absurdly ugly lizard","you disgusting waste of oxygen","fuck off","jerk","your mom is such a whore I fucked her twice and she wants more","nigga you suck","you are weak as your dad's protection I'll rip your ass off you dumbass bitch","worthless and jobless dick","tired of failure pointless homeless faggot","sickening disgusting piece of rot","kill yourself","you disgusting pedophile piece of shit trying to comeback","dick rider","horny ass pedophile","corny ass jr","you suck crazy ass nigga silent dirty ass pedophile no one loves you"]






@bot.event
async def on_ready():
    print ("Bot is ready")
    print("Prefix is s.")
    print("Made by ERROR")
    
@bot.event
async def on_message(message):
    if message.author.id == bot.user:
        return
    if message.author.id in active_responders:
        response = random.choice(responses)
        await message.channel.send(f"{active_responders[message.author.id]} {response}")
        

@bot.event
async def on_message(message):
    if message.author != bot.user:
        for word in notifyWords:
    if afkMode == True:
        if message.author != bot.user:
            if message.author.id not in afkLogs:
                if message.channel.type == discord.ChannelType.private:
                    await message.channel.send("Sorry, I'm currently not available!"")

                    log_message(
                        "AFK Logs",
                        f"DM from {message.author.name}#{message.author.discriminator}: {message.content}",
                        Fore.YELLOW,
                    )

                    afkLogs.append(message.author.id)
            else:
                if message.channel.type == discord.ChannelType.private:
                    log_message(
                        "AFK Logs",
                        f"{message.author.name}#{message.author.discriminator}: {message.content}",
                        Fore.YELLOW,
                    )
        else:
            await bot.process_commands(message)
    else:
        if message.author == bot.user:
            await bot.process_commands(message)            
        
        
    await bot.process_commands(message)
        
@bot.command()
async def ar(ctx , member: discord.Member):
    await ctx.message.delete()
    active_responders[member.id] = member.mention
    
@bot.command()
async def ars(ctx , member:discord.Member):
    await ctx.message.delete()
    if member.id in active_responders:
        del active_responders[member.id]
        await ctx.send("Stopped ✅")
        
    
    
    
        
        









    
        
       




    
    
       
@bot.command()
async def spam(ctx ,amount: int ,* , message:str):
   
    await ctx.message.delete()
    for _ in range(amount):
        await ctx.send(message)
        
help_message = (
    "```ERROR PRESENTS\n"
    "                  \n"
    "                 \n"
    
    "MADE BY ERROR\n"
    "                \n"
    "                \n"
    "PREFIX IS s.\n"
    "                \n"
    "                \n"
    "COMMANDS ARE :-\n"
    "                 \n"
    "Ping - s.ping\n"
    "                  \n"
    "Spam - s.spam <amount <Text>\n"
    "                      \n"
    "Fs - s.fs <amount> <Text> \n"
    "                   \n"
    "Ladder - s.ladder <amount> <sentence> \n"
    "                        \n"
    "Loop - s.loop <amount <message>\n"
    "                       \n"
    "dmm - s.dmm <amount> \n"
    "                      \n"
    "Tokencheck- s.tokencheck <token>                        \n"
    "                        \n"
    "Stream - s.stream <text to stream>                     \n"
    "                     \n"
    "Streamend - s.streamend \n"
    "                      \n"
    "Ar - s.ar <mention>            \n"
    "                       \n"
    "Ars - s.ars <mention>                  \n"
    "                        \n"
    "Gayrate - s.gayrate              \n"
    "                         \n"
    "Dc - s.dc \n"
    "                       \n"
    "Copyserver - <old id> <new id> \n"
    "                       \n"
    "Ap - s.ap <mention>                     \n"
    "                      \n"
    "Aps - s.aps  \n"
    "                  \n"
    "Smm - Mentions everyone in a server \n"
    "                       \n"
    "More commands soon\n```")
                
        
   
        
        
bot.remove_command('help')
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(help_message, delete_after = 5)

@bot.command(name = 'ladder')
async def ladder(ctx , * , message: str):
    await ctx.message.delete()
    words = message.split()
    for word in words:
        await ctx.send(word)
        await asyncio.sleep(0)
                           
@bot.command(name = 'loop')
async def loop(ctx , count:int , * ,message:str):
    await ctx.message.delete()
    for i in range(1, count+1):
        await ctx.send(f"{message} {i} ")
        await asyncio.sleep(0)
    




@bot.command(name = 'tokencheck')
async def tokencheck(ctx , token:str):
    try:
        test_bot = commands.Bot(command_prefix="+" , self_bot = True)
        await test_bot.login(token)
        await ctx.send("The token is valid")
        await test_bot.logout()
    except discord.LoginFailure:
        

        
    
        await ctx.send("The token is invalid")
    except Exception as e:
        await ctx.send(f"An error has occured: {str(e)}")
    finally:
        await client.logout()
  
 
@bot.command()
async def stream(ctx , *, title:str):
    await ctx.message.delete()
    await bot.change_presence(activity =discord.Streaming(name = title , url = "https://www.twitch.tv/ERROR69FR"))
    await ctx.send(f"Now streaming **{title}**")
    
@bot.command()
async def streamend(ctx):
    await ctx.message.delete()
    await bot.change_presence(activity=None)
    await ctx.send("stopped streaming")

@bot.command()
async def fs(ctx , amount:int , * , message :str):
    await ctx.message.delete()
    for _ in range(amount):
        await ctx.send(message)
        await asyncio.sleep(0)

@bot.command()
async def gayrate(ctx , member: discord.Member):
    await ctx.message.delete()
    if member == ctx.author:
        await ctx.send("You cant rate yourself!")
        return
    percentage = random.randint(1 , 100)
    await ctx.send(f"{member.mention} has a gayrate of **{percentage}%**!")
    
@bot.command()
async def av(ctx , member: discord.Member = None):
    await ctx.message.delete()
    if member is None:
        member= ctx.author
    embed = discord.Embed(title=f"{member.name}'s Avatar", color=discord.Color.blue())  
    avatar_url = avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed.set_image(url=avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)# Get the avatar URL


    await ctx.send(embed=embed)
        
@bot.command()
async def dc(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    channels = guild.channels
    confirmation_message = await ctx.send("Are you sure you want to delete all the channels? yes or no")
    def check (m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() == 'yes'
    try:
        await bot.wait_for('message', check=check, timeout=30)
    except asyncyio.TimeoutError:
        
            await confirmation_message.edit(content="Channel deletion canceled due to timeout.")
            return
      
        
    for channel in channels:
        try:
            await channel.delete()
        except Exepction as e:
            await ctx.send("Failed")
    await ctx.send("Done ✅")            
            
            
            
            
                     
@bot.command()
async def copyserver(ctx ,   source_guild_id:int , target_guild_id:int):
    source_guild = bot.get_guild(source_guild_id)
    target_guild = bot.get_guild(target_guild_id)
    if not source_guild or not target_guild:
        
            
        await ctx.send("Invalid source or target server ID.")
        return
    for category in source_guild.categories:
        new_category = await target_guild.create_category(category.name)
        
        for channel in category.channels:
            if isinstance(channel, discord.TextChannel):
                await target_guild.create_text_channel(channel.name, category=new_category)
                
            elif isinstance(channel, discord.VoiceChannel):
                    await target_guild.create_voice_channel(channel.name, category=new_category)
        for channel in source_guild.text_channels:  
            if channel.category is None:
                await target_guild.create_text_channel(channel.name)
        for channel in source_guild.voice_channels:
            await target_guild.create_voice_channel(channel.name)
            

@bot.command()
async def smm(ctx):
    # Fetch all members in the guild (server)
    await ctx.message.delete()
    members = ctx.guild.members
    member_count = len(members)

    if member_count >= 1000:
        # Ping half of the server members randomly
        half_count = member_count // 2
        half_members = random.sample(members, half_count)
        await ctx.send(', '.join(member.mention for member in half_members))
    elif member_count < 500:
        # Mention all members
        await ctx.send(', '.join(member.mention for member in members))
    else:
        # Randomly mention half of the members
        half_count = member_count // 2
        half_members = random.sample(members, half_count)
        await ctx.send(', '.join(member.mention for member in half_members))           
                

response_task = None

@bot.command()
async def ap(ctx, *mentions: discord.Member):
    await ctx.message.delete()
    
    global response_task

    if response_task is not None and not response_task.done():
        await ctx.send("I'm already sending responses! Use `!s.aps` to stop.")
        return

    if not mentions:
        await ctx.send("Please mention at least one user.")
        return

    async def send_responses():
        while True:
            # Randomly select a response
            response = random.choice(responses)
            # Send the response to the mentioned users
            await ctx.send(', '.join(member.mention for member in mentions) + f": {response}")
            await asyncio.sleep(0.5)  # Wait for 5 seconds before sending the next response

    # Start the task
    response_task = bot.loop.create_task(send_responses())

@bot.command()
async def aps(ctx):
    await ctx.message.delete()
    global response_task

    if response_task is not None and not response_task.done():
        response_task.cancel()
        response_task = None
        await ctx.send("Stopped sending responses.")
    else:
        await ctx.send("No ongoing response task to stop.")
        

@bot.command() # Ensure the user has permission
async def purge(ctx, amount: int):
    await ctx.message.delete()
    if amount < 1:
        await ctx.send("Please specify a number greater than 0.", delete_after=5)
        return

    await ctx.message.delete()  # Delete the command message

    deleted = 0
    async for message in ctx.channel.history(limit=amount):
        if message.author.id == bot.user.id:  # Check if the message is from the bot
            await message.delete()
            deleted += 1

      # Feedback to the user
        
@bot.command()
async def dmm(ctx, amount: int):
    if ctx.channel.type == discord.ChannelType.private:  # Check if it's a DM
        if amount < 1:
            await ctx.send("Please specify a number greater than 0.", delete_after=5)
            return

        deleted = 0
        async for message in ctx.channel.history(limit=amount):
            if message.author.id == bot.user.id:  # Check if the message is from the bot
                await message.delete()
                deleted += 1

        await ctx.send(f"Deleted {deleted} messages.", delete_after=5)  # Feedback to the user
    else:
        await ctx.send("This command can only be used in DMs.", delete_after=5)
        await asyncio.sleep(0.1)

@bot.command(
    description="Turns on AFK mode, which will automatically respond to DMs and log the messages."
)
async def afk(ctx):
    global afkMode

    if afkMode:
        await ctx.message.edit(content=f":x: | AFK mode disabled.")

        log_message("afk", "AFK mode enabled.", Fore.RED)

        afkMode = False

        afkLogs.clear()

        await bot.change_presence(status=discord.Status.online)

    else:
        await ctx.message.edit(content=f":white_check_mark: | AFK mode enabled.")

        log_message("afk", "AFK mode enabled.", Fore.RED)

        afkMode = True

        await bot.change_presence(status=discord.Status.idle)

    await delete_after_timeout(ctx.message)
    
bot.run(token=os.environ.get('token'))

    
            

    
    
    

                        
    

