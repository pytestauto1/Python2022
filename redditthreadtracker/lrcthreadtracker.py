import requests
import tkinter as tk 
from datetime import datetime

thread = []


#reddit api logic
subreddit = 'loopringorg'
limit = '1'
timeframe = 'day'
listing = 'new'

#api query look for new thread in subreddit
def newLrcThread(subreddit,listing,limit,timeframe):
    try:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(url,headers = {'User-agent':'lrccheck'})
        #print(request.json())
    except:
        print('error')
    return request.json()

#call above method and store into object r 
r = newLrcThread(subreddit,listing,limit,timeframe)
#print(r)  


def newLrcThreadTitle(r):
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
        
    return posts

#reads r extracts title , stores , console logs 
posts = newLrcThreadTitle(r)
print(posts) # returns. 



#Canvas, GUI setup:
canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Reddit-Loopring-LRC")

# a layer to return values


#newLrcThread(subreddit,listing,limit,timeframe)



canvas.mainloop()