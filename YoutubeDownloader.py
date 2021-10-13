from pytube import YouTube  # Install the Module pytube
from pytube import Stream
from tkinter import *  # Import TKInter for a GUI
from tkinter import ttk
from pydub import AudioSegment
import time
import os
from tkinter import filedialog

delechar = '~"#%&*:<>?/\{|}.'
picklist = ["mp3", "mp4"]

def youtubeDownload():
    print("Start Download....")
    link = (entry.get())
    output_Path = ""
    if (entry2.get()) == "":
        output_Path = os.getcwd()
    else:
        output_Path = (entry2.get())
    
    print(output_Path)

    comboElement = comboBox.get()
    yt = YouTube(link)
    print(yt.title)
    titel = (yt.title.translate({ord(i): None for i in delechar}))

    if (comboElement == "mp3"):
        yt.streams.filter(only_audio=True).order_by(
            'abr').desc().first().download(filename="Input", output_path=output_Path)
        print("Download Finished!")
        print("Start Converting....")
        song = AudioSegment.from_file(output_Path+"\Input.webm", "webm")

        song.export(output_Path+"\\"+titel+".mp3",
                    format="mp3", bitrate="192k")
        print(output_Path+titel+".mp3")
        if os.path.exists(output_Path+"\Input.webm"):
            os.unlink(output_Path+"\Input.webm")
        else:
            print("File does not exist")

        print("Finished, you can now enjoy: " +
              yt.title + " in " + output_Path)

    else:
        yt.streams.get_highest_resolution().download(output_path=output_Path)
        print("Finished you can now enjoy: "+yt.title+ " in "+output_Path)


def clear_entry(event, entry):
    entry.delete(0, END)


def getOutput():

    output = filedialog.askdirectory()
    entry2.insert(0, output)


root = Tk()
root.geometry("1000x500")
frame = Frame(root)
frame.pack()


label = Label(frame, text="Youtube Downloader by Roman Brejninger")
label.pack(pady=50)


entry = Entry(frame, width='80')
entry.insert(0, 'Your Youtube Link')
entry.pack()
#entry.pack(padx='5', pady='120')
entry.bind("<Button-1>", lambda event: clear_entry(event, entry))





comboBox = ttk.Combobox(frame, values=picklist)
comboBox.current(0)
comboBox.pack()


button = Button(frame, text="Donwnload", command=youtubeDownload)
button.pack(pady=20)


entry2 = Entry(frame, width='80')
entry2.pack(pady=20)

button_filepath = Button(frame, text="File", command=getOutput)
button_filepath.pack()

button_reset = Button(frame, text="Reset")
button_reset.bind("<Button-1>", lambda event: clear_entry(event, entry))
button_reset.pack(pady=25,side=RIGHT)




root.title("Youtube Downloader by Roman Brejninger")
root.mainloop()


# YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()
