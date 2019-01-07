import numpy as np
docs = "Can I eat the Pizza".lower().split()
doc1 = set(docs)
doc1 = sorted(doc1)
print ("\nvalues: ", doc1)

integer_encoded = []
for i in docs:
    v = np.where( np.array(doc1) == i)[0][0]
    integer_encoded.append(v)
print ("\ninteger encoded: ",integer_encoded)

def get_vec(len_doc,word):
    empty_vector = [0] * len_doc
    vect = 0
    find = np.where( np.array(doc1) == word)[0][0]
    empty_vector[find] = 1
    return empty_vector

def get_matrix(doc1):
    mat = []
    len_doc = len(doc1)
    for i in docs:
        vec = get_vec(len_doc,i)
        mat.append(vec)
        
    return np.asarray(mat)

print ("\nMATRIX:")
print (get_matrix(doc1))
    
"""
OUTPUT: 
values:  ['can', 'eat', 'i', 'pizza', 'the']

integer encoded:  [0, 2, 1, 4, 3]

MATRIX:
[[1 0 0 0 0]
 [0 0 1 0 0]
 [0 1 0 0 0]
 [0 0 0 0 1]
 [0 0 0 1 0]]
"""
