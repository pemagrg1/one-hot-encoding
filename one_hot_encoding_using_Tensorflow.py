import tensorflow as tf
import pandas as pd

text = 'My cat is a great cat'
tokens = text.lower().split()

vocab = set(tokens)
vocab = pd.Series(range(len(vocab)), index=vocab)

word_ids = vocab.loc[tokens].values

inputs = tf.placeholder(tf.int32, [None])
# TensorFlow has an operation for one-hot encoding
one_hot_inputs = tf.one_hot(inputs, len(vocab))
transformed = tf.Session().run(one_hot_inputs, {inputs: word_ids})


print (transformed)
