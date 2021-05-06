from tkinter import *
from pytube import YouTube

root = Tk()
root.title("Youtube Downloader")

url = Entry(root, text="Enter the url here!",borderwidth=5)
url.grid(row=0,column=0,columnspan=15,padx=10, pady=10)


btn_dwd = Button(root, text="Download",command=lambda: download(url.get())).grid(row=1,column=0,padx=10,pady=10)

def download(url):
    yt = YouTube(url)
    global ytLabel
    ytLabel.forget()
    ytLabel = Label(root, text=yt.title)
    ytLabel.grid(row=3,column=0)
    
    global choice

    if choice.get() == 1:
        yt.streams.filter(only_audio=True).first().download()
    else:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



choice = IntVar()

Radiobutton(root, text="Audio Only", variable=choice, value=1).grid(row=2,column=0)
Radiobutton(root, text="Audio + Video", variable=choice, value=2).grid(row=2,column=1)

ytLabel = Label(root, text="Enter a url to fetch the title")
ytLabel.grid(row=3,column=0)

root.mainloop()