Created Date: 7 Jan 2019

#### One hot encoding
`Basic of one hot encoding using various ways: numpy,  sklearn, Keras etc.`<br>
The machine cannot understand words and therefore it needs numerical values so as to make it easier for the machine to process the data. To apply any type of algorithm to the data, we need to convert the categorical data to numbers. To achieve this, one hot ending is one way as it converts categorical variables to binary vectors.<br>
##### Example:
Suppose we have a sentence as "Can I eat the Pizza".<br>
looking at this, we can directly say that all the words are different from each other but how will the machine know?
so when we try to apply one hot ending i.e converting the categories into numerical labels.
1. Firstly, convert the text to lower and then sort the words in ascending form i.e A-Z. Now we'll have "can, eat,  i, pizza, the".
2. Give a numerical label as we can see can is at 0th position and eat is at 1 same way, assign the values like can:0, i:2, eat:1, the:4, pizza:3.
3. Transform to binary vectors. 
`[
 can: [1. 0. 0. 0. 0.] 
 i: [0. 0. 1. 0. 0.] 
 eat: [0. 1. 0. 0. 0.] 
 the: [0. 0. 0. 0. 1.] 
 pizza: [0. 0. 0. 1. 0.]
 ]`
 
Got some idea? Are you wondering whats Categorical variable now?<br>
Well, Categorical variables are basically the fixed value number on the basis of some qualitative properties. Such as Sex of an individual as it can be either male or female or trans. Weather is also one example as it can be sunny, cloudy, or rainy. 
Binary variables are nothing but values that contains only 0s and 1s.
