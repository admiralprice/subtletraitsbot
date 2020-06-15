import praw
import pdb
import re
import os
import time
import math

stime = time.time()
# 'indianpeoplefacebook',
subredditnames = ['subtleasiantraits','FoodPorn','Cricket','nostalgia','Tinder','Cringetopia','Showerthoughts','Jokes','ComedyCemetry','MemeEconomy','dankmemes','terriblefacebookmemes']
Head = "Invitation to r/subtleindiantraits"
Mess = "Hey, there fellow redditor, a really quick invite to r/subtleindiantraits!\n\nWe are a happy little community. We see anything Indian, we take pride and celebrate its essence through memes. We cordially invite you to join our sub and re-connect with your innate Indianness. \n\nHelp us grow with your creativity.\n\nShukriya!\n\nYour friendly neighbourhood Indian bot.\n\n...........\n\n^(Please dont go grammar nazi on me. I fired the translator as he got lost in translation. KBye.)"


KEYWORDS = ['indian','india']
EXCLUDEWORDS = ['indiana', 'indianapolis']

#KEYWORDS = ['asian parent','asian kid','indian parent','indian kid', 'so india','desi things', 'things india', 'subtle india', 'indian trait', 'bakchodi', 'indians do', 'india']
#KEYWORDS = ['jhingalala','Every']
USERNAME = 'justindianstuff'
PASSWORD = 'Robinishood69'
CLIENT_ID = 'VRi20mq9xuDKuQ'
CLIENT_SECRET = 'YRp4P0Ep6p0ewL1bAeZ28oC-BPk'
USER_AGENT = 'just indian things user message bot v1.0 by /u/justindianthings'
NEW_LIMIT = 1000
RISING_LIMIT = 1000
TOP_LIMIT = 1000
HOT_LIMIT = 1000

# Create the Reddit instance and log in
reddit = praw.Reddit('bot')

print("Authenticating...")
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent=USER_AGENT,
    username=USERNAME)
print("Authenticaed as {}".format(reddit.user.me()))
print("Authenticated")
#start the sub loop
subcount = 0
messages_sent = 0
for mysub in subredditnames :
    subcount = subcount + 1
    SUBREDDIT_NAME = mysub
    print(' ')
    print('---')
    print(str(subcount)+' of '+str(len(subredditnames))+' - Subreddit : '+mysub)

    # Create a list
    if not os.path.isfile("user_messaged_to.txt"):
        user_messaged_to = []

    # Or load the list of posts we have replied to
    else:
        with open("user_messaged_to.txt", "r") as f:
            user_messaged_to = f.read()
            user_messaged_to = user_messaged_to.split("\n")
            user_messaged_to = list(filter(None, user_messaged_to))


    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    #start for new posts
    print("New is on!")

    for submission in subreddit.new(limit=NEW_LIMIT):
        SENT = submission.title.lower()
        SENT = re.sub(r'[^\w\s]','',SENT)    
        WORDS = SENT.split(' ') 
        SSCOUNT = 0  
        for ke in EXCLUDEWORDS:
            if ke in WORDS:
                SSCOUNT = SSCOUNT + 1

        if any(k.lower() in submission.title.lower() for k in KEYWORDS) and SSCOUNT==0:
            # Reply
            try:
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
            except :
                    print("Something broke. Move on bruh.")
                    continue

    #start for rising
    print("Rising is on!")

    for submission in subreddit.rising(limit=RISING_LIMIT):
        SENT = submission.title.lower()
        SENT = re.sub(r'[^\w\s]','',SENT)    
        WORDS = SENT.split(' ') 
        SSCOUNT = 0  
        for ke in EXCLUDEWORDS:
            if ke in WORDS:
                SSCOUNT = SSCOUNT + 1

        if any(k.lower() in submission.title.lower() for k in KEYWORDS) and SSCOUNT==0:
            # Reply
            try:
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
            except :
                    print("Something broke. Move on bruh.")
                    continue

    #start for hoto
    print("Hot is on!")

    for submission in subreddit.hot(limit=HOT_LIMIT):
        SENT = submission.title.lower()
        SENT = re.sub(r'[^\w\s]','',SENT)    
        WORDS = SENT.split(' ') 
        SSCOUNT = 0  
        for ke in EXCLUDEWORDS:
            if ke in WORDS:
                SSCOUNT = SSCOUNT + 1

        if any(k.lower() in submission.title.lower() for k in KEYWORDS) and SSCOUNT==0:
            # Reply
            try:
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
            except :
                    print("Something broke. Move on bruh.")
                    continue

    #start for top
    print("Top is on!")

    for submission in subreddit.top(limit=TOP_LIMIT):
        SENT = submission.title.lower()
        SENT = re.sub(r'[^\w\s]','',SENT)    
        WORDS = SENT.split(' ') 
        SSCOUNT = 0  
        for ke in EXCLUDEWORDS:
            if ke in WORDS:
                SSCOUNT = SSCOUNT + 1

        if any(k.lower() in submission.title.lower() for k in KEYWORDS) and SSCOUNT==0:
            # Reply
            try:
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
            except :
                    print("Something broke. Move on bruh.")
                    continue


    with open("user_messaged_to.txt",'w') as f:
        for post_id in user_messaged_to:
            f.write(post_id + "\n")

print("Total messages sent:", messages_sent)
#update the list

etime = time. time()
telm = math.floor((etime - stime)/60)
tels = (etime - stime) - telm*60
print(' ')
print('---')
print(' ')
print("Time elapsed = %d"%telm + " min %0.2f" %tels+" sec")
