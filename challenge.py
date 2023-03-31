import random
import tkinter
global play ,point
def win_lost():
    for i in range(4):
        for j in range(4):
            if play[i][j]==2048:
                return 'win'
            elif play[i][j]==0:
                return 'continued'
    for i in range(3):
        for j in range(3):
            if play[i][j]==play[i + 1][j] or play[i][j]==play[i][j + 1]:
                return 'continued'
    for j in range(3):
        if(play[3][j]== play[3][j + 1]):
            return 'continued'

    for i in range(3):
        if(play[i][3]== play[i + 1][3]):
            return 'continued'

    return 'lost'





def randadd():
    global play
    state=win_lost()
    if state=='continued':
        a=random.randint(0,3)
        b=random.randint(0,3)

        while play[a][b] !=0:
            a=random.randint(0,3)
            b=random.randint(0,3)
        play[a][b]=2
        reset()
        return play
    elif state=='win':
        root1=tkinter.Toplevel(root)
        frame1 = tkinter.Frame(root1,borderwidth=10)
        frame1.grid(row=0,column=0)
        win_label=tkinter.Label(frame1, text='You Win!!!',justify=tkinter.LEFT,font=('Consolas',20),width=15)
        win_label.grid(row=0,column=0,sticky=tkinter.W)
        win_but=tkinter.Button(frame1,text='OK',font=('Consolas',20),command=root1.destroy)
        win_but.grid(row=1,column=0)
        play=[]
        for i in range(4):
            play.append([0]*4)
        reset()
        point_label=tkinter.Label(frame, text='Point= 0',justify=tkinter.LEFT,font=('Consolas',20),width=15)
        point_label.grid(row=4,column=1,sticky=tkinter.W)

    elif state=='lost':
        root1=tkinter.Toplevel(root)
        frame1 = tkinter.Frame(root1,borderwidth=10)
        frame1.grid(row=0,column=0)
        win_label=tkinter.Label(frame1, text='You Lost!!! QQ',justify=tkinter.LEFT,font=('Consolas',20),width=15)
        win_label.grid(row=0,column=0,sticky=tkinter.W)
        win_but=tkinter.Button(frame1,text='OK',font=('Consolas',20),command=root1.destroy)
        win_but.grid(row=1,column=0)
        play=[]
        for i in range(4):
            play.append([0]*4)
        reset()
        point_label=tkinter.Label(frame, text='Point= 0',justify=tkinter.LEFT,font=('Consolas',20),width=15)
        point_label.grid(row=4,column=1,sticky=tkinter.W)


