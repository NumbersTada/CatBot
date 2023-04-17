from distutils.command.upload import upload
import time,requests,random,os,base64,hashlib
from itertools import cycle
from urllib3 import connection
from json import loads
from threading import Thread

substitution = {"r":"w",
"l":"w",
"R":"W",
"L":"W",
"no":"nu",
"has":"haz",
"have":"haz",
"you":"uu",
"the":"da",
"R":"W",
"The":"Da" }
#Prefixes
prefix = ["<3 ",
"H-hewwo?? ",
"HIIII! ",
"Haiiii! ",
"Huohhhh. ",
"OWO ",
"OwO ",
"UwU ",
"88w88 ",
"H-h-hi, ",]
#Suffixes
suffix = [" :3",
" UwU",
" >_>",
" ^_^",
"..",
" Huoh.",
" ^-^",
" ;_;",
" xD",
" x3",
" :D",
" :P",
" ;3",
" XDDD",
" Sigh.",
" ._.",
" >_<"
"xD xD xD",
":D :D :D",]
def owoify(owo):
    for word, initial in substitution.items():
        owo = owo.replace(word.lower(), initial)
    output = random.choice(prefix) + owo + random.choice(suffix)
    return output

def request(self, method, url, body=None, headers=None):
    if headers is None:
        headers = {}
    else:
        # Avoid modifying the headers passed into .request()
        headers = headers.copy()
    super(connection.HTTPConnection, self).request(method, url, body=body, headers=headers)
connection.HTTPConnection.request = request

def comment_chk(*,username,comment,levelid,percentage,type):
        part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
        return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def xor(data, key):
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
        return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
        return xor(base64.b64decode(data.encode()).decode(),"37526")

def getGJUsers(target):
    data={
        "secret":"Wmfd2893gb7",
        "str":target
    }
    request =  requests.post("http://www.boomlings.com/database/getGJUsers20.php",data=data,headers={"User-Agent": ""}).text.split(":")[1::2]
    username = request[0]
    uuid = request[2]
    accountid = request[10]
    return (username,accountid,uuid)

def uploadGJComment(name,passw,comment,perc,level):
        try:
                accountid = getGJUsers(name)[1]                                                                                                                        
                gjp = gjp_encrypt(passw)
                c = base64.b64encode(comment.encode()).decode()
                chk = comment_chk(username=name,comment=c,levelid=str(level),percentage=perc,type="0")
                data={
                    "secret":"Wmfd2893gb7",
                    "accountID":accountid,
                    "gjp":gjp,
                    "userName":name,
                    "comment":c,
                    "levelID":level,
                    "percent":perc,
                    "chk":chk
                }
                return requests.post("http://www.boomlings.com/database/uploadGJComment21.php",data=data,headers={"User-Agent": ""}).text
        except:
                return "problem"


print("CatBot by NumbersTada")
un = input("Enter your Geometry Dash username: ")
pw = input("Enter your Geometry Dash password: ")
lvlid = input("Enter the ID of the level where the bot will run: ")

