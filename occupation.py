from flask import Flask, render_template

my_app = Flask(__name__)


def fileOpen(filename):
    inStream = open(str(filename), "r")
    Input = inStream.readlines()
    inStream.close()
    return Input

fileInfo = fileOpen("occupations.csv")

import random

def tidify(jobsList):
    counter = 0
    for string in jobsList:
        jobsList[counter] = string.strip("\r\n")
        counter += 1
    return jobsList

fileInfo = tidify(fileInfo)               

def listify(jobsList):
    counter = 0
    for string in jobsList:
        if string[0] == '"':
            jobsList[counter] = string.split(",")
            while len(jobsList[counter]) != 2:
                jobsList[counter][0] =  jobsList[counter][0] + "," + jobsList[counter][1]
                jobsList[counter].pop(1)
        else :
            jobsList[counter] = string.split(",")
        counter += 1
    return jobsList

fileInfo =  listify(fileInfo)
                
def dictify(listOfList):
    d = {} #dictionary
    for l in listOfList:
        #print l[0]
        d[l[0]] = l[1]
    return d

#print fileInfo
fileDictionary = dictify(fileInfo)
#print fileDictionary

def weightedRandom(d):
    randNum = (1.0 * random.randint(0, 998)) / 10
    keys = d.keys()
    for string in keys:
        if string != "Job Class" and string != "Total":
            randNum = randNum - float(d[string])
        if randNum < 0:
            return string


def ridHead(d):
    newD = {}
    for k in d.keys():
        if k != "Job Class":
            newD[k] = d[k]
    return newD

fileDictionary = ridHead(fileDictionary)
randJob = weightedRandom(fileDictionary)

@my_app.route('/occupations')
def main():
    return render_template('occupations.html', listkeys = fileDictionary.keys(), d = fileDictionary, randomJob = randJob)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
