import praw
import pdb
import re
import os
import time
import math

stime = time.time()

# THIS BOT IS FOR NON INDIAN SUBS
# Already run on  - 'memes','meme','subtleasiantraits'
USERNAME = 'justindianstuff'
PASSWORD = 'Robinishood69'
CLIENT_ID = 'VRi20mq9xuDKuQ'
CLIENT_SECRET = 'YRp4P0Ep6p0ewL1bAeZ28oC-BPk' 
USER_AGENT = 'just indian things post comment bot v1.0 by /u/justindianthings'

# subredditnames = ['memes','meme','subtleasiantraits','askreddit', 'jokes', 'funny','aww','mildlyinteresting','Showerthoughts']
# Cricket returns timeout, maybe the bot has seen a lot of negative karma
COMMENTLIM = None
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


print ('Will delete comments below '+str(COMMENTMINSCORE)+' upvotes...')
comdel = 0
comments = reddit.user.me().comments.new(limit=COMMENTLIM) 
for comment in comments:
    if comment.score < COMMENTMINSCORE:
        print (str(comment.subreddit)+' - '+str(comment.submission.title))
        comdel = comdel + 1
        comment.delete()

etime = time. time()
telm = math.floor((etime - stime)/60)
tels = (etime - stime) - telm*60
print(' ')
print('---')
print('I deleted '+str(comdel)+' comments. ')     
print(' ')
print("Time elapsed = %d"%telm + " min %0.2f" %tels+" sec")



