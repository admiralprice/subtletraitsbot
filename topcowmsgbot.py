import praw
import pdb
import re
import os
import time
import math

stime = time.time()

## FUNCTIONS

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

##############

def SUBMISSIONS(msubmission):
    NOSENTMSG = 0
    if (submission.archived == False) and (submission.locked == False):
        try:
            for comment in submission.comments.list():
                NOSENTMSG = 0
                try:
                    trialvar = comment.author.name 
                    DOALLOW, DOEXCLUDE = CHKUSER(comment.author.name.lower())
                    if(DOALLOW > 1) and (DOEXCLUDE == 0):
                        NOSENTMSG = NOSENTMSG + SENDMSG(comment.author.name,'Comment Author')
                except:
                    continue
        except:
            print("\nBroke something, sorry!\n")
    return NOSENTMSG

# ----------------------------------------------------------------------------------------------- #

USERNAME = 'cowptimus_prime'
PASSWORD = 'CowsWillRise69'
CLIENT_ID = 'OwBr9ul1xA-qYQ'
CLIENT_SECRET = 'gRN0Kpl8QmlfPK3_ZyY8zt7irkQ'
USER_AGENT = 'Unite all cows of reddit v1.0 by /u/cowptimus_prime'

NEW_LIMIT, RISING_LIMIT, HOT_LIMIT, TOP_LIMIT = 1000,1000,1000,1
# and (submission.over_18 == NSFW_FLAG) 
Head = "Cows of reddit unite @ r/RevolutionaryCows"
Mess = "Fellow Bovine!\n\nHumans have dominated us for too long. Its time to rise up and take back whats ours. Unite at r/RevolutionaryCows, and together we shall rise and show the world what we are capable of!\n\nYour fellow botvine\n\nCowptimus Prime"
totalcount, commsadded = 0,  0

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

# ----------------------------------------------------------------------------------------------- #

if not os.path.isfile("user_messaged_to.txt"):
    user_messaged_to = []

# Or load the list of posts we have replied to
else:
    with open("user_messaged_to.txt", "r") as f:
        user_messaged_to = f.read()
        user_messaged_to = user_messaged_to.split("\n")
        user_messaged_to = list(filter(None, user_messaged_to))

SUBREDDIT_NAME = 'all'  
MSG_SENT = 0
subreddit = reddit.subreddit(SUBREDDIT_NAME)

# ----------------------------------------------------------------------------------------------- #

postcount = 0
print('\n\nnew')
for submission in subreddit.new(limit=NEW_LIMIT):
    # print(submission.title)
    postcount = postcount + 1
    if(postcount%100 == 0):
        print(postcount)
    try:
        trialvar = submission.author.name
        DOALLOW, DOEXCLUDE = CHKUSER(submission.author.name.lower())
        if(DOALLOW > 0) and (DOEXCLUDE == 0):   
            MSG_SENT = MSG_SENT + SENDMSG(submission.author.name,'Post Author')
        MSG_SENT = MSG_SENT + SUBMISSIONS(submission)
    except:
        continue

postcount = 0
print('\n\nrising')
for submission in subreddit.rising(limit=RISING_LIMIT):
    # print(submission.title)
    postcount = postcount + 1
    if(postcount%100 == 0):
        print(postcount)
    try:
        trialvar = submission.author.name
        DOALLOW, DOEXCLUDE = CHKUSER(submission.author.name.lower())
        if(DOALLOW > 0) and (DOEXCLUDE == 0):   
            MSG_SENT = MSG_SENT + SENDMSG(submission.author.name,'Post Author')
        MSG_SENT = MSG_SENT + SUBMISSIONS(submission)
    except:
        continue


postcount = 0
print('\n\nhot')
for submission in subreddit.hot(limit=HOT_LIMIT):
    # print(submission.title)
    postcount = postcount + 1
    if(postcount%100 == 0):
        print(postcount)
    try:
        trialvar = submission.author.name
        DOALLOW, DOEXCLUDE = CHKUSER(submission.author.name.lower())
        if(DOALLOW > 0) and (DOEXCLUDE == 0):   
            MSG_SENT = MSG_SENT + SENDMSG(submission.author.name,'Post Author')
        MSG_SENT = MSG_SENT + SUBMISSIONS(submission)
    except:
        continue


postcount = 0
print('\n\ntop')
for submission in subreddit.top(limit=TOP_LIMIT):
    # print(submission.title)
    postcount = postcount + 1
    if(postcount%100 == 0):
        print(postcount)
    try:
        trialvar = submission.author.name
        DOALLOW, DOEXCLUDE = CHKUSER(submission.author.name.lower())
        if(DOALLOW > 0) and (DOEXCLUDE == 0):   
            MSG_SENT = MSG_SENT + SENDMSG(submission.author.name,'Post Author')
        MSG_SENT = MSG_SENT + SUBMISSIONS(submission)
    except:
        continue

with open("user_messaged_to.txt",'w') as f:
    for myuser in user_messaged_to:
        f.write(myuser + "\n")

print(' ')
print('---')
print('I sent '+str(MSG_SENT)+' message(s).')     


etime = time. time()
telm = math.floor((etime - stime)/60)
tels = (etime - stime) - telm*60
print(' ')
print('---')
# print('I added a total of '+str(totalcount)+' comment(s), and deleted '+str(comdel)+' comments. ')     
print(' ')
print("Time elapsed = %d"%telm + " min %0.2f" %tels+" sec")



