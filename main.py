import praw
import time

reddit = praw.Reddit(client_id='*',
                      client_secret='*',
                     user_agent='*',
                    username='*',
                     password='*',)
subreddit = reddit.subreddit('HairyAssGirls').new();
def hasflair():
    while True:
        for sub in subreddit:
            if sub.link_flair_text:
                print(sub.link_flair_text)
            else:
                print("No flair")
                sub.remove() # this should delete the post
                poster = sub.author
                reddit.redditor(str(poster)).message("Your post was removed from r/HairyAssGirls", "You Didn't have a flair")
                time.sleep(30)

def postedtoday():
    postername = []
    while True:
        for sub in subreddit:
            if sub.link_flair_text == '❤️super hairy redditor❤':
                print('❤️super hairy redditor❤')

            elif sub.author in postername:
                print("they posted twice in a day")
                sub.remove
                reddit.redditor(str(poster)).message("Your post was removed from r/HairyAssGirls","You posted more than once a day, and don't have the \"❤️super hairy redditor❤\" flair")
                time.sleep(10)

            else:
                postername.append(sub.author)
                print("They have posted once")

        time.sleep(24.0 * 60.0 * 60.0)  # 24 hours in seconds
        postername = []


hasflair()
postedtoday()

