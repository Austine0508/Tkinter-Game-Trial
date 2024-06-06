import tkinter as tk
import time

List=[]
point=0

def jump(event):
    global canvas
    global List
    global ball
    for x in range(200):
        canvas.move(ball,0,-1)
        win.update()
        canvas.move(List[-1],-0.5,0)
        win.update()
        time.sleep(0.001)
    #time.sleep(0.1)
    for x in range(200):
        canvas.move(ball,0,1)
        win.update()
        canvas.move(List[-1],-0.5,0)
        win.update()
        time.sleep(0.001)

def blocks(List,canvas):
    global point
    global win
    block=canvas.create_rectangle(750,350,800,450,fill='black')
    List.append(block)
    lock=0
    while True:
        canvas.move(block,-5,0)
        q,w,e,r=canvas.coords(ball)
        tup=canvas.find_overlapping(q,w,e,r)
        if len(tup)>2:
            win.destroy()
            WIN=tk.Tk()
            lbl=tk.Label(master=WIN,text="GAME OVER!!!",font=('Calibri',200))
            lbl.pack()
            
        win.update()
        time.sleep(0.025)
        lst=canvas.coords(block)
        if lst[2]<=0 and lst[3]==450:
            break
        
        else:
            if lst[2]<50:
                if lock==0:
                    point+=10
                    print(point)
                    lock=1

win=tk.Tk()
canvas=tk.Canvas(win,width=800,height=600,bg='sky blue')
ground=canvas.create_rectangle(0,450,800,600,fill='brown')
ball=canvas.create_oval(50,375,125,450,fill='red')
lbl=tk.Label(master=canvas,text="Points:"+str(point),width=10,height=2)
win.bind('<Up>',jump)

canvas.pack()
lbl.place(x=400,y=10)
while True:
    blocks(List,canvas)
    lbl['text']="Points:"+str(point)
