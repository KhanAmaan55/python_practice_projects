import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("testclip.mp4")
def play(speed):
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed,frame = stream.read()
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image = frame,ancho=tkinter.NW)
    canvas.create_text(134,26,fill="black",font="Times 25  bold", text = "Decision Pending")
    


def pending(decision):
    # Display decision pending
    frame= cv2.cvtColor(cv2.imread("Decision_Pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image = frame,ancho=tkinter.NW)
    # 3 sec sleep
    time.sleep(3)
    #display out/not out
    if decision =='out':
        decisionimg = 'Out.png'
    else:
        decisionimg = 'not_out.png'
    
    frame= cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image = frame,ancho=tkinter.NW)


def out():
    thread = threading.Thread(target=pending , args=("out",))
    thread.daemon=1
    thread.start()
    print("OUT")

def not_out():
    thread=threading.Thread(target=pending , args=("not out",))
    thread.daemon=1
    thread.start()
    print("NOt out")


SET_WIDTH = 650
SET_HEIGHT = 368

window= tkinter.Tk()
window.title("Third Umpire Amaan kit")
cv_img= cv2.cvtColor(cv2.imread("Owner.png"), cv2.COLOR_BGR2RGB)
canvas= tkinter.Canvas(window, width=SET_WIDTH, height= SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW, image=photo)
canvas.pack()


#Buttons
btn=tkinter.Button(window,text="<<< Previous(FAST)", width =50, command=partial(play, -25))
btn.pack()

btn=tkinter.Button(window,text="<<< Previous(SLOW)", width =50, command=partial(play, -2))
btn.pack()

btn=tkinter.Button(window,text="Next (FAST) >>>", width =50, command=partial(play, +25))
btn.pack()

btn=tkinter.Button(window,text="Next (SLOW) >>>", width =50, command=partial(play, +2))
btn.pack()

btn=tkinter.Button(window,text="GIVE OUT", width =50, command= out)
btn.pack()

btn=tkinter.Button(window,text="GIVE NOT OUT", width =50, command=not_out)
btn.pack()

window.mainloop()