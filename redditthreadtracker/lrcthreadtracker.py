import requests
import tkinter as tk 
from datetime import datetime

thread = []


#reddit api logic
subreddit = 'loopringorg'
limit = '10'
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

#add a Frame
frame = tk.Frame(canvas,bg="grey")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

#show titles'posts' on our canvas
#widget returns list of posts, need to split 'posts' value 

for widget in frame.winfo_children():
        widget.destroy()
for post in posts:
    label = tk.Label(frame, text = posts, bg ="gray")
    label.pack()

#newLrcThread(subreddit,listing,limit,timeframe)



canvas.mainloop()