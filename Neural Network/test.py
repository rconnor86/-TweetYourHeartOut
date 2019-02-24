import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
import os

MAX_LENGTH = 140

print('Reloading the tokenizer')

with open('C:/Users/Karl/OneDrive - Washington State University (email.wsu.edu)/School/Hackathon/2019/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# human friendly printing
labels = ['empty', 'relief', 'neutral', 'boredom', 'anger', 'hate', 'enthusiasm', 'fun', 'happiness',
          'love', 'sadness', 'surprise', 'worry']

model = keras.models.load_model('C:/Users/Karl/OneDrive - Washington State University (email.wsu.edu)/School/Hackathon/2019/TwitterModel.h5')
model.summary()

while 1:
    evalSentence = []
    evalSentence.append(input('Input a sentnece to be evaluated, or Enter to quit: '))
    evalSentence.append('I feel sad. Me is sad')
    print(evalSentence)

    if len(evalSentence[0]) == 0:
        break

    sentenceSequence = tokenizer.texts_to_sequences(evalSentence)
    print(sentenceSequence)
    sentenceSequence = keras.preprocessing.sequence.pad_sequences(sentenceSequence, maxlen=MAX_LENGTH, padding='post')

    pred = model.predict_classes(sentenceSequence)


    #print("%s sentiment; %f%% confidence" %
    #      (labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
    print(pred)