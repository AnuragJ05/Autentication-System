import pyaudio
import wave
import cv2
import os
import pickle
import time
from scipy.io.wavfile import read
from IPython.display import Audio, display, clear_output
import gui

from main_functions import *

class adduser():
 
 def __init__(self,plObject):
   self.responseObject=plObject  

 def sendResponse(self,response):
   self.responseObject.getResponse(response)
 
 def add(self,usrname):
    self.name=usrname.strip()
     # check for existing database
    if os.path.exists('./face_database/embeddings.pickle'):
        with open('./face_database/embeddings.pickle', 'rb') as database:
            self.db = pickle.load(database)   
            
            if self.name in self.db or self.name == 'unknown':
                self.sendResponse("Name Already Exists! Try Another Name...")
                return
    else:
        #if database not exists than creating new database
        self.db = {}
    
    self.cap = cv2.VideoCapture(0)
    self.cap.set(3, 640)
    self.cap.set(4, 480)
    
    #detecting only frontal face using haarcascade
    self.face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    
    i = 3
    self.face_found = False
    
    while True:            
        _, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1, 0)
            
        #time.sleep(1.0)
        cv2.putText(self.frame, 'Keep Your Face infront of Camera', (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (255, 255, 255), 2)
        
        cv2.putText(self.frame, 'Starting', (260, 270), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (255, 255, 255), 2)
        
        cv2.putText(self.frame, str(i), (290, 330), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.3, (255, 255, 255), 3)

        i-=1
                   
        cv2.imshow('frame',self.frame)
        cv2.waitKey(1000)
        
        if i < 0:
            break
            
    self.start_time = time.time()        
    self.img_path = './saved_image/1.jpg'

    ## Face recognition 
    while True:
        self.curr_time = time.time()
        
        _, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1, 0)
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        
        face = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(face) == 1:
            for(x, y, w, h) in face:
                roi = self.frame[y-10:y+h+10, x-10:x+w+10]

                fh, fw = roi.shape[:2]

                #make sure the face roi is of required height and width
                if fh < 20 and fw < 20:
                    continue

                face_found = True
                #cv2.imwrite(img_path, roi)

                cv2.rectangle(self.frame, (x-10,y-10), (x+w+10, y+h+10), (255, 200, 200), 2)

         
        if self.curr_time - self.start_time >= 3:
            break
            
        cv2.imshow('frame', self.frame)
        cv2.waitKey(1)
            
    self.cap.release()        
    cv2.destroyAllWindows()

    
    if face_found:
        img = cv2.resize(roi, (96, 96))

        self.db[self.name] = img_to_encoding(img)

        with open('./face_database/embeddings.pickle', "wb") as database:
            pickle.dump(self.db, database, protocol=pickle.HIGHEST_PROTOCOL)
    
    elif len(face) > 1:
        self.sendResponse("More than one faces found. Try again...")
        return
    
    else:
        self.sendResponse('There was no face found in the frame. Try again...')
        return
      
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    #Voice authentication
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3
    
    source = "./voice_database/" +self.name
    
   
    os.mkdir(source)

    for i in range(3):
        audio = pyaudio.PyAudio()

        if i == 0:
            j = 3
            while j>=0:
                time.sleep(1.0)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.sendResponse("Speak your name in {} seconds".format(j))
                j-=1

        elif i ==1:
            time.sleep(2.0)
            self.sendResponse("Speak your name one more time")
            time.sleep(0.8)
        
        else:
            time.sleep(2.0)
            self.sendResponse("Speak your name one last time")
            time.sleep(0.8)

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

        self.sendResponse("recording...")
        frames = []

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        # saving wav file of speaker
        waveFile = wave.open(source + '/' + str((i+1)) + '.wav', 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        self.sendResponse("Done")

    dest =  "./gmm_models/"
    count = 1

    for path in os.listdir(source):
        path = os.path.join(source, path)

        features = np.array([])
        
        # reading audio files of speaker
        (sr, audio) = read(path)
        
        # extract 40 dimensional MFCC & delta MFCC features
        vector   = extract_features(audio,sr)

        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))
            
        # when features of 3 files of speaker are concatenated, then do model training
        if count == 3:    
            gmm = GMM(n_components = 16, n_iter = 200, covariance_type='diag',n_init = 3)
            gmm.fit(features)

            # saving the trained gaussian model
            pickle.dump(gmm, open(dest + self.name + '.gmm', 'wb'))
            self.sendResponse(self.name + ' added successfully') 
            
            features = np.asarray(())
            count = 0
        count = count + 1

