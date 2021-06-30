import tkinter as tk
import tkinter.font as font
from tkinter import *
from PIL import ImageTk,Image
import os
import time
import add_user
import recognize

class gui:

    def welcomeWindow(self):
        self.window=tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = True
        self.window.title("Authenticator")
        self.frame=Frame(master=self.window,bg='white')
        self.frame.pack(fill=BOTH,expand=1)
        self.frame.pack_propagate(0)
        imgO=Image.open(os.getcwd()+"/images/splash.png")
        img= ImageTk.PhotoImage(imgO)
        self.Imagelabel=Label(self.frame,image=img,bg='white')
        self.Imagelabel.pack(side="bottom",fill="both",expand="yes")
        self.welcomeLabel=Label(self.frame,text='Authenticator',font=font.Font(family='Times New Roman', size=50, weight='bold'),bg='white',fg='#149120')
        self.welcomeLabel.pack(side=TOP)
        self.window.after(5000,lambda:self.window.destroy())
        self.window.mainloop()


    def __init__(self):
        self.window = None
        self.addUser=add_user.adduser(self)
        self.recognizeUser=recognize.recognizeuser(self)

    def initComponents(self):
        self.window=tk.Tk()
        self.window.attributes('-fullscreen',True)
        self.window.title("Authenticator")
        self.window.bind("<Escape>", self.quitFullScreen)



    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def mainWindow(self):
        self.frame=Frame(master=self.window,bg='white')
        self.frame.pack(fill=BOTH,expand=1)
        logoimg=Image.open(os.getcwd()+"/images/logo.png")
        imgLogo=ImageTk.PhotoImage(logoimg)
        self.logoimageLabel=Label(self.frame,image=imgLogo,width=50,height=50,bg="white")
        self.logoimageLabel.place(x=20,y=20)
        self.logoTitleLabel=Label(self.frame,text="Authenticator",bg='white',fg='#149120',font=font.Font(family='Times New Roman', size=25, weight='bold'))
        self.logoTitleLabel.place(x=110,y=20)

        self.reduce=100;
        self.addLabel=Label(self.frame,text="Add User",bg='white',fg='#2980B9',font=font.Font(family='Times New Roman', size=30, weight='bold'))
        self.addLabel.place(x=300-self.reduce,y=200-self.reduce)
        self.recognizeLabel=Label(self.frame,text="Authenticate User",bg='white',fg='#2980B9',font=font.Font(family='Times New Roman', size=30, weight='bold'))
        self.recognizeLabel.place(x=900-self.reduce,y=200-self.reduce)
        addimgO=Image.open(os.getcwd()+"/images/add.png")
        addimg= ImageTk.PhotoImage(addimgO)
        self.addbutton=tk.Button(self.frame,image=addimg,width=400,height=400,command=self.switchToAddUserFrame)
        self.addbutton.place(x=10+40+10+30+150+20-self.reduce,y=200+80+2-self.reduce)
        recogimgO=Image.open(os.getcwd()+"/images/recognize.png")
        recogimg= ImageTk.PhotoImage(recogimgO)
        self.recognizebutton=tk.Button(self.frame,image=recogimg,width=400,height=400,command=self.switchToRecognizeFrame)
        self.recognizebutton.place(x=10+40+10+30+150+20+600-self.reduce,y=200+80+2-self.reduce)
        self.exitbutton = tk.Button(self.frame, text='Exit',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.window.destroy)
        self.exitbutton.place(x=10+40+10+30+150+20+450-self.reduce,y=200+80+500-self.reduce)
        self.window.mainloop()

    def adduserFrame(self):
        self.userframe=Frame(master=self.window,bg='white')
        self.userframe.pack(fill=BOTH,expand=1)
        logoimg=Image.open(os.getcwd()+"/images/logo.png")
        imgLogo=ImageTk.PhotoImage(logoimg)
        self.logoimageLabel=Label(self.userframe,image=imgLogo,width=50,height=50,bg="white")
        self.logoimageLabel.place(x=20,y=20)
        self.logoTitleLabel=Label(self.userframe,text="Authenticator",bg='white',fg='#149120',font=font.Font(family='Times New Roman', size=25, weight='bold'))
        self.logoTitleLabel.place(x=110,y=20)

        self.addReduce=100
        voiceimgO=Image.open(os.getcwd()+"/images/voice.png")
        voiceimg= ImageTk.PhotoImage(voiceimgO)
        self.voiceimagelabel=Label(self.userframe,image=voiceimg,bg='white')
        self.voiceimagelabel.place(x=110-self.addReduce,y=200-self.addReduce)
        self.text=Text(self.userframe, state='normal',width=50,height=20,bg="white",fg='#21618C',font=font.Font(family='Times New Roman', size=20))
        self.text.place(x=10+40+10+30+150+20+450+50-self.addReduce,y=150-self.addReduce)
        self.text.insert(END, 'Welcome to Authenticator...........\n\n To add a new user follow the steps given below:\n\n Step1: Enter your name\n\n Step2: Add your face and\n\n Step3: Add your voice \n\n After reading all the steps click on the proceed button')
        self.text['state']="disabled"
        self.backbutton = tk.Button(self.userframe, text='Back',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.switchToMainWindow)
        self.backbutton.place(x=10+40+10+30+150+20+200-self.addReduce,y=200+80+500-self.addReduce)
        self.proceedbutton = tk.Button(self.userframe, text='Proceed',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.switchToAddFaceFrame)
        self.proceedbutton.place(x=10+40+10+30+150+20+450-self.addReduce,y=200+80+500-self.addReduce)
        self.window.mainloop()

    def addfaceframe(self):
        self.userframe=Frame(master=self.window,bg='white')
        self.userframe.pack(fill=BOTH,expand=1)
        logoimg=Image.open(os.getcwd()+"/images/logo.png")
        imgLogo=ImageTk.PhotoImage(logoimg)
        self.logoimageLabel=Label(self.userframe,image=imgLogo,width=50,height=50,bg="white")
        self.logoimageLabel.place(x=20,y=20)
        self.logoTitleLabel=Label(self.userframe,text="Authenticator",bg='white',fg='#149120',font=font.Font(family='Times New Roman', size=25, weight='bold'))
        self.logoTitleLabel.place(x=110,y=20)

        self.addfaceReduce=100
        faceimgO=Image.open(os.getcwd()+"/images/face.png")
        faceimg= ImageTk.PhotoImage(faceimgO)
        self.faceimagelabel=Label(self.userframe,image=faceimg,bg='white')
        self.faceimagelabel.place(x=110-self.addfaceReduce,y=200-self.addfaceReduce)
        self.nameLabel=Label(self.userframe,text="Enter your Name:",bg="white",fg='#21618C',font=font.Font(family='Times New Roman', size=20, weight='bold'))
        self.nameLabel.place(x=10+40+10+30+150+20+450+50,y=50)
        self.nametext=Text(self.userframe, state='normal',width=15, height=1,bg="#ffffff",fg='#21618C',font=font.Font(family='Times New Roman', size=20))
        self.nametext.place(x=10+40+10+30+150+200+300+100+150,y=50)

        self.addbutton = tk.Button(self.userframe, text='Add',font=font.Font(family='Times New Roman', size=15, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.callAddMethod)
        self.addbutton.place(x=10+40+10+30+150+200+300+100+150+250,y=50)
        self.text=Text(self.userframe, state='normal',width=50,height=20,bg="white",fg='#21618C',font=font.Font(family='Times New Roman', size=20))
        self.text.place(x=10+40+10+30+150+20+450+50-self.addfaceReduce,y=250-self.addfaceReduce)
        self.text['state']="disabled"
        self.donebutton = tk.Button(self.userframe, text='Done',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.switchToMainWindow)
        self.donebutton.place(x=10+40+10+30+150+20+350-self.addfaceReduce,y=200+80+500-self.addfaceReduce)
        self.donebutton['state']=tk.DISABLED
        self.window.mainloop()

    def callAddMethod(self):
        name=self.nametext.get("1.0",END).strip()
        if name=="":
            self.errorfield=Message(self.userframe,text="Please enter name ",width=200,bg="#ffffff",fg="red",font=font.Font(family='Times New Roman', size=15))
            self.errorfield.place(x=10+40+10+30+150+200+300+100+140,y=90)
        else :
            self.errorfield=Message(self.userframe,text="Please enter name ",width=200,bg="#ffffff",fg="white",font=font.Font(family='Times New Roman', size=15))
            self.errorfield.place(x=10+40+10+30+150+200+300+100+140,y=90)
            self.window.update()
            self.nametext['state']=tk.DISABLED
            self.addbutton['state']=tk.DISABLED
            self.addUser.add(name)
            self.donebutton['state']=tk.NORMAL
        self.window.mainloop()

    def switchToAddUserFrame(self):
        self.frame.destroy()
        self.adduserFrame()

    def switchToAddFaceFrame(self):
        self.userframe.destroy()
        self.addfaceframe()

    ##############

    def switchToMainWindow(self):
        self.userframe.destroy()
        self.mainWindow()



    def getResponse(self,response):
        self.text['state']="normal"
        self.text.insert(END,response+"\n")
        self.text['state']="disabled"
        s="Name Already Exists! Try Another Name..."
        if response==s:
            self.tryagainbutton = tk.Button(self.userframe, text='Try Again',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.switchToMainWindow)
            self.tryagainbutton.place(x=10+40+10+30+150+20+450,y=200+80+500)
            self.tryagainbutton['state']=tk.NORMAL
        self.window.update()

    ##############

    def recognizeuserFrame(self):
        self.userframe=Frame(master=self.window,bg='white')
        self.userframe.pack(fill=BOTH,expand=1)
        logoimg=Image.open(os.getcwd()+"/images/logo.png")
        imgLogo=ImageTk.PhotoImage(logoimg)
        self.logoimageLabel=Label(self.userframe,image=imgLogo,width=50,height=50,bg="white")
        self.logoimageLabel.place(x=20,y=20)
        self.logoTitleLabel=Label(self.userframe,text="Authenticator",bg='white',fg='#149120',font=font.Font(family='Times New Roman', size=25, weight='bold'))
        self.logoTitleLabel.place(x=110,y=20)
        lockimgO=Image.open(os.getcwd()+"/images/lock.png")
        lockimg= ImageTk.PhotoImage(lockimgO)
        self.lockimagelabel=Label(self.userframe,image=lockimg,bg='white')
        self.lockimagelabel.place(x=100,y=100)
        self.recognizebutton = tk.Button(self.userframe, text='Recognize',font=font.Font(family='Times New Roman', size=15, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.callRecognizeMethod)
        self.recognizebutton.place(x=10+40+10+30+150+20+450+50,y=80)
        self.recognizemessage=Message(self.userframe,text="click here to authenticate user ",width=600,bg="#ffffff",fg="#1F618D",font=font.Font(family='Times New Roman', size=15))
        self.recognizemessage.place(x=10+40+10+30+150+20+450+170,y=80)
        self.text=Text(self.userframe, state='normal',width=50,height=20,bg="white",fg='#21618C',font=font.Font(family='Times New Roman', size=20))
        self.text.place(x=10+40+10+30+150+20+450+50,y=150)
        self.text['state']="disabled"

        self.backbutton = tk.Button(self.userframe, text='Back',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.switchToMainWindow)
        self.backbutton.place(x=10+40+10+30+150+20+100,y=200+80+400)
        #self.adduserbutton = tk.Button(self.userframe, text='Add New User',font=font.Font(family='Times New Roman', size=25, weight='bold'),bg='#ffffff', fg='#E74C3C',command=self.switchToAddUserFrame)
        #self.adduserbutton.place(x=10+40+10+30+150+20+450,y=200+80+500)
        #self.adduserbutton['state']=tk.DISABLED
        self.window.mainloop()


    def switchToRecognizeFrame(self):
        self.frame.destroy()
        self.recognizeuserFrame()

    def callRecognizeMethod(self):
        self.backbutton['state']=tk.DISABLED
        self.recognizeUser.recog()
        self.backbutton['state']=tk.NORMAL


if __name__=='__main__':
    g=gui()
    g.welcomeWindow()
    g.initComponents()
    g.mainWindow()