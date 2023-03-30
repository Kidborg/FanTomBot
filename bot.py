import os
import discord
from discord.ext import commands

# задаем параметры бота
bot = commands.Bot(command_prefix="!")




# словарь соответствий реакций и ролей
roles = {
    "🟥": 1090169572960784506,  # замените здесь ID роли
    "🟧": 1090169663054426162,
    "🟨": 1090169697162498108,
}


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to the Discord API.")


@bot.event
async def on_raw_reaction_add(event):
    if event.user_id == bot.user.id:
        return

    # получаем необходимые объекты
    guild = bot.get_guild(event.guild_id)
    member = await guild.fetch_member(event.user_id)
    emoji = event.emoji.name

    # находим нужную роль
    role_id = roles.get(emoji)
    if not role_id:
        return
    role = guild.get_role(role_id)
    if not role:
        return

    # добавляем роль участнику
    await member.add_roles(role)
    print(f"{member.display_name} was given {role.name}")


@bot.event
async def on_raw_reaction_remove(event):
    if event.user_id == bot.user.id:
        return

    # получаем необходимые объекты
    guild = bot.get_guild(event.guild_id)
    member = await guild.fetch_member(event.user_id)
    emoji = event.emoji.name

    # находим нужную роль
    role_id = roles.get(emoji)
    if not role_id:
        return
    role = guild.get_role(role_id)
    if not role:
        return

    # удаляем роль у участника
    await member.remove_roles(role)
    print(f"{member.display_name} was removed {role.name}")

@bot.slash_command(name='sendmsg')
async def send(ctx, message):
    await ctx.send(message)

@bot.slash_command(name='sendbut')
async def sendmsg(ctx, channel_id, *, message):
    channel = bot.get_channel(int(channel_id))
    await channel.send(message)

@bot.slash_command(name = 'quiz')
async def quiz(ctx, question, answer):
    await ctx.send(f"Вопрос: {question}")

    user_answer = await bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == ctx.channel)
    while not user_answer.content == answer:
        await ctx.send(f"Неправильно")
        user_answer = await bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == ctx.channel)
    else:
        await ctx.send("Правильно!")
        roles = [role.name for role in ctx.author.roles]
        if '📊〡Математик 1' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 1")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 2")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 2' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 2")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 3")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 3' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 3")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 4")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 4' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 3")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 4")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 5' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 4")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 5")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 6' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 5")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 6")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 7' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 6")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 7")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 8' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 7")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 8")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 9' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 9")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 10")
            await ctx.author.add_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 1")
            await ctx.author.add_roles(role)


