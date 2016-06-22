import praw
import time

r = praw.Reddit(user_agent = "MuricaMurciaBoot v0.1")
print("Logging in...")
r.login("MuricaMurciaBot", "***********")

cache = []

words_to_match = ["MURICA"]
while True:
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit("test")
    print("Testing for questions...")
    for submission in subreddit.get_hot(limit=10):
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            comment.reply("['¡MURCIA!](http://krikienoid.github.io/flagwaver/#?src=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fe%2Fe8%2FBandera_de_Murcia2.0.png%2F640px-Bandera_de_Murcia2.0.png)")
            print("Reply succesful!")
            cache.append(comment.id)
    print("Comment loop finished, time to sleep.")