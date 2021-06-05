import pyautogui
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import time
import os
class screenshot:
    def __init__(self):
        a=Tk()
        a.geometry("400x200")
        a.title("Screenshot")
        a['background']='#856ff8'
        def choose():
            dirr= filedialog.askdirectory()
            lbl_dir.config(text=dirr)
        def start():
            times=int(ent_times.get())
            sec=float(ent_sec.get())
            timer=float(ent_timer.get())
            time.sleep(timer)
            dirr=lbl_dir["text"]
            os.chdir(dirr)
            os.mkdir(f'{dirr}/screenshots')
            os.chdir(f'{dirr}/screenshots')
            ndirr=f'{dirr}/screenshots'
            if times>1:
                for i in range(times-1):
                    pyautogui.screenshot().save(f'{ndirr}/{i}.png')
                    time.sleep(sec)
            pyautogui.screenshot().save(f'{ndirr}/{times-1}.png')
        lbl_times=Label(a,text="TIMES").grid(row=0,column=0)
        ent_times=Entry(a)
        ent_times.grid(row=1,column=0)
        lbl_sec=Label(a,text="Secs in between").grid(row=2,column=0)
        ent_sec=Entry(a)
        ent_sec.grid(row=3,column=0)
        lbl_place=Label(a,text="Place").grid(row=0,column=1)
        btn_place=Button(a,text="Choose",command=choose)
        btn_place.grid(row=1,column=1)
        lbl_timer=Label(a,text="Timer").grid(row=2,column=1)
        ent_timer=Entry(a)
        ent_timer.grid(row=3,column=1)
        lbl_dir=Label(a,text='')
        lbl_dir.grid(row=4,column=0,columnspan=2)
        btn_start=Button(a,text="Start",command=start)
        btn_start.grid(row=5,column=0,columnspan=2)
        mainloop
screenshot()
