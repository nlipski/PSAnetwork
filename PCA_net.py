"""
Assignment3
Nick Lipski
10130209
2016/11/18


The PCA_net class
    decreases the dimension of the input from 2D to 1D
    network has 2 input nodes and 1 output node
    writes the output vector into a separate csv file"""

import csv #imports required libraries
import sys
lRate= 0.1


"""Read method
    reades the instances of the sounds.csv file and enters them into a list"""
def Read(filename):
    list=[]         # initializes all the required variables
    mean=[0.,0.]
    count=0
    with open(filename, 'r') as csvfile:
        file = csv.reader(csvfile, delimiter=',')   # opens and reads the file
        for line in file:                           # iterates through th file line by line
            list.append([float(line[0]),float(line[1])])    # casts the values to the floats and appends them to the list
            mean[0]+=float(line[0])     # also adds them up for the mean values
            mean[1]+=float(line[1])
            count+=1
        mean[0]=mean[0]/count   #calculates the mean for each attribute
        mean[1]=mean[1]/count
    return list,mean    #returns both the list and calculated mean valuse


""" Write function
    saves the list of outputed values into a separate csv file"""
def Write(list):
    with open('output.csv', 'w') as csvfile:
        file = csv.writer(csvfile, lineterminator='\n') #opens and creates a file named ouput.csv
        file.writerow(list) # writes a list into it


""" Train function
    receives weights, data at the iteration and activation of this data line"""
def Train(weights, data, output):
    delta_w=[0.]*2      #initializes a variable
    delta_w[0]=lRate*output*(data[0]-output*weights[0])     # calculates delta values
    delta_w[1] = lRate * output * (data[1] - output * weights[1])
    weights[0]+=delta_w[0]  # adjusts the weight values
    weights[1]+=delta_w[1]
    return weights  #returns adjusted weights


""" Activation function
    receives a data line and weights """
def Activation(data, weights):
    output=weights[0]*data[0]+weights[1]*data[1]    # calcultes an activation value
    return output


"""MeanChange function
    receives a data line and mean values
    subtructs the mean values from the data
    returns an adjusted data line"""
def MeanChange(list, mean):
    list[0]-=mean[0]
    list[1]-=mean[1]
    return list




weights=[1,0]   # initial weights
output=[]       # output list
activation=[]
list, mean=Read("sound.csv")    # reads the input file and creates data list and mean values for it
point=0
for line in list:   #iterates through each instance of data
    list[point]=MeanChange(line,mean)   # adjusts the data values by a mean
    activation=Activation(line,weights) # calculates the activation value
    weights=Train(weights, line ,activation)    # adjust the weights
    point+=1

for line in list:
    output.append(weights[0]*line[0]+weights[1]*line[1])    # appends the output data to the list using fianl

Write(output)   # writes the list to the output file

print("Final weights: ",weights)
