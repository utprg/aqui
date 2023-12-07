import discord
from discord.ext import commands
from keep_alive import keep_alive
#Discord周りの処理準備
TOKEN = 'MTE3NjQxMDk5ODMyNDg1ODkwMQ.Gclmlu.c7W6uwvO-g_E3jthfsne7aUg05wn3ZoJQik7sI'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
)

genchisignal="\N{WHITE LEFT POINTING BACKHAND INDEX}"

#サイコロが動くフィールド(狙った数値が出るように数字なり記号は変換する必要あり)
grid=[["6","%","2","x","9"],
      ["-","5","+","4","^"],
      ["8","x","1","+","7"],
      ["%","2","+","3","-"],
      ["4","-","9","^","2"]]
cp=[2,2]
currentformula=[grid[cp[0]][cp[1]]]
dice=[1,2,3,4,5,6]
currentformula.append(str(dice[0]))

#上への移動
@bot.command(name="up",description="UP")
async def u(ctx: discord.ApplicationContext):
    global grid,cp,currentformula,dice
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[0]==0:
        await ctx.respond("reset")
        cp=[2,2]
        currentformula=[grid[cp[0]][cp[1]]]
        dice=[1,2,3,4,5,6]
        currentformula.append(str(dice[0]))
    else:
        cp[0]-=1
        currentformula.append(grid[cp[0]][cp[1]])
        dice[0],dice[1],dice[5],dice[4]=dice[1],dice[5],dice[4],dice[0]
        currentformula.append(str(dice[0]))
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    f=[currentformula[0]]
    for i in range(1,len(currentformula)):
        if currentformula[i].isdigit() and f[-1].isdigit():
            f[-1]+=currentformula[i]
        else:
            f.append(currentformula[i])
    if len(f)==3:
        if f[1]=='+':
            f=[str(int(f[0])+int(f[2]))]
        elif f[1]=='-':
            f=[str(int(f[0])-int(f[2]))]
        elif f[1]=='x':
            f=[str(int(f[0])*int(f[2]))]
        elif f[1]=='%':
            f=[str(int(f[0])%int(f[2]))]
        elif f[1]=='^':
            f=[str(int(f[0])**int(f[2]))]   
    currentformula=f
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    num=int(currentformula[0])
    r=[]
    r.append(num%26)
    q=num//26
    while q!=0:
        r.append(q%26)
        q=q//26
    for i in range(len(r)-1):
        if r[i]==0:
            r[i]=26
            r[i+1]=r[i+1]-1
        if r[i]==-1:
            r[i]=25
            r[i+1]=r[i+1]-1
    if r[-1]<=0:
        del r[-1]
    r.reverse()
    letters=[chr(num+64) for num in r]
    await ctx.respond("".join(letters))

#下への移動
@bot.command(name="down",description="DOWN")
async def d(ctx: discord.ApplicationContext):
    global grid,cp,currentformula,dice
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[0]==len(grid)-1:
        await ctx.respond("reset")
        cp=[2,2]
        currentformula=[grid[cp[0]][cp[1]]]
        dice=[1,2,3,4,5,6]
        currentformula.append(str(dice[0]))
    else:
        cp[0]+=1
        currentformula.append(grid[cp[0]][cp[1]])
        dice[0],dice[1],dice[5],dice[4]=dice[4],dice[0],dice[1],dice[5]
        currentformula.append(str(dice[0]))
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    f=[currentformula[0]]
    for i in range(1,len(currentformula)):
        if currentformula[i].isdigit() and f[-1].isdigit():
            f[-1]+=currentformula[i]
        else:
            f.append(currentformula[i])
    if len(f)==3:
        if f[1]=='+':
            f=[str(int(f[0])+int(f[2]))]
        elif f[1]=='-':
            f=[str(int(f[0])-int(f[2]))]
        elif f[1]=='x':
            f=[str(int(f[0])*int(f[2]))]
        elif f[1]=='%':
            f=[str(int(f[0])%int(f[2]))]
        elif f[1]=='^':
            f=[str(int(f[0])**int(f[2]))]   
    currentformula=f
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    num=int(currentformula[0])
    r=[]
    r.append(num%26)
    q=num//26
    while q!=0:
        r.append(q%26)
        q=q//26
    for i in range(len(r)-1):
        if r[i]==0:
            r[i]=26
            r[i+1]=r[i+1]-1
        if r[i]==-1:
            r[i]=25
            r[i+1]=r[i+1]-1
    if r[-1]<=0:
        del r[-1]
    r.reverse()
    letters=[chr(num+64) for num in r]
    await ctx.respond("".join(letters))

