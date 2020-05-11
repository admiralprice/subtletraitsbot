import praw
import pdb
import re
import os

# THIS BOT IS FOR NON INDIAN SUBS
# Already run on  - 'memes','meme','subtleasiantraits'
subredditnames = ['askreddit', 'jokes', 'funny']
for mysub in subredditnames:    
    print(' ')
    print('---')
    print('Subreddit : '+mysub)        

    SUBREDDIT_NAME = mysub
    KEYWORDS = ['asian parent','asian kid','indian parent','indian kid', 'so india','desi things', 'things india', 'subtle india', 'indian trait', 'bakchodi', 'indians do', 'india']
    USERNAME = 'justindianstuff'
    PASSWORD = 'Robinishood69'
    CLIENT_ID = 'VRi20mq9xuDKuQ'
    CLIENT_SECRET = 'YRp4P0Ep6p0ewL1bAeZ28oC-BPk' 
    USER_AGENT = 'just indian things post comment bot v1.0 by /u/justindianthings'

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

    for submission in subreddit.new(limit=1000):
        # print(submission.title)

        # Make sure you didn't already reply to this post
        if (submission.id not in posts_replied_to) and (submission.over_18 == False) and (submission.archived == False):

            # Not case sensitive
            # if re.search("Indian mom", submission.title, re.IGNORECASE):
            # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
            if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                # Reply
                submission.reply("This seems like a r/subtleindiantraits moment. Sent by a bot. Beep boop borp, I have kissed zorg.")
                print("Bot replying to : ", submission.title)

                # Store id in list
                posts_replied_to.append(submission.id)
                commsadded = commsadded + 1


    # Write updated list to file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

    print('rising')

    for submission in subreddit.rising(limit=1000):
        # print(submission.title)

        # Make sure you didn't already reply to this post
        if (submission.id not in posts_replied_to) and (submission.over_18 == False) and (submission.archived == False):

            # Not case sensitive
            # if re.search("Indian mom", submission.title, re.IGNORECASE):
            # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
            if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                # Reply
                submission.reply("This seems like a r/subtleindiantraits moment. Sent by a bot. Beep boop borp, I have kissed zorg.")
                print("Bot replying to : ", submission.title)

                # Store id in list
                posts_replied_to.append(submission.id)
                commsadded = commsadded + 1

    # Write updated list to file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

    print('hot')

    for submission in subreddit.hot(limit=1000):
        # print(submission.title)

        # Make sure you didn't already reply to this post
        if (submission.id not in posts_replied_to) and (submission.over_18 == False) and (submission.archived == False):

            # Not case sensitive
            # if re.search("Indian mom", submission.title, re.IGNORECASE):
            # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
            if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                # Reply
                submission.reply("This seems like a r/subtleindiantraits moment. Sent by a bot. Beep boop borp, I have kissed zorg.")
                print("Bot replying to : ", submission.title)

                # Store id in list
                posts_replied_to.append(submission.id)
                commsadded = commsadded + 1

    # Write updated list to file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


    print('top')

    for submission in subreddit.top(limit=1000):
        # print(submission.title)

        # Make sure you didn't already reply to this post
        if (submission.id not in posts_replied_to) and (submission.over_18 == False) and (submission.archived == False):

            # Not case sensitive
            # if re.search("Indian mom", submission.title, re.IGNORECASE):
            # if has_keyword = any(k.lower() in post.title.lower() for k in KEYWORDS):
            if any(k.lower() in submission.title.lower() for k in KEYWORDS):
                # Reply
                submission.reply("This seems like a r/subtleindiantraits moment. Sent by a bot. Beep boop borp, I have kissed zorg.")
                print("Bot replying to : ", submission.title)

                # Store id in list
                posts_replied_to.append(submission.id)
                commsadded = commsadded + 1



    # Write updated list to file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

    print(' ')
    print('---')
    print('I added '+str(commsadded)+' comment(s).')        
