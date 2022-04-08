# Modules
import threading, requests, random, time

# Data For Fake Account And Password Generator So It Will Make The Sended Data Legit And Get Accepted Even If They Have A Filter.
MAIL_Var = ["sharon","richard","justin","ella","jungcock","hashimin","bulsheesh","scandalors","melody","acker","jhony","lexie","khalifa","stephen","dorota","georgeta","krystiana","gerbold","iona","lore","surprize","dog","admin","cat","shermin"]
MAIL1_Var = ["communication","help","gaming","assistant","trinity","sponsor","love_you","sexlife","cum","mukbangs","assistant","support","info","work","school","help","care","random","admin","moderator","adm","mod"]
MAIL2_Var = ["gmail","outlook","me","yahoo","pornhub","microsoft","youtube","pornhub","brazzers","google","hotmail","insta","facebook","msn","gore","freebrazzers"]
MAIL3_Var = ["-","_",".",""]
PASSWORD_Var = ["123456789","987654321","090807060504030201","Dragon","Cat","Dog","Fury","1111111111","Sheesh123","spam6912345","ILOVEYOU","WELOVEEARTH","08112233445","GetReadyWeAreHavingFun","ILOVEPORN691298","636564636261Memak","loveLetter","Qwerty123","qwertyuopasdfghjklzxcvbnm","GYGAUBCDUSVBXJAISHI","Hentailover69","hewdvxbsxhjksbdsbohedf","wteruyegabzkxchh","qwertyuiopasdfghjklzxcvbnm","ABCDEFGHILKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz","Yes_Daddy_Give_Me_Your_Seed","I Love You Shermin","Walang Tayo Bitch","Mamamo blue69"]

#Logo
LOGO = """\033[1;31;40m██████\033[1;32;40m╗░░\033[1;31;40m██████\033[1;32;40m╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗\033[1;34;40m██████\033[1;32;40m╗░
\033[1;31;40m██\033[1;32;40m╔══\033[1;31;40m██\033[1;32;40m╗\033[1;31;40m██\033[1;32;40m╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝\033[1;34;40m██\033[1;32;40m╔══\033[1;34;40m██\033[1;32;40m╗
\033[1;31;40m██████\033[1;32;40m╔╝╚\033[1;31;40m█████\033[1;32;40m╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░\033[1;34;40m██████\033[1;32;40m╔╝
\033[1;31;40m██\033[1;32;40m╔═══╝░░╚═══\033[1;31;40m██\033[1;32;40m╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░\033[1;34;40m██\033[1;32;40m╔══\033[1;34;40m██\033[1;32;40m╗
\033[1;31;40m██\033[1;32;40m║░░░░░\033[1;31;40m██████\033[1;32;40m╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗\033[1;34;40m██\033[1;32;40m║░░\033[1;34;40m██\033[1;32;40m║
\033[1;32;40m╚═╝░░░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝ V.2.0"""
LOGO1 = """\033[1;36;40mCreated By: \033[1;35;40mRedFurrFox On Github
\033[1;36;40mJoin Our FB Group: \033[1;35;40mhttps://www.facebook.com/groups/1778790372291663\n\n"""

# Delay
T = 0.75
T1 = 0.50

# Collection Of Data
print(LOGO)
print(LOGO1)
time.sleep(T)
print("(Please Don't Mind The Error On Import If You See It. This Script Need That Module Even It Is Deprecated)\n")
time.sleep(T)
print("""\033[1;34;40m[?] \033[1;37;40mPlease Choose Your Selection To Start:
\033[1;32;40m[01] \033[1;37;40mStart
\033[1;32;40m[02] \033[1;37;40mHelp
\033[1;32;40m[00] \033[1;37;40mExit\n""")
time.sleep(T1)
S = input("\033[1;33;40m[=] \033[1;37;40mYour Selection= ")