#左への移動
@bot.command(name="left",description="LEFT")
async def l(ctx: discord.ApplicationContext):
    global grid,cp,currentformula,dice
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[1]==0:
        await ctx.respond("reset")
        cp=[2,2]
        currentformula=[grid[cp[0]][cp[1]]]
        dice=[1,2,3,4,5,6]
        currentformula.append(str(dice[0]))
    else:
        cp[1]-=1
        currentformula.append(grid[cp[0]][cp[1]])
        dice[0],dice[3],dice[5],dice[2]=dice[2],dice[0],dice[3],dice[5]
        currentformula.append(str(dice[0]))
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    f=[currentformula[0]]
    for i in range(1,len(currentformula)):
        if currentformula[i].isdigit() and f[-1].isdigit():
            f[-1]+=currentformula[i]
        else:
            f.append(currentformula[i])
    if len(f)==3:
        if f[1]=='+':
            f=[str(int(f[0])+int(f[2]))]
        elif f[1]=='-':
            f=[str(int(f[0])-int(f[2]))]
        elif f[1]=='x':
            f=[str(int(f[0])*int(f[2]))]
        elif f[1]=='%':
            f=[str(int(f[0])%int(f[2]))]
        elif f[1]=='^':
            f=[str(int(f[0])**int(f[2]))]   
    currentformula=f
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    num=int(currentformula[0])
    r=[]
    r.append(num%26)
    q=num//26
    while q!=0:
        r.append(q%26)
        q=q//26
    for i in range(len(r)-1):
        if r[i]==0:
            r[i]=26
            r[i+1]=r[i+1]-1
        if r[i]==-1:
            r[i]=25
            r[i+1]=r[i+1]-1
    if r[-1]<=0:
        del r[-1]
    r.reverse()
    letters=[chr(num+64) for num in r]
    await ctx.respond("".join(letters))

#右への移動
@bot.command(name="right",description="RIGHT")
async def r(ctx: discord.ApplicationContext):
    global grid,cp,currentformula,dice
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[1]==len(grid)-1:
        await ctx.respond("reset")
        cp=[2,2]
        currentformula=[grid[cp[0]][cp[1]]]
        dice=[1,2,3,4,5,6]
        currentformula.append(str(dice[0]))
    else:
        cp[1]+=1
        currentformula.append(grid[cp[0]][cp[1]])
        dice[0],dice[3],dice[5],dice[2]=dice[3],dice[5],dice[2],dice[0]
        currentformula.append(str(dice[0]))
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    f=[currentformula[0]]
    for i in range(1,len(currentformula)):
        if currentformula[i].isdigit() and f[-1].isdigit():
            f[-1]+=currentformula[i]
        else:
            f.append(currentformula[i])
    if len(f)==3:
        if f[1]=='+':
            f=[str(int(f[0])+int(f[2]))]
        elif f[1]=='-':
            f=[str(int(f[0])-int(f[2]))]
        elif f[1]=='x':
            f=[str(int(f[0])*int(f[2]))]
        elif f[1]=='%':
            f=[str(int(f[0])%int(f[2]))]
        elif f[1]=='^':
            f=[str(int(f[0])**int(f[2]))]   
    currentformula=f
    if mirrorserver:
        mirrorchannel=mirrorserver.get_channel(mirror_channel_id)
        if mirrorchannel:
            await mirrorchannel.send("".join(currentformula))
        else:
            print("channel not exist")
    else:
        print("server not exist")
    num=int(currentformula[0])
    r=[]
    r.append(num%26)
    q=num//26
    while q!=0:
        r.append(q%26)
        q=q//26
    for i in range(len(r)-1):
        if r[i]==0:
            r[i]=26
            r[i+1]=r[i+1]-1
        if r[i]==-1:
            r[i]=25
            r[i+1]=r[i+1]-1
    if r[-1]<=0:
        del r[-1]
    r.reverse()
    letters=[chr(num+64) for num in r]
    await ctx.respond("".join(letters))

@bot.event
async def on_message(message):
    if message.author.bot and message.content in ["OLD","KAITI","PHONE","SW"]:
        global genchisignal
        await message.add_reaction(genchisignal)

# Botの起動とDiscordサーバーへの接続
keep_alive()
bot.run(TOKEN)
