import re
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
from math import ceil
 
root = tk.Tk()
root.geometry("340x400")
root.title("Duration Calculator")
root.configure(bg="#333333")
 
settings = tk.Frame(bg="#333333")
frame = tk.Frame(bg="#333333")
 
delta=15
realTime=''
roundMinutes=''
startClicked = tk.StringVar()
startClicked.set('AM')
endClicked = tk.StringVar()
endClicked.set('AM')
 
def timeConvert(event=None):
    try:
        time1 = startEntry.get()
        time2 = endEntry.get()
        if (
            re.search('[a-zA-Z]', time1) or
            re.search('[a-zA-Z]', time2)
            ):
            raise ValueError('Incompatible time entry')
 
        #if the time entries don't have a ':' between HH and MM, insert it
        if time1.find(':') == -1: time1 = (time1[:-2] + ':' + time1[-2:])
        if time2.find(':') == -1: time2 = (time2[:-2] + ':' + time2[-2:])
        startEntry.delete(0, "end")
        startEntry.insert(0, time1)
        endEntry.delete(0, "end")
        endEntry.insert(0, time2)
   
        #append AM/PM selection
        time1 += startDrop.get()
        time2 += endDrop.get()
 
        #convert to datetime object for math
        time1 = datetime.strptime(time1, "%I:%M%p")
        time2 = datetime.strptime(time2, "%I:%M%p")
       
        delta = int(roundEntry.get())
       
        realTime = time2-time1
        realMinutes = realTime.total_seconds() / 60
       
        if realMinutes % delta != 0:
            roundMinutes = ceil(realMinutes / delta) * delta
        else:
            roundMinutes = realMinutes
        roundMinutes = timedelta(minutes=roundMinutes)
 
        totalVal.configure(text=realTime)
        roundTimeVal.configure(text=roundMinutes)
    except:
        messagebox.showerror("Error", "Must use numbers and [hh:mm] formatting for time")
 
def helpMsg():
    messagebox.showinfo("Help", """Calculate time duration and round to custom minutes as needed.
 
Round (mm): round the time spent up to the next minute specified
 
Start/End Time: time the task begins and ends; must be in hours and minutes
 
Click the "Submit" button or press Enter on your keyboard to calculate""")
 
 
def am(event=None):
    if "startDrop" in str(event.widget): startClicked.set('AM')
    if "endDrop" in str(event.widget): endClicked.set('AM')
 
def pm(event=None):
    if "startDrop" in str(event.widget): startClicked.set('PM')
    if "endDrop" in str(event.widget): endClicked.set('PM')
 
#create widgets
label = tk.Label(frame, text="Duration Calc", font=('Helvetica', 20), bg="#333333", fg='#6abf4b')
helpBtn = tk.Button(settings, text="Help", bg="#333333", fg="#cccccc", font=('Helvetica', 10), command=helpMsg)
 
roundLabel = tk.Label(frame, text="Round (mm) ", font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
roundEntry = tk.Entry(frame, font=('Helvetica', 10), width=3, borderwidth=1.5, relief=tk.FLAT)
roundEntry.insert(0, delta)
 
startLabel = tk.Label(frame, text="Start Time (hh:mm AM/PM) ", font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
startEntry = tk.Entry(frame, font=('Helvetica', 10), width=10, borderwidth=1.5, relief=tk.FLAT)
startEntry.focus_set()
startDrop = ttk.Combobox(frame, width=3, text=startClicked, name="startDrop")
startDrop['values'] = ('AM', 'PM')
startDrop['state'] = 'readonly'
startDrop.bind('a', am)
startDrop.bind('p', pm)
 
endLabel = tk.Label(frame, text="End Time (hh:mm AM/PM) ", font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
endEntry = tk.Entry(frame, font=('Helvetica', 10), width=10, borderwidth=1.5, relief=tk.FLAT)
endDrop = ttk.Combobox(frame, width=3, text=endClicked, name="endDrop")
endDrop['values'] = ('AM', 'PM')
endDrop['state'] = 'readonly'
endDrop.bind('a', am)
endDrop.bind('p', pm)
 
submitBtn = tk.Button(frame, text="Submit", bg='#6abf4b', fg='#ffffff', font=('Helvetica', 10), command=lambda: timeConvert())
root.bind('<Return>', timeConvert)
 
totalLabel = tk.Label(frame, text="Total Time Spent: ", font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
totalVal = tk.Label(frame, text=realTime, font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
roundTimeLabel = tk.Label(frame, text="Rounded Time: ", font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
roundTimeVal = tk.Label(frame, text=roundMinutes, font=('Helvetica', 10), bg="#333333", fg='#FFFFFF')
 
#place widgets
    #top bar for help button
settings.pack(fill="x")
helpBtn.pack(side='right')
 
    #main frame for widgets
frame.pack()
label.grid(column=0, row=0, columnspan=3, sticky="news", pady=10)
 
roundLabel.grid(column=0, row=1, sticky='e')
roundEntry.grid(column=1, row=1, pady=15, sticky='w')
 
startLabel.grid(column=0, row=2, sticky='e')
startEntry.grid(column=1, row=2, pady=5)
startDrop.grid(column=2, row=2, padx=5)
 
endLabel.grid(column=0, row=3, sticky='e')
endEntry.grid(column=1, row=3)
endDrop.grid(column=2, row=3, padx=5)
 
submitBtn.grid(column=0, row=5, columnspan=3, pady=30)
 
totalLabel.grid(column=0, row=6, sticky='e')
totalVal.grid(column=1, row=6, sticky='w')
roundTimeLabel.grid(column=0, row=7, sticky='e')
roundTimeVal.grid(column=1, row=7, sticky='w')
 
root.mainloop()