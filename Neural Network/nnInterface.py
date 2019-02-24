from tensorflow import keras
import numpy as np
import pickle

def loadModel():
    print('Loading the model')
    return keras.models.load_model('TwitterModel.h5')


def loadTokenizer():
    print('Loading the tokenizer')
    with open('tokenizer.pickle', 'rb') as handle:
        return pickle.load(handle)


def readFromCSV(csvPath):
    print("Reading from ", csvPath)
    return np.genfromtxt(csvPath, comments=None, delimiter=',', encoding='utf-8', dtype=None)


def tokenize(sentences):
    print(sentences)
    tokenizer = loadTokenizer()
    return tokenizer.texts_to_sequences(sentences)


def padSentences(sentences, max_length):
    return keras.preprocessing.sequence.pad_sequences(sentences, maxlen=max_length, padding='post')


def prepareData(csvPath):
    MAX_LENGTH = 140
    data = readFromCSV(csvPath)
    tokens = tokenize(data)
    return padSentences(tokens, 140)


def runPredictiveModel(tokens):
    model = loadModel()
    return model.predict_classes(tokens)


def analyzePredComplex(preds):
    labels = ['empty', 'relief', 'neutral', 'boredom', 'anger', 'hate', 'enthusiasm', 'fun', 'happiness', 'love', 'sadness', 'surprise', 'worry']
    return labels[np.bincount(preds).argmax()]


def analyzePredSimple(preds):
    labels = ['empty', 'relief', 'neutral', 'anger', 'happiness', 'sadness', 'surprise', 'worry']
    values = []
    for x in preds:
        if x == 0:
            values.append(0)
        if x == 1:
            values.append(1)
        if x == 2 or x == 3:
            values.append(2)
        if x == 4 or x == 5:
            values.append(3)
        if x == 6 or x == 7 or x == 8 or x == 9:
            values.append(4)
        if x == 10:
            values.append(5)
        if x == 11:
            values.append(6)
        if x == 12:
            values.append(12)

    return labels[np.bincount(values).argmax()]


def runNextwork(csvPath, mode=0):
    data = prepareData(csvPath)
    print(data)
    preds = runPredictiveModel(data)

    if mode is 0:
        return analyzePredSimple(preds)
    else:
        return analyzePredComplex(preds)

data = runNextwork('test.csv', 1)
print(data)