uploadGJComment(un,pw,"CatBot is running! Use /help for usage.","0",lvlid)
def commands(level):
  url=f"http://gdbrowser.com/api/comments/{level}?count=1"
  r=loads(requests.get(url).text)[0]
  u=r['username']
  com=r['content']
  perc=random.randint(1,100)
  yesNo=['Yes', 'No']
  ships=['you hit an iceberg and die', 'you die due to food poisoning', 'you took an untrusted covid vaccine and suddenly died', 'you lived', 'you found your goofy ahh uncle and died', 'quandale dingle dipped you in hot oil and died','a furry jumped on you...... you died', 'pablo escobar shot you twenty times', '[RESPONSE NOT FOUND]', 'you woke up and it was a dream, and died', 'tweeted and got ratioed, then died', 'a phycho toddler killed you','*windows xp shutdown sound*', 'joe biden was the driver, you died', 'got banned for violating the dress code', 'got in a crowd of 4chanusers, you died', 'nikocado avocado ate you', 'ishowspeed yelled at you, you died of fear', 'got trolled, you died', 'someone posted fanart of your oc to e621', 'twitter cancelled you, suddenly died', 'the fbi made you eat pigs until you told them where the bodies were', 'you had a good time... NOT MY FAULT YOURALL DIRTY MINDED', 'got cbt, then died', 'edp445 was baking cupcakes, you drowned instead', 'twomad flopped on you saying goodnight girl', 'your mom groundedyou', '404, response not found', 'the government was eating pickles', 'you farded and died', 'got a liver transplant with a tiktoker', 'nikocado avocado inhaled you, you died','freddy fazbear belly flopped on you and died', 'got kicked in the thighs by a naruto wannabe', 'thought this was a relationship command', 'got attacked by big fat men', '/e danced', 'got hitby baller and died', 'micheal jackson beated you with a stick', 'peter griffin suffocated you by his belly', 'someone got a glock from the rari', 'suddenly ankhazone plays', 'your uncle laughs from behind you', 'got noscopedby a call of duty player', 'furries started kissing you, did you even die?', 'npesta screamed at you']
  ben=['Ben?', 'No.', 'Yes?', 'Oh-ho-ho!', 'Na-na-na-na-na.', 'Eurgh.']
  if(com.startswith("/ai")):
    c=com.split("/ai ")
    resp = requests.get("http://api.brainshop.ai/get?bid=169422&key=4GCemcdYgy50PlZ2&uid=0&msg="+c[1], headers={'Accept': 'application/json'})
    jsonResp = resp.json()
    airesp = jsonResp["cnt"]
    uploadGJComment(un,pw,f"{u}, {airesp}",perc,level)
    print(f"ai executed by {u}: {com}")
  elif(com.startswith("/uwu")):
    c=com.split("/uwu ")
    resp = requests.get("http://api.brainshop.ai/get?bid=169422&key=4GCemcdYgy50PlZ2&uid=0&msg="+c[1], headers={'Accept': 'application/json'})
    jsonResp = resp.json()
    airesp = jsonResp["cnt"]
    cc = owoify(airesp)
    uploadGJComment(un,pw,f"{u}, {cc}",perc,level)
    print(f"uwu executed by {u}: {com}")
  elif(com.startswith("/help")):
      uploadGJComment(un,pw,f"@{u}, CatBot Help (select category) /h_gd /h_core /h_fun /h_ai",perc,level)
      print(f"help executed by {u}: {com}")
  elif(com.startswith("/h_gd")):
      uploadGJComment(un,pw,f"GD Category /stats [text] /pointercrate[number]",perc,level)
      print(f"h_gd executed by {u}: {com}")
  elif(com.startswith("/h_core")):
      uploadGJComment(un,pw,f"Core Category /help /code /funfact /plans",perc,level)
      print(f"h_core executed by {u}: {com}")
  elif(com.startswith("/h_fun")):
      uploadGJComment(un,pw,f"Fun Category: /hello /talkingben /ship /cool /poggers /poll [text] /say [text] /yesOrNo",perc,level)
      print(f"h_fun executed by {u}: {com}")                                                      
  elif(com.startswith("/h_ai")):
      uploadGJComment(un,pw,f"AI Category /ai [text] /uwu [text]",perc,level)
      print(f"h_ai executed by {u}: {com}")
  elif(com.startswith("/docs")):
      uploadGJComment(un,pw,f"@{u}, Command not ready yet.",perc,level)
      print(f"docs executed by {u}: {com}")
  elif(com.startswith("CatBot")):
      uploadGJComment(un,pw,f"@{u}, that's my name! :D",perc,level)
  elif(com.startswith("@CatBot")):
      uploadGJComment(un,pw,f"@{u}, that's my name! :D",perc,level)
  elif(com.startswith("/plans")):
      planned=random.choice(plans)
      uploadGJComment(un,pw,f"@{u}, Planning on {planned}",perc,level)
      print(f"plans executed by {u}: {com}")
  elif(com.startswith("/funfact")):
      fact=random.choice(facts)
      uploadGJComment(un,pw,f"@{u}, Fun Fact: {fact}",perc,level)
      print(f"funfact executed by {u}: {com}")
  elif(com.startswith("/code")):
      uploadGJComment(un,pw,f"@{u}, sorry, no code link.",perc,level)
  elif(com.startswith("/stats")):
     c=com.split("/stats ")
     cc=c[1]
     shtats=loads(requests.get(f"http://gdbrowser.com/api/profile/{cc}").text)
     ccc=f"@{u}, {c[1]} has {shtats['stars']} Stars, {shtats['diamonds']} Diamonds, {shtats['coins']} Coins, {shtats['userCoins']} User Coins, {shtats['demons']} Demons and {shtats['cp']} Creator Points."
     uploadGJComment(un,pw,f"{ccc}",perc,level)
     print(f"stats executed by {u}: {com}")                                  
  elif(com.startswith("/pointercrate")):
     c=com.split("/pointercrate ")
     d=loads(requests.get("http://pointercrate.com/api/v2/demons/listed?limit=100").text)
     d2=loads(requests.get("http://pointercrate.com/api/v2/demons/listed?after=100").text)                                                                 
     d3=d+d2
     cc=int(c[1])-1
     ccc=f"#{d3[cc]['position']}: {d3[cc]['name']} by {d3[cc]['publisher']['name']}, verified by {d3[cc]['verifier']['name']}"
     uploadGJComment(un,pw,f"@{u} {ccc}",perc,level)
     print(f"pointercrate executed by {u}: {com}")
  elif(com.startswith("Im")):
     c=com.split("Im ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("im")):
     c=com.split("im ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("I'm")):
     c=com.split("I'm ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("i'm")):
     c=com.split("i'm ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("I am")):
     c=com.split("I am")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("i am")):
     c=com.split("i am ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("i am")):
     c=com.split("i am ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm dad!",perc,level)
  elif(com.startswith("/talkingben")):
     tb=random.choice(ben)
     uploadGJComment(un,pw,f"@{u}, {tb}",perc,level)
     print(f"talkingben executed by {u}: {com}")
  elif(com.startswith("/ship")):
     bruh = random.choice(ships)
     uploadGJComment(un,pw,f"@{u}, you got on the cruise and {bruh}",perc,level)
     print(f"ship executed by {u}: {com}")
  elif(com.startswith("/cool")):
     uploadGJComment(un,pw,f"@{u}, You are {perc}% cool!",perc,level)
     print(f"cool executed by {u}: {com}")
  elif(com.startswith("/poggers")):
     uploadGJComment(un,pw,f"@{u}, You are {perc}% poggers!",perc,level)
     print(f"poggers executed by {u}: {com}")
  elif(com.startswith("/yesOrNo")):
     yN=random.choice(yesNo)
     uploadGJComment(un,pw,f"@{u}, {yN}",perc,level)
     print(f"yesOrNo executed by {u}: {com}")
  elif(com.startswith("/say")):
     c=com.split("/say ")
     uploadGJComment(un,pw,f"@{u}, {ccom}",perc,level)
     print(f"say executed by {u}: {com}")
  elif(com.startswith("/poll")):
     c=com.split("/poll ")
     cc=c[1]
     uploadGJComment(un,pw,f"{u}'s Poll > {cc} (Vote with likes and dislikes)",perc,level)
     print(f"poll executed by {u}: {com}")
  elif(com.startswith("/hello")):
     uploadGJComment(un,pw,f"Hello {u}!",perc,level)
     print(f"hello executed by {u}: {com}")

lvl = lvlid
while 1:
    try:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(1.6)
    except:
        print("err")
