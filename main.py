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
mode=0
grids=[[["9","-","1","%","7"],
      ["+","4","%","6","^"],
      ["2","%","1","-","8"],
      ["x","5","x","3","+"],
      ["3","^","8","-","1"]],

      [["5","x","3","^","4"],
      ["-","7","+","1","x"],
      ["5","%","2","-","8"],
      ["x","9","+","6","%"],
      ["2","^","4","x","3"]],

      [["7","x","4","+","2"],
      ["-","1","^","3","x"],
      ["5","%","1","%","7"],
      ["x","2","^","6","+"],
      ["8","+","9","-","3"]],
      
      [["1","+","6","-","4"],
      ["x","1","%","9","^"],
      ["7","-","8","x","7"],
      ["^","1","%","5","+"],
      ["3","%","2","x","2"]],
      
      [["8","+","6","%","9"],
      ["^","3","x","4","-"],
      ["6","-","1","^","7"],
      ["%","3","%","1","%"],
      ["2","+","5","x","8"]],
      
      [["3","x","8","+","4"],
      ["%","8","-","2","+"],
      ["6","+","1","^","9"],
      ["x","3","-","6","x"],
      ["7","^","5","%","2"]]]
grid=grids[mode%6]
sps=[(2,2)]*6
dices=[(2,6,3,4,1,5),
       (5,3,6,1,4,2),
       (2,6,3,4,1,5),
       (6,5,3,4,2,1),
       (2,4,6,1,3,5),
       (4,1,5,2,6,3)]
cp=list(sps[mode%6])
currentformula=[grid[cp[0]][cp[1]]]
dice=list(dices[mode%6])
currentformula.append(str(dice[0]))

#上への移動
@bot.command(name="up",description="UP")
async def u(ctx: discord.ApplicationContext):
    global grid,cp,sps,currentformula,dice,dices,mode
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[0]==0:
        await ctx.respond("reset")
        cp=list(sps[mode%6])
        currentformula=[grid[cp[0]][cp[1]]]
        dice=list(dices[mode%6])
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
    if num==0:
        await ctx.respond("Null")
    else:
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
    global grid,cp,sps,currentformula,dice,dices,mode
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[0]==len(grid)-1:
        await ctx.respond("reset")
        cp=list(sps[mode%6])
        currentformula=[grid[cp[0]][cp[1]]]
        dice=list(dices[mode%6])
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
    if num==0:
        await ctx.respond("Null")
    else:
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
    global grid,cp,sps,currentformula,dice,dices,mode
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[1]==0:
        await ctx.respond("reset")
        cp=list(sps[mode%6])
        currentformula=[grid[cp[0]][cp[1]]]
        dice=list(dices[mode%6])
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
    if num==0:
        await ctx.respond("Null")
    else:
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
    global grid,cp,sps,currentformula,dice,dices,mode
    mirror_server_id=1178925484457861150
    mirror_channel_id=1178925484457861153
    mirrorserver=bot.get_guild(mirror_server_id)
    if cp[1]==len(grid)-1:
        await ctx.respond("reset")
        cp=list(sps[mode%6])
        currentformula=[grid[cp[0]][cp[1]]]
        dice=list(dices[mode%6])
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
    if num==0:
        await ctx.respond("Null")
    else:
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
    global mode,cp,dice,currentformula
    answers=["ATGT","PIZZA","PUSAN","SEBAN","WINTER","RITOU"]
    hints=["TAKARA","NATIONAL","PHONE","SOUTHWEST","MATUMOTO","KAICHI"]
    if message.author.bot and message.content==answers[mode%6]:
        global genchisignal
        await message.add_reaction(genchisignal)
        mode+=1
        grid=grids[mode%6]
        cp=list(sps[mode%6])
        dice=list(dices[mode%6])
        currentformula=[grid[cp[0]][cp[1]]]
        currentformula.append(str(dice[0]))
        await message.reply("正解！ 現地ヒントを開示します")
        await message.reply(hints[mode%6])

# Botの起動とDiscordサーバーへの接続
keep_alive()
bot.run(TOKEN)