# If Else statement
if S == "1" or S == "01":
    URL = input("\033[1;34;40m[?] \033[1;37;40mPlease Enter The Phishing Recieving Link: \n")
    DATA = input("\033[1;34;40m[?] \033[1;37;40mPlease Enter The Username Box: \n")
    DATA1 = input("\033[1;34;40m[?] \033[1;37;40mPlease Enter The Password Box: \n")
    print("\033[1;34;40m[*] \033[1;37;40mProcessing...")
    print("\033[1;34;40m[*] \033[1;37;40mPlease Be Patient While This Script Become Fully Loaded")

    # The Processor
    def SP():
        while True:
            MG = random.choice(MAIL_Var)
            M1G = random.choice(MAIL1_Var)
            M2G = random.choice(MAIL2_Var)
            M3G = random.choice(MAIL3_Var)
            PG = random.choice(PASSWORD_Var) + random.choice(PASSWORD_Var)
            PG1 = random.choice(PASSWORD_Var)
            PG2 = random.choice(PASSWORD_Var) + random.choice(MAIL_Var) or random.choice(MAIL_Var) + random.choice(PASSWORD_Var)  # To somehow avoid reputation of data
            PG3 = PG or PG1 or PG2
            DATA3 = {
                f'{DATA}': f'{MG + M3G + M1G + "@" + M2G + ".com"}',
                f'{DATA1}': f'{PG2}'
            }
            time.sleep(5)
            Lmao = requests.post(url=URL, data=DATA).text  # Trust me dont use the "Lmao" variable... I didn't use "Lmao" variable as the data in it is kinda useless... It will make your terminal/console ugly and it will spam you with useless data. Also why did I think naming That variable as "Lmao" XD.
            print(f'\033[1;34;40m[/] \033[1;37;40mSpam Sent Successfully To This {URL} Link')
            print(f'\033[1;34;40m[*] \033[1;37;40mGenerated Data = {MG + M3G + M1G + "@" + M2G + ".com"}:{PG3}\n')
    
    # Threading so it will spam the phishing site effectively
    threads = []
    for i in range(70):
        t = threading.Thread(target=SP)
        t.daemon = True
        threads.append(t)
    for i in range(70):
        threads[i].start()
    for i in range(70):
        threads[i].join()
    
    print("\033[1;31;40m[X] \033[1;37;40mIf You Are Reading This... Either Your Link/Boxes That You Entered Are Incorrect Or Either You Are Offline Or The Site Itself.")
    print("\033[1;34;40m[-_-] \033[1;37;40mSo... Basically, The Script Just Stop Working. Because Of You... Nahhh Joke. K Bye Have A Nice Day")
    print("\033[1;34;40m[*] \033[1;33;40mExiting Script...")
    exit()

elif S == "2" or S == "02":
    print("""\033[1;35;40m
========================================================================
To Use This Tool, You Must Collect The Following:
========================================================================
    - URL Where The Data You've Entered Goes 
        Example: Use 'https://redeemcode-phillipines.games/reward.php' 
        Instead Of: 'https://redeemcode-phillipines.games.com'
    - Username Box/Request 
        Example: 'code' for username box based on my url example
    - Password Box/Request 
        Example: 'playid' for password box based on my url example
------------------------------------------------------------------------
You Can Access All Of This By Using A Built-in DevTool On Your Selected 
Browser (Works Great On PC).
------------------------------------------------------------------------

 +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +

========================================================================
Notes Before You Run This Script:
========================================================================
    - This May Cause DOS Attack On Your Target.
        So Please Only Use This On Phishing Sites NOT On Any Legit Sites
        Like Google And Facebook.
    - This Can Cause Lag On Your Device While It Is Running.
        Make Sure Your Phone Has Atleast 2GB 
        So This Script Will Not Cause Lags On Your Device
    - This Tool Can Be Tricky To Non Geek Peoples.
    - If You Have Discovered Some Bug, Please Try To Report It On Us.
    - Want To Suggest A Feature On This Script?
        Feel Free To Suggest It On My Github Repo Or Go To Our FB Group
    - I Am Not Responsible For Any Lawsuits Against Third Party Users 
      Using This Tool Too Far From What I Intended Purpose.
        As A User Of My Script, Please Please Please...
        Atleast Know Your Limit.
    - This Tool Is Created To Spam Phishing Links... 
      So Basically, I Made This To Annoy Bad Hackers :)
    - Download All Required Modules For This Script To Run
        (Like: Asyncio, Threading, Requests, Random And Time)
------------------------------------------------------------------------

 +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Still Don't Know How To Use It? 
Join Our FB Group And Ask Any Of Our Group Admins, 
They Will Assist You On How To Use This Script.)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +

========================================================================
- To My Fellow Hackers Or Who Will Try To Reverse Engineer This Script:
========================================================================
You Can Do Whatever You Want On My Code "With Or Without Credits", 
I Can Assist You If You Want. I Created This Code So People Can Modify
It Freely. Im Dead Serious... XD

Also Please Join Our Fb Group, We Want Like You Aspiring Hackers To Be 
Part Of Us. So... See You There :)
------------------------------------------------------------------------
\n""")
    print("\033[1;34;40m[*] \033[1;33;40mExiting Script...")
    exit()

elif S == "0" or S == "00":
    print("\033[1;36;40m[-] \033[1;34;40mThank You For Using My Script :)")
    print("\033[1;34;40m[*] \033[1;33;40mExiting Script...")
    exit()

else:
    print(f'\033[1;31;40m[X] \033[1;33;40m{S} \033[1;37;40mIs Not On The List, Please Try Again.')
    print("\033[1;34;40m[*] \033[1;33;40mExiting Script...")
    exit()

# If you want to copy it... please just make sure that you will make it less obvious so no one will strike your repo for copyrights what so ever, thanks :)
# Created By: RedFurrFox On Github (https://github.com/RedFurrFox)
# Join Our FB Group: https://www.facebook.com/groups/1778790372291663


# 8===================D- - __ _                                                                         (Just Random Dick Jokes.... Don't Mind This.... XD)
