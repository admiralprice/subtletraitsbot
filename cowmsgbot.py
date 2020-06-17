import praw
import pdb
import re
import os
import time
import math

stime = time.time()
# 'indianpeoplefacebook',
subredditnames = ['subtleasiantraits','FoodPorn','Cricket','nostalgia','Tinder','Cringetopia','Showerthoughts','Jokes','ComedyCemetry','MemeEconomy','dankmemes','terriblefacebookmemes']
Head = "Cows of reddit unite @ r/RevolutionaryCows"
Mess = "Fellow Bovine!\n\nHumans have dominated us for too long. Its time to rise up and take back whats ours. Unite, and together we shall rise and show the world what we are capable of!\n\nYour fellow botvine\n\nCowptimus Prime"


KEYWORDS = ['cow','bull']
EXCLUDEWORDS = ['moscow', 'bullet']

#KEYWORDS = ['asian parent','asian kid','indian parent','indian kid', 'so india','desi things', 'things india', 'subtle india', 'indian trait', 'bakchodi', 'indians do', 'india']
#KEYWORDS = ['jhingalala','Every']
USERNAME = 'cowptimus_prime'
PASSWORD = 'CowsWillRise69'
CLIENT_ID = 'OwBr9ul1xA-qYQ'
CLIENT_SECRET = 'gRN0Kpl8QmlfPK3_ZyY8zt7irkQ'
USER_AGENT = 'Unite all cows of reddit v1.0 by /u/cowptimus_prime'
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
