from keras.preprocessing.text import Tokenizer
from numpy import array
from numpy import argmax
from keras.utils import to_categorical


doc = "Can I eat the Pizza".lower().split()

def using_Tokenizer(doc):
    # create the tokenizer
    t = Tokenizer()
    # fit the tokenizer on the documents
    t.fit_on_texts(doc)

    # integer encode documents
    encoded_docs = t.texts_to_matrix(doc, mode='count')
    return encoded_docs

def using_to_categorical(doc):
    label_encoder = LabelEncoder()
    data = label_encoder.fit_transform(doc)
    data = array(data)

    # one hot encode
    encoded = to_categorical(data)
    return encoded

def invert_encoding(row_num):
    inverted = label_encoder.inverse_transform([argmax(onehot_encoded[row_num, :])])
    return inverted
    
print ("===using Keras Tokenizer for OneHotEncoding===")
print (using_Tokenizer(doc))
print ()
print ("===using Keras to_categorical for OneHotEncoding===")
print (using_to_categorical(doc))
print ()
print (invert_encoding(int(0)))

"""
OUTPUT:
===using Keras Tokenizer for OneHotEncoding===
[[0. 1. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]]

===using Keras to_categorical for OneHotEncoding===
[[1. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 0. 0. 1.]
 [0. 0. 0. 1. 0.]]

['can']
"""