import json
from PIL import Image, ImageDraw, ImageFont
@bot.slash_command(name='textimage')
async def textimage(ctx, *, text: str):
    W, H = (500, 500)
    font = ImageFont.truetype('arial.ttf', 40)
    img = Image.new('RGB', (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    draw.text(((W-w)/2, (H-h)/2), text, fill=(0, 0, 0), font=font)
    img.save('text.png')
    await ctx.send(file=discord.File('text.png'))

shop_items = {
    "wood": {
        "price": 10,
        "description": "A piece of wood"
    },
    "stone": {
        "price": 20,
        "description": "A piece of stone"
    },
    "iron": {
        "price": 30,
        "description": "A piece of iron"
    }
}

# словарь со списком доступных работ и зарплатами
jobs = {
    "woodcutter": {
        "salary": 50,
        "cooldown": 60
    },
    "miner": {
        "salary": 70,
        "cooldown": 120
    }
}

# словарь с мини-играми казино
casino_games = {
    "coin_flip": {
        "description": "Flip a coin, if it lands on heads you double your money, if it lands on tails you lose everything!",
        "win_chance": 0.5,
        "multiplier": 2
    },
    "roulette": {
        "description": "Pick a color (red or black) and a number (1-6). If the color and number match, you win!",
        "win_chance": 0.16,
        "multiplier": 6
    },
    "slot_machine": {
        "description": "Pull the lever and try to match 3 symbols on the reels. Each symbol has a different payout!",
        "win_chance": 0.1,
        "multiplier": 10
    }
}

# словарь с текущим состоянием пользователя
def create_user(user_id):
    return {
        "money": 100,
        "inventory": {},
        "job": None,
        "job_cooldown": 0
    }
users = {}
# команда для просмотра профиля пользователя
@bot.slash_command(name="profile", description="View your profile.")
async def profile(ctx):
    user_id = ctx.author.id
    if user_id in users:
        user = users[user_id]
        money = user['money']
        inventory = user['inventory']
        job = user['job']
        job_cooldown = user['job_cooldown']
        message = f"**Username:** {ctx.author.name}\n\n**Money:** {money}\n\n**Inventory:**\n"
        if inventory:
            for item, amount in inventory.items():
                message += f"{item}: {amount}\n"
        else:
            message += "Empty"
        message += f"\n**Job:** {job or 'None'}"
        if job_cooldown > 0:
            message += f"\n**Job cooldown:** {job_cooldown} seconds"
        await ctx.send(message)
    else:
        users[user_id] = create_user(user_id)
        await ctx.send("User created.")

# команда для просмотра списка товаров в магазине
@bot.slash_command(name="shop", description="View the shop.")
async def shop(ctx):
    message = "**Shop:**\n"
    for item, data in shop_items.items():
        message += f"{item}: {data['description']} - Price: {data['price']}\n"
    await ctx.send(message)

# команда для покупки товара в магазине
@bot.slash_command(name="buy", description="Buy an item from the shop.")
async def buy(ctx, item: str):
    user_id = ctx.author.id
    if user_id not in users:
        users[user_id] = create_user(user_id)
    user = users[user_id]
    if item not in shop_items:
        await ctx.send("Item not found.")
        return
    price = shop_items[item]['price']
    if user['money'] < price:
        await ctx.send("Not enough money.")
        return
    if item in user['inventory']:
        user['inventory'][item] += 1
    else:
        user['inventory'][item] = 1
    user['money'] -= price
    await ctx.send(f"{item} purchased for {price}.")

# команда для просмотра списка доступных работ
@bot.slash_command(name="view_jobs", description="View available jobs.")
async def view_jobs(ctx):
    message = "**Jobs:**\n"
    for job, data in jobs.items():
        message += f"{job}: Salary - {data['salary']}, Cooldown - {data['cooldown']}\n"
    await ctx.send(message)

# команда для получения работы
@bot.slash_command(name="get_job", description="Get a job.")
async def get_job(ctx, job: str):
    user_id = ctx.author.id
    if user_id not in users:
        users[user_id] = create_user(user_id)
    user = users[user_id]
    if job not in jobs:
        await ctx.send("Job not found.")
        return
    user['job'] = job
    user['job_cooldown'] = jobs[job]['cooldown']
    await ctx.send(f"Got job: {job}.")

# команда для выполнения работы и получения зарплаты
@bot.slash_command(name="work", description="Go to work.")
async def work(ctx):
    user_id = ctx.author.id
    if user_id not in users:
        users[user_id] = create_user(user_id)
    user = users[user_id]
    if not user['job']:
        await ctx.send("You don't have a job.")
        return
    if user['job_cooldown'] > 0:
        await ctx.send(f"Job cooldown: {user['job_cooldown']} seconds.")
        return
    user['money'] += jobs[user['job']]['salary']
    user['job_cooldown'] = jobs[user['job']]['cooldown']
    await ctx.send(f"Earned {jobs[user['job']]['salary']}.")

import os
import discord
from discord.ext import commands

# задаем параметры бота
bot = commands.Bot(command_prefix="!")




# словарь соответствий реакций и ролей
roles = {
    "🟥": 1090169572960784506,  # замените здесь ID роли
    "🟧": 1090169663054426162,
    "🟨": 1090169697162498108,
}


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to the Discord API.")


@bot.event
async def on_raw_reaction_add(event):
    if event.user_id == bot.user.id:
        return

    # получаем необходимые объекты
    guild = bot.get_guild(event.guild_id)
    member = await guild.fetch_member(event.user_id)
    emoji = event.emoji.name

    # находим нужную роль
    role_id = roles.get(emoji)
    if not role_id:
        return
    role = guild.get_role(role_id)
    if not role:
        return

    # добавляем роль участнику
    await member.add_roles(role)
    print(f"{member.display_name} was given {role.name}")


@bot.event
async def on_raw_reaction_remove(event):
    if event.user_id == bot.user.id:
        return

    # получаем необходимые объекты
    guild = bot.get_guild(event.guild_id)
    member = await guild.fetch_member(event.user_id)
    emoji = event.emoji.name

    # находим нужную роль
    role_id = roles.get(emoji)
    if not role_id:
        return
    role = guild.get_role(role_id)
    if not role:
        return

    # удаляем роль у участника
    await member.remove_roles(role)
    print(f"{member.display_name} was removed {role.name}")

@bot.slash_command(name='sendmsg')
async def send(ctx, message):
    await ctx.send(message)

@bot.slash_command(name='sendbut')
async def sendmsg(ctx, channel_id, *, message):
    channel = bot.get_channel(int(channel_id))
    await channel.send(message)

@bot.slash_command(name = 'quiz')
async def quiz(ctx, question, answer):
    await ctx.send(f"Вопрос: {question}")

    user_answer = await bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == ctx.channel)
    while not user_answer.content == answer:
        await ctx.send(f"Неправильно")
        user_answer = await bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == ctx.channel)
    else:
        await ctx.send("Правильно!")
        roles = [role.name for role in ctx.author.roles]
        if '📊〡Математик 1' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 1")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 2")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 2' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 2")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 3")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 3' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 3")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 4")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 4' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 3")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 4")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 5' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 4")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 5")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 6' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 5")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 6")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 7' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 6")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 7")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 8' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 7")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 8")
            await ctx.author.add_roles(role)
        elif '📊〡Математик 9' in roles:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 9")
            await ctx.author.remove_roles(role)
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 10")
            await ctx.author.add_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="📊〡Математик 1")
            await ctx.author.add_roles(role)


