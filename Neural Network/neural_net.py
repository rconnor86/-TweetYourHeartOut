from __future__ import absolute_import, division, print_function
import numpy as np
import tensorflow as tf
from tensorflow import keras
import json
import pickle

VOCAB = 20000  # Number of words the program will 'know'
MAX_LENGTH = 140  # The max number of words that will be allowed in a tweet

print('Extracting data from data.csv')
# Extract from data.csv
data1 = np.genfromtxt("Data/data.csv", skip_header=1,  comments=None, delimiter=',', encoding='utf-8', dtype=None)
data2 = np.genfromtxt("Data/text_emotion.csv", encoding='utf-8', skip_header=1,
                      delimiter=',', usecols=(1, 3), dtype=None)

print('Combining data into x and y lists')
# Combine data into single variables
data1_x = [x[0] for x in data1]
data2_x = [x[1] for x in data2]

data1_y = [x[1] for x in data1]
data2_y = [x[0] for x in data2]

data_x = data2_x
data_y = data2_y

for emote, i in zip(data_y, range(0, len(data_y))):
    if emote == 'empty':
        emote = emote.replace('empty', '0')
    if emote == 'relief':
        emote = emote.replace('relief', '1')
    if emote == 'neutral':
        emote = emote.replace('neutral', '2')
    if emote == 'boredom':
        emote = emote.replace('boredom', '3')
    if emote == 'anger':
        emote = emote.replace('anger', '4')
    if emote == 'hate':
        emote = emote.replace('hate', '5')
    if emote == 'enthusiasm':
        emote = emote.replace('enthusiasm', '6')
    if emote == 'fun':
        emote = emote.replace('fun', '7')
    if emote == 'happiness':
        emote = emote.replace('happiness', '8')
    if emote == 'love':
        emote = emote.replace('love', '9')
    if emote == 'sadness':
        emote = emote.replace('sadness', '10')
    if emote == 'surprise':
        emote = emote.replace('surprise', '11')
    if emote == 'worry':
        emote = emote.replace('worry', '12')
    data_y[i] = int(emote)

print('Tokenizing data')
tokenizer = keras.preprocessing.text.Tokenizer(num_words=VOCAB)
# Feed the tweets to the tokenizer
tokenizer.fit_on_texts(data_x)

print('Creating and saving dictionary')
dictionary = tokenizer.word_index
with open('dictionary.json', 'w') as dictf:
    json.dump(dictionary, dictf)
print('Convert x data to sequences and y to numpy array')
x_sequences = tokenizer.texts_to_sequences(data_x)
data_y = np.asarray(data_y)

print('Padding the sequences')
x_sequences = keras.preprocessing.sequence.pad_sequences(x_sequences, maxlen=MAX_LENGTH, padding='post')

print('Saving the tokenizer')
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print('Making Model')
model = keras.Sequential()
model.add(keras.layers.Embedding(VOCAB, 16))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.SeparableConv1D(filters=60, kernel_size=5, activation='relu',
                                       bias_initializer='random_uniform', depthwise_initializer='random_uniform',
                                       padding='same'))
model.add(keras.layers.SeparableConv1D(filters=60, kernel_size=5, activation='relu',
                                       bias_initializer='random_uniform', depthwise_initializer='random_uniform',
                                       padding='same'))
model.add(keras.layers.MaxPooling1D(pool_size=5))
model.add(keras.layers.SeparableConv1D(filters=120, kernel_size=5, activation='relu',
                                       bias_initializer='random_uniform', depthwise_initializer='random_uniform',
                                       padding='same'))
model.add(keras.layers.SeparableConv1D(filters=120, kernel_size=5, activation='relu',
                                       bias_initializer='random_uniform', depthwise_initializer='random_uniform',
                                       padding='same'))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.Dense(13, activation='sigmoid'))

model.summary()

print('Splitting data')
x_train = x_sequences
y_train = data_y
y_train = keras.utils.to_categorical(y_train, num_classes=13)

print(len(x_train))
print(len(y_train))

print(y_train[0])
print(y_train[1])
print(data_y[0])
print(data_y[1])


print('Compiling model')
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print('Train model')
history = model.fit(x_train,
                    y_train,
                    batch_size=50,
                    epochs=10,
                    validation_split=0.1,
                    verbose=1)

model.save('TwitterModel.h5')


