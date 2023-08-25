import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox, filedialog
import webbrowser
import pytube
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import VideoFileClip

root = tk.Tk()
root.resizable(False, False)
root.title("Youtube link to MP3 downloader")
root.config(bg="#FF8674")
width = 600
height = 370

x = int((root.winfo_screenwidth() / 2) - (width / 2))
y = int((root.winfo_screenheight() / 2) - (height / 2))

root.geometry(f'{width}x{height}+{x}+{y}')




def menu(e):
        w = e.widget
        the_menu.entryconfigure("Copy",
                                command=lambda: w.event_generate("<<Copy>>"))

        the_menu.entryconfigure("Paste",
                                command=lambda: w.event_generate("<<Paste>>"))

        the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


def panels():
    welcome = Label(root, text="Welcome to the Youtube link To MP3 Convertor <3", bg="#FF8674",font="Poppins 20 ")
    welcome.pack()
    welcome.place(x=10, y=60)

    copyright = Label(root, text="Copyright by Fernando Rodrigues - Anyone Can use it :)",bg="#FF8674", font="Arial 12")
    copyright.place(x=100,y=100)

    yt_link = Label(root, text="Enter link :",bg="#FF8674", pady=5,padx=5, font="Arial 10")
    yt_link.place(x=100,y=170)

    root.linkText = Entry(root, width=20, textvariable=link_entry, font="Arial 14")
    root.linkText.bind_class("Entry", "<Button-3><ButtonRelease-3>", menu)
    root.linkText.place(x=173, y=170)

    mp3_button = Button(root,    text="Download",command=download_mp3, bg="#FF8674",width=10, font="Arial 10", cursor="hand2")
    mp3_button.place(x=400,y=170)


    folder_label = Label(root,text="Save to:", bg="#FF8674",pady=5,padx=9,font="Arial 10")
    folder_label.place(x=100,y=200)

    root.file_browse_text = Entry(root,width=25,textvariable=download_path,font="Arial 13")
    root.file_browse_text.place(x=160,y=200)

    file_browse = Button(root,text="Browse",command=browse_file,width=10,bg="#FF8674",relief=GROOVE, cursor="hand2")
    file_browse.place(x=400,y=200)

    contact = Label(root, text="Feel Free To support me on my projects :)", bg= "#FF8674",font="Arial 12")
    contact.place(x=150, y= 300)

    github_link = Label(root, text="GitHub", font="Arial 10", fg="black", bg="#00FFFF", cursor="hand2")
    github_link.grid(row=6,column=2,)
    github_link.bind('<Button-1>', lambda x:webbrowser.open_new_tab("https://Github.com/Fernando7181"))

    linkedin_link = Label(root, text="Linkedin", font="Arial 10", fg="black", bg="#FF0000", cursor="hand2")
    linkedin_link.grid(row=6, column=4,)
    linkedin_link.bind('<Button-1>', lambda x: webbrowser.open_new_tab("https://www.linkedin.com/in/fernando-barbosa-rodrigues-8803a5245/"))


def browse_file():
    download_Directory = filedialog.askdirectory()
    download_path.set(download_Directory)

def download_mp3():
    try:
        youtube_link = link_entry.get()
        download_folder = download_path.get()
        get_item = YouTube(youtube_link)
        file_res = get_item.streams.get_lowest_resolution()
        file_Convert = file_res.download(download_folder)

        video = VideoFileClip(file_Convert)
        video.audio.write_audiofile(file_Convert[:-4] + ".mp3")
        video.close()
        os.remove(file_Convert)
        messagebox.showinfo("Your Music is Downloaded :)", f"Downloaded audio : {get_item.title}")
    except:
        messagebox.showerror("Invalid Link", "Insert the corret link.")




link_entry = StringVar()
var = IntVar()
link_entry = StringVar()
download_path = StringVar()

panels()
root.mainloop()

