import praw
import pdb
import re
import os
import time
import math

stime = time.time()
# 'indianpeoplefacebook',
chkrising = {'bakchodi':1,'bollywoodmemes':0,'dankindia':0,'desimemes':0,'DesiMemeTemplates':0,'india':1,'indiameme':0,'IndianDankMemes':0,'IndianFootball':0,'Indiangirlsontinder':0,'indianpeoplefacebook':1,'indianpeoplequora':1,'IndianMeyMeys':0,'indianmemecompany':0,'IIMDank':0,'IIMemology':0,'MandirGang':0,'SaimanSays':1,'unitedstatesofindia':1}
subredditnames = list(chkrising.keys())
Head = "Invitation to r/subtleindiantraits"
# Mess = "Hey, there fellow Memelord, a really quick invite to r/subtleindiantraits!\n\nWe are a simple community. We see anything Indian, we take pride and make memes. Ghalib ke sher ho, ya mummy ki chappal. Sabse pyaar hai hume. Aur yahi pyaar failane hum aapko saadar aamantrit karte hai.\n\nHelp us grow with your creativity.\n\nShukriya!\n\nYour friendly neighbourhood Indian bot.\n\n............\n\n**T R A N S L A T I O N**\n\n*roses are red*\n\n*indians are cool*\n\n*i dare ya, i double dare ya*\n\n*to find a sub this cool*\n\n...........\n\n^(The translator was fired as he got lost in translation. KBye.)"
Mess = "Hey, there fellow redditor, a really quick invite to r/subtleindiantraits!\n\nWe are a happy little community. We see anything Indian, we take pride and celebrate its essence through memes. We cordially invite you to join our sub and re-connect with your innate Indianness. \n\nHelp us grow with your creativity.\n\nShukriya!\n\nYour friendly neighbourhood Indian bot.\n\n...........\n\n^(Please dont go grammar nazi on me. I fired the translator as he got lost in translation. KBye.)"

#KEYWORDS = ['asian parent','asian kid','indian parent','indian kid', 'so india','desi things', 'things india', 'subtle india', 'indian trait', 'bakchodi', 'indians do', 'india']
#KEYWORDS = ['jhingalala','Every']
USERNAME = 'notsosubtleindianbot'
PASSWORD = 'JustMessing69'
CLIENT_ID = 'FlD33lKGw0QzJw'
CLIENT_SECRET = 'cXRAk3Y93AO0jwqol53woZa93Gk'
USER_AGENT = 'just indian things user message bot v1.1 by /u/notsosubtleindianbot'

TOP_LIMIT = 0
RISING_LIMIT = 1000
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
    #start for top posts
    if(chkrising[SUBREDDIT_NAME]):
        print("Rising is on!")
        for submission in subreddit.rising(limit = RISING_LIMIT):
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
                    continue
    #start for hot
    print("Hot is on!")

    for submission in subreddit.hot(limit = HOT_LIMIT):
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
                continue
    with open("user_messaged_to.txt",'w') as f:
        for myuser in user_messaged_to:
            f.write(myuser + "\n")

print("Total messages sent:", messages_sent)
#update the list

etime = time. time()
telm = math.floor((etime - stime)/60)
tels = (etime - stime) - telm*60
print(' ')
print('---')
print(' ')
print("Time elapsed = %d"%telm + " min %0.2f" %tels+" sec")
