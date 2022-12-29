import pyaudio
import numpy as np
 
CHUNK = 1024 
RATE = 44100
 

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib.pyplot import specgram
import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Input, Flatten, Dropout, Activation
from keras.layers import Conv1D, MaxPooling1D, AveragePooling1D
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import confusion_matrix
from keras import regularizers
import os

# mylist= os.listdir('/content/drive/MyDrive/Colab_Notebooks/과제/메타버스/raw_data')

# loading json and creating model
from keras.models import model_from_json
json_file = open("/database/jhkim/metaverse/model.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/database/jhkim/metaverse/Emotion_Voice_Detection_Model.h5")
print("Loaded model from disk")
 
# # evaluate loaded model on test data
# loaded_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
# score = loaded_model.evaluate(x_testcnn, y_test, verbose=0)
# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

data, sampling_rate = librosa.load("/database/jhkim/metaverse/for_test.wav")


import os
import pandas as pd
import librosa
import glob 

X, sample_rate = librosa.load("/database/jhkim/metaverse/for_test.wav", res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
sample_rate = np.array(sample_rate)
mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
featurelive = mfccs
livedf2 = featurelive

livedf2= pd.DataFrame(data=livedf2)
livedf2 = livedf2.stack().to_frame().T
twodim= np.expand_dims(livedf2, axis=2)
livepreds = loaded_model.predict(twodim, 
                         batch_size=32, 
                         verbose=1)

from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

livepreds1=livepreds.argmax(axis=1)
liveabc = livepreds1.astype(int).flatten()

#########################################
angry = livepreds[0][0] + livepreds[0][5]
calm = livepreds[0][1] + livepreds[0][6]
fearful = livepreds[0][2] + livepreds[0][7]
happy = livepreds[0][3] + livepreds[0][8]
sad = livepreds[0][4] + livepreds[0][9]

#########################################

#print(max([angry, calm, fearful, happy, sad]))
print("%s: %.4f%%" % ('angry', angry))
print("%s: %.4f%%" % ('calm', calm))
print("%s: %.4f%%" % ('fearful', fearful))
print("%s: %.4f%%" % ('happy', happy))
print("%s: %.4f%%" % ('sad', sad))


import socket
import time
from datetime import datetime


HOST = '127.0.0.1' 
PORT = 8000       



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(server_socket)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(server_socket)

server_socket.bind((HOST, PORT))

print(server_socket)

server_socket.listen()


client_socket, addr = server_socket.accept()

print('Connected by', addr)

k = 0

'''
while True:
    
    msg = "hello world " + str(k)
    client_socket.sendall(msg.encode())
    print('send 완료 '+ str(k) )
    k += 1
    time.sleep(2)
           
'''
client_socket.close()
server_socket.close()