import json
from PIL import Image, ImageDraw, ImageFont
@bot.slash_command(name='textimage')
async def textimage(ctx, *, text: str):
    W, H = (500, 500)
    font = ImageFont.truetype('arial.ttf', 40)
    img = Image.new('RGB', (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    draw.text(((W-w)/2, (H-h)/2), text, fill=(0, 0, 0), font=font)
    img.save('text.png')
    await ctx.send(file=discord.File('text.png'))

shop_items = {
    "wood": {
        "price": 10,
        "description": "A piece of wood"
    },
    "stone": {
        "price": 20,
        "description": "A piece of stone"
    },
    "iron": {
        "price": 30,
        "description": "A piece of iron"
    }
}

# словарь со списком доступных работ и зарплатами
jobs = {
    "woodcutter": {
        "salary": 50,
        "cooldown": 60
    },
    "miner": {
        "salary": 70,
        "cooldown": 120
    }
}

# словарь с мини-играми казино
casino_games = {
    "coin_flip": {
        "description": "Flip a coin, if it lands on heads you double your money, if it lands on tails you lose everything!",
        "win_chance": 0.5,
        "multiplier": 2
    },
    "roulette": {
        "description": "Pick a color (red or black) and a number (1-6). If the color and number match, you win!",
        "win_chance": 0.16,
        "multiplier": 6
    },
    "slot_machine": {
        "description": "Pull the lever and try to match 3 symbols on the reels. Each symbol has a different payout!",
        "win_chance": 0.1,
        "multiplier": 10
    }
}

# словарь с текущим состоянием пользователя
def create_user(user_id):
    return {
        "money": 100,
        "inventory": {},
        "job": None,
        "job_cooldown": 0
    }
users = {}
# команда для просмотра профиля пользователя
@bot.slash_command(name="profile", description="View your profile.")
async def profile(ctx):
    user_id = ctx.author.id
    if user_id in users:
        user = users[user_id]
        money = user['money']
        inventory = user['inventory']
        job = user['job']
        job_cooldown = user['job_cooldown']
        message = f"**Username:** {ctx.author.name}\n\n**Money:** {money}\n\n**Inventory:**\n"
        if inventory:
            for item, amount in inventory.items():
                message += f"{item}: {amount}\n"
        else:
            message += "Empty"
        message += f"\n**Job:** {job or 'None'}"
        if job_cooldown > 0:
            message += f"\n**Job cooldown:** {job_cooldown} seconds"
        await ctx.send(message)
    else:
        users[user_id] = create_user(user_id)
        await ctx.send("User created.")

# команда для просмотра списка товаров в магазине
@bot.slash_command(name="shop", description="View the shop.")
async def shop(ctx):
    message = "**Shop:**\n"
    for item, data in shop_items.items():
        message += f"{item}: {data['description']} - Price: {data['price']}\n"
    await ctx.send(message)

# команда для покупки товара в магазине
@bot.slash_command(name="buy", description="Buy an item from the shop.")
async def buy(ctx, item: str):
    user_id = ctx.author.id
    if user_id not in users:
        users[user_id] = create_user(user_id)
    user = users[user_id]
    if item not in shop_items:
        await ctx.send("Item not found.")
        return
    price = shop_items[item]['price']
    if user['money'] < price:
        await ctx.send("Not enough money.")
        return
    if item in user['inventory']:
        user['inventory'][item] += 1
    else:
        user['inventory'][item] = 1
    user['money'] -= price
    await ctx.send(f"{item} purchased for {price}.")

# команда для просмотра списка доступных работ
@bot.slash_command(name="view_jobs", description="View available jobs.")
async def view_jobs(ctx):
    message = "**Jobs:**\n"
    for job, data in jobs.items():
        message += f"{job}: Salary - {data['salary']}, Cooldown - {data['cooldown']}\n"
    await ctx.send(message)

# команда для получения работы
@bot.slash_command(name="get_job", description="Get a job.")
async def get_job(ctx, job: str):
    user_id = ctx.author.id
    if user_id not in users:
        users[user_id] = create_user(user_id)
    user = users[user_id]
    if job not in jobs:
        await ctx.send("Job not found.")
        return
    user['job'] = job
    user['job_cooldown'] = jobs[job]['cooldown']
    await ctx.send(f"Got job: {job}.")

# команда для выполнения работы и получения зарплаты
@bot.slash_command(name="work", description="Go to work.")
async def work(ctx):
    user_id = ctx.author.id
    if user_id not in users:
        users[user_id] = create_user(user_id)
    user = users[user_id]
    if not user['job']:
        await ctx.send("You don't have a job.")
        return
    if user['job_cooldown'] > 0:
        await ctx.send(f"Job cooldown: {user['job_cooldown']} seconds.")
        return
    user['money'] += jobs[user['job']]['salary']
    user['job_cooldown'] = jobs[user['job']]['cooldown']
    await ctx.send(f"Earned {jobs[user['job']]['salary']}.")

