import praw
import pdb
import re
import os
import time
import math

stime = time.time()


# BOT FOR ADDING COMMENTS AFTER 
# Already run on  - 'memes','meme','subtleasiantraits'
USERNAME = 'justindianstuff'
PASSWORD = 'Robinishood69'
CLIENT_ID = 'VRi20mq9xuDKuQ'
CLIENT_SECRET = 'YRp4P0Ep6p0ewL1bAeZ28oC-BPk' 
USER_AGENT = 'just indian things post comment bot v1.0 by /u/justindianthings'


subreddits = ['askouija']

POSTREPLY = "Spirits, this seems like a r/subtleindiantraits moment. Guessed by a bot. Beep boop borp, I have kissed zorg.\n\n^I ^am ^just ^a ^bot, ^what ^do ^I ^know? ^If ^this ^is ^a ^mistake, ^downvote ^the ^comment ^and ^I ^will ^delete ^it. ^The ^humans ^are ^all ^busy ^coitussing, ^I ^doubt ^they'll ^bother ^with ^anything ^I ^say. ^Avadakedavra!."

KEYWORDS = ['asian parent','asian kid','indian parent','indian kid', 'so india','desi things', 'things india', 'subtle india', 'indian trait', 'bakchodi', 'indians do', 'india']

COMKEYS = ['goodbye','good','bye']

NEW_LIMIT = 1000
RISING_LIMIT = 1000
HOT_LIMIT = 1000
TOP_LIMIT = 1000
NSFW_FLAG = False
COMMENTLIM = 100
COMMENTMINSCORE = 0
# and (submission.over_18 == NSFW_FLAG) 

totalcount = 0

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


SUBREDDIT_NAME = 'AskOuija'    

# Create a list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# Or load the list of posts we have replied to
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Pull the hottest 10 entries from a subreddit of your choosing
commsadded = 0
subreddit = reddit.subreddit(SUBREDDIT_NAME)

print('new')

for submission in subreddit.new(limit=NEW_LIMIT):
    # print(submission.title)

    # Make sure you didn't already reply to this post    
    # if (submission.id not in posts_replied_to) and (submission.archived == False) and (submission.locked == False):

    if (submission.id not in posts_replied_to) and (submission.archived == False) and (submission.locked == False):
        # Not case sensitive
        # if re.search("Indian mom", submission.title, re.IGNORECASE):
        # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
        if any(k.lower() in submission.title.lower() for k in KEYWORDS):
            # Reply
            for comment in submission.comments.list():
                if any(cc.lower() in comment.body.lower() for cc in COMKEYS):
                    comment.reply(POSTREPLY)
                    print("Bot replying to : ", submission.title)
                    time.sleep(5)
                    # Store id in list
                    posts_replied_to.append(submission.id)
                    commsadded = commsadded + 1
                    totalcount = totalcount + 1


# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

print('rising')

for submission in subreddit.rising(limit=RISING_LIMIT):
    # print(submission.title)

    # Make sure you didn't already reply to this post
    if (submission.id not in posts_replied_to) and (submission.archived == False) and (submission.locked == False):
        # Not case sensitive
        # if re.search("Indian mom", submission.title, re.IGNORECASE):
        # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
        if any(k.lower() in submission.title.lower() for k in KEYWORDS):
            # Reply
            for comment in submission.comments.list():
                if any(cc.lower() in comment.body.lower() for cc in COMKEYS):
                    comment.reply(POSTREPLY)
                    print("Bot replying to : ", submission.title)
                    time.sleep(5)
                    # Store id in list
                    posts_replied_to.append(submission.id)
                    commsadded = commsadded + 1
                    totalcount = totalcount + 1

# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

print('hot')

for submission in subreddit.hot(limit=HOT_LIMIT):
    # print(submission.title)

    # Make sure you didn't already reply to this post
    if (submission.id not in posts_replied_to) and (submission.archived == False) and (submission.locked == False):
        # Not case sensitive
        # if re.search("Indian mom", submission.title, re.IGNORECASE):
        # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
        if any(k.lower() in submission.title.lower() for k in KEYWORDS):
            # Reply
            for comment in submission.comments.list():
                if any(cc.lower() in comment.body.lower() for cc in COMKEYS):
                    comment.reply(POSTREPLY)
                    print("Bot replying to : ", submission.title)
                    time.sleep(5)
                    # Store id in list
                    posts_replied_to.append(submission.id)
                    commsadded = commsadded + 1
                    totalcount = totalcount + 1

# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


print('top')

for submission in subreddit.top(limit=TOP_LIMIT):
    # print(submission.title)

    # Make sure you didn't already reply to this post
    if (submission.id not in posts_replied_to) and (submission.archived == False) and (submission.locked == False):
        # Not case sensitive
        # if re.search("Indian mom", submission.title, re.IGNORECASE):
        # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
        if any(k.lower() in submission.title.lower() for k in KEYWORDS):
            # Reply
            for comment in submission.comments.list():
                if any(cc.lower() in comment.body.lower() for cc in COMKEYS):
                    comment.reply(POSTREPLY)
                    print("Bot replying to : ", submission.title)
                    time.sleep(5)
                    # Store id in list
                    posts_replied_to.append(submission.id)
                    commsadded = commsadded + 1
                    totalcount = totalcount + 1



# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

print(' ')
print('---')
print('I added '+str(commsadded)+' comment(s).')     


# Search 200 comments for downvotes, if they have -1, delete it.
print (' ')
print ('---')
print ('Will delete comments below '+str(COMMENTMINSCORE)+' upvotes...')
comdel = 0
comments = reddit.user.me().comments.new(limit=COMMENTLIM) 
for comment in comments:
    if comment.score < COMMENTMINSCORE:
        print (str(comment.score)+' - '+comment.body)
        comdel = comdel + 1
        comment.delete()

etime = time. time()
telm = math.floor((etime - stime)/60)
tels = (etime - stime) - telm*60
print(' ')
print('---')
print('I added a total of '+str(totalcount)+' comment(s), and deleted '+str(comdel)+' comments. ')     
print(' ')
print("Time elapsed = %d"%telm + " min %0.2f" %tels+" sec")