def up():
    point=0
    c=0
    while c<3:
        for j in range(4):
            for i in [0,1,2]:
                if play[i][j]==play[i+1][j] and play[i][j]!=0:
                    play[i][j]=play[i][j]+play[i+1][j]
                    play[i+1][j]=0
                    point=point+play[i][j]
                elif play[i][j]!=play[i+1][j] and play[i][j] == 0:
                    play[i][j]=play[i+1][j]
                    play[i+1][j] =0
            
                elif play[i][j]!=0 and play[i+1][j]==0:
                    play[i][j]=play[i][j]
                    play[i+1][j] =0
        c=c+1

    point_label=tkinter.Label(frame, text='Point=',justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    point_label=tkinter.Label(frame, text='Point='+str(point),justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    randadd()
    return play


def down():
    point=0
    c=0
    while c<3:
        for j in range(4):
            for i in [3,2,1]:
                if play[i][j]==play[i-1][j] and play[i][j]!=0:
                    play[i][j]=play[i][j]+play[i-1][j]
                    play[i-1][j]=0
                    point=point+play[i][j]
                elif play[i][j]!=play[i-1][j] and play[i][j] == 0:
                    play[i][j]=play[i-1][j]
                    play[i-1][j] =0

                elif play[i][j]!=0 and play[i-1][j]==0:
                    play[i][j]=play[i][j]
                    play[i-1][j] =0
        c=c+1
    point_label=tkinter.Label(frame, text='Point=',justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    point_label=tkinter.Label(frame, text='Point='+str(point),justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    randadd()
    return play

def left():
    point=0
    c=0
    while c<3:
        for i in range(4):
            for j in [0,1,2]:
                if play[i][j]==play[i][j+1] and play[i][j]!=0:
                    play[i][j]=play[i][j]+play[i][j+1]
                    play[i][j+1]=0
                    point=point+play[i][j]
                elif play[i][j]!=play[i][j+1] and play[i][j] == 0:
                    play[i][j]=play[i][j+1]
                    play[i][j+1] =0

                elif play[i][j]!=0 and play[i][j+1]==0:
                    play[i][j]=play[i][j]
                    play[i][j+1] =0

        c=c+1
    point_label=tkinter.Label(frame, text='Point=',justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    point_label=tkinter.Label(frame, text='Point='+str(point),justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    randadd()
    return play

def right():
    point=0
    c=0
    while c<3:
        for i in range(4):
            for j in [3,2,1]:
                if play[i][j]==play[i][j-1] and play[i][j]!=0:
                    play[i][j]=play[i][j]+play[i][j-1]
                    play[i][j-1]=0
                    point=point+play[i][j]
                elif play[i][j]!=play[i][j-1] and play[i][j] == 0:
                    play[i][j]=play[i][j-1]
                    play[i][j-1] =0

                elif play[i][j]!=0 and play[i][j-1]==0:
                    play[i][j]=play[i][j]
                    play[i][j-1] =0


        c=c+1
    point_label=tkinter.Label(frame, text='Point=',justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    point_label=tkinter.Label(frame, text='Point='+str(point),justify=tkinter.LEFT,font=('Consolas',20),width=15)
    point_label.grid(row=4,column=1,sticky=tkinter.W)
    randadd()
    return play

def reset():
    records_box.delete(0,tkinter.END)
    for i,v in enumerate(play):
        records_box.insert(i,'{:>2} {:>2} {:>2} {:>2}'.format(v[0],v[1],v[2],v[3]))

#def judge():


point=0
play=[]
for i in range(4):
    play.append([0]*4)

root= tkinter.Tk()
frame = tkinter.Frame(root,borderwidth=10)
frame.grid(row=0,column=0)

point_label=tkinter.Label(frame, text='Point='+str(point),justify=tkinter.LEFT,font=('Consolas',20),width=15)
point_label.grid(row=4,column=1,sticky=tkinter.W)
up_but=tkinter.Button(frame,text='Up',font=('Consolas',20),command=up)
up_but.grid(row=0,column=3)
down_but=tkinter.Button(frame,text='Down',font=('Consolas',20),command=down)
down_but.grid(row=2,column=3)
right_but=tkinter.Button(frame,text='Right',font=('Consolas',20),command=right)
right_but.grid(row=1,column=4)
left_but=tkinter.Button(frame,text='Left',font=('Consolas',20),command=left)
left_but.grid(row=1,column=2)
start_but=tkinter.Button(frame,text='Start',font=('Consolas',20),command=randadd)
start_but.grid(row=4,column=4,sticky=tkinter.E)



records_box=tkinter.Listbox(frame,font=('Consolas',50),width=15,height=4)
records_box.grid(row=0,column=0,rowspan=5,sticky=tkinter.W)

for i,v in enumerate(play):
    records_box.insert(i,'{:>2} {:>2} {:>2} {:>2}'.format(v[0],v[1],v[2],v[3]))

root.mainloop()



#while True:
#    randadd(play)
#    z=input('command(up-> u /doen-> d/left-> l/right-> r):')
#    point=0
#    for i in play:
#        point=point+sum(i)
#    if z=='u':
#        up(play)
#    elif z=='d':
#        down(play)
#    elif z=='l':
#        left(play)
#    elif z=='r':
#        right(play)
#    state=win_lost(play)
#    if state=='lost':
#        for i in play:
#            print(i)
#        print('lost')
#        break
#
#    elif state=='continued':
#        print(f'continued , point={point}')
#    elif state=='win':
#        print('win')
#    else:




