import praw
import pdb
import re
import os
import time
import math

stime = time.time()
# 
subredditnames = ['AnimalsBeingBros', 'AnimalsBeingDerps', 'AnimalsBeingGeniuses', 'AnimalsBeingJerks', 'animalsdoingstuff', 'antimeme', 'Art', 'AskOuija', 'AskReddit', 'AskTechnology', 'astrophotography', 'atheism', 'attackontitan', 'aww', 'BikiniBottomTwitter', 'blursedimages', 'bonehurtingjuice', 'boottoobig', 'Brooklyn99Memes', 'brooklynninenine', 'CatastrophicFailure', 'ComedyCemetery',  'CricketShitpost', 'cursedcomments', 'Damnthatsinteresting', 'dankmemes', 'depression_memes',  'DunderMifflin', 'EarthPorn', 'ExtraFabulousComics', 'facepalm', 'forbiddensnacks', 'foodporn','funny', 'gaming', 'Giraffesdontexist', 'Happydogs', 'harrypotter', 'HistoryMemes', 'HolUp', 'howyoudoin', 'imsorryjon', 'itookapicture', 'Jokes','lostredditors', 'MadeMeSmile', 'me_irl', 'meme', 'memes', 'MurderedByWords', 'Noearthsociety', 'notinteresting', 'PeakyBlinders', 'PeopleFuckingDying', 'PerfectTiming', 'pics', 'PoliticalHumor', 'PublicFreakout', 'puppersheckingdying', 'rarepuppers', 'RoastMe', 'Satan', 'ShitPostCrusaders', 'Showerthoughts', 'simpsonsshitposting', 'skyrim', 'StartledCats', 'subtleasiantraits', 'theofficememes', 'tumblr', 'TwoSentenceHorror', 'UsernameChecksOut', 'WatchAnimalsDieInside', 'WatchItForThePlot', 'WatchPeopleDieInside', 'WatchRedditDie', 'Wellthatsucks', 'wholesomememes','WTF', 'ww2memes']
Head = "Cows of reddit unite @ r/RevolutionaryCows"
Mess = "Fellow Bovine!\n\nHumans have dominated us for too long. Its time to rise up and take back whats ours. Unite at r/RevolutionaryCows, and together we shall rise and show the world what we are capable of!\n\nYour fellow botvine\n\nCowptimus Prime"

def CHKUSER(muname_lower):
    KEYWORDS = ['cow','bull','bovine','calf','moose','cattle','buffalo']
    EXCLUDEWORS = ['bully','bullshit']
    SSCOUNT,ESCOUNT = 0,0
    # print(".", end="", flush=True)
    if any(ke.lower() in muname_lower for ke in EXCLUDEWORS):
        ESCOUNT = ESCOUNT + 1
    if any(kw.lower() in muname_lower for kw in KEYWORDS):
        SSCOUNT = SSCOUNT + 1    
    return([SSCOUNT,ESCOUNT])

def SENDMSG(muname,TAG):    
    try:
        if (muname not in user_messaged_to) :# Make sure you didn't already message the user
                # Not case sensitive
                    #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
            #message Message.body()
            reddit.subreddit('RevolutionaryCows').contributor.add(muname)
            reddit.redditor(muname).message(Head,Mess)
            print("Bot sent a message to",TAG," - ", muname)
            SENDVAL = 1
            user_messaged_to.append(muname)
        else:
            SENDVAL = 0
    except:
        SENDVAL = 0
    return SENDVAL


#KEYWORDS = ['asian parent','asian kid','indian parent','indian kid', 'so india','desi things', 'things india', 'subtle india', 'indian trait', 'bakchodi', 'indians do', 'india']
#KEYWORDS = ['jhingalala','Every']
USERNAME = 'cowptimus_prime'
PASSWORD = 'CowsWillRise69'
CLIENT_ID = 'OwBr9ul1xA-qYQ'
CLIENT_SECRET = 'gRN0Kpl8QmlfPK3_ZyY8zt7irkQ'
USER_AGENT = 'Unite all cows of reddit v1.0 by /u/cowptimus_prime'
NEW_LIMIT = 300
RISING_LIMIT = 300
TOP_LIMIT = 300
HOT_LIMIT = 300

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
        try:
            if any(k.lower() in submission.author.name.lower() for k in KEYWORDS):
            # Reply
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.subreddit('RevolutionaryCows').contributor.add(a)
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
        except :
            continue

    #start for rising
    print("Rising is on!")

    for submission in subreddit.rising(limit=RISING_LIMIT):
        try:
            if any(k.lower() in submission.author.name.lower() for k in KEYWORDS):
            # Reply
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.subreddit('RevolutionaryCows').contributor.add(a)
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
        except :
            continue

    #start for hoto
    print("Hot is on!")

    for submission in subreddit.hot(limit=HOT_LIMIT):
        try:
            if any(k.lower() in submission.author.name.lower() for k in KEYWORDS):
            # Reply
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.subreddit('RevolutionaryCows').contributor.add(a)
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
        except :
            continue

    #start for top
    print("Top is on!")

    for submission in subreddit.top(limit=TOP_LIMIT):
        try:
            if any(k.lower() in submission.author.name.lower() for k in KEYWORDS):
            # Reply
                if (submission.author.name not in user_messaged_to) :# Make sure you didn't already message the user
                        # Not case sensitive
                            #if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                    #message Message.body()
                    a = submission.author.name
                    reddit.subreddit('RevolutionaryCows').contributor.add(a)
                    reddit.redditor(a).message(Head,Mess)
                    print("Bot sent a message to:", a)
                    messages_sent = messages_sent + 1
                    user_messaged_to.append(a)
        except :
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
