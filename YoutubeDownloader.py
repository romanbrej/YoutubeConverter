from pytube import YouTube #Install the Module pytube
from pytube import Stream
from tkinter import * #Import TKInter for a GUI 
from tkinter import ttk
from pydub import AudioSegment
import time
import os

delechar = '~"#%&*:<>?/\{|}.'

def youtubeDownload():
    print("Start Download....")
    link = (entry.get())
    comboElement = comboBox.get()
    yt = YouTube(link)
    print(yt.title)
    titel = (yt.title.translate({ord(i): None for i in delechar }))
    
    if (comboElement == "mp3"):
        yt.streams.filter (only_audio=True).order_by('abr').desc().first().download(filename= "Input")
        print("Download Finished!")
        print("Start Converting....")
        song = AudioSegment.from_file("Input.webm", "webm")
        song.export(titel+".mp3", format="mp3", bitrate= "192k")
        if os.path.exists("Input.webm"):
            os.remove("Input.webm")
        else:
            print("File does not exist")
        
        print("Finished, you can now enjoy: "+ yt.title)

    else:
        yt.streams.get_highest_resolution().download()
        print("Finished you can now enjoy: "+yt.title)
        


def clear_entry(event,entry):
    entry.delete(0,END)



root = Tk()
root.geometry("1000x500")
frame = Frame(root)
frame.pack()
 

label =Label(frame, text = "Youtube Downloader by Roman Brejninger")
label.pack()


entry = Entry(frame, width = '80')
entry.insert(0, 'Your Youtube Link')
entry.pack(padx = '5', pady = '120')
entry.bind("<Button-1>", lambda event: clear_entry(event, entry))



picklist = ["mp4", "mp3"]

comboBox= ttk.Combobox(frame,values = picklist)
comboBox.set("MP4 or MP3")
comboBox.pack()


button = Button(frame, text = "Donwnload", command = youtubeDownload)
button.pack()

button_reset = Button(frame, text = "Reset")
button_reset.bind("<Button-1>", lambda event: clear_entry(event, entry))
button_reset.pack()

picklist = ["mp4", "mp3"]


root.title("Youtube Downloader by Roman Brejninger")
root.mainloop()




#YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()