from os import listdir
from os.path import isfile, join
import json
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import correctNames


def getFiles(dir):
    msgFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in range(len(msgFiles)):
        if msgFiles[i].split("_")[0] != 'message':
            msgFiles.remove()
        else:
            msgFiles[i] = dir + '\\' + msgFiles[i]
    return msgFiles


def getParticipantsNames(files):
    participants = []
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            for participant in data['participants']:
                if participant not in participants:
                    participants.append(participant["name"])
    return participants

def setParticipantsMsgcount(participants, files):
    participantsDict = dict()
    for participant in participants:
        participantsDict[participant] = 0

    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            for msg in data['messages']:
                if msg["sender_name"] in participants:
                    participantsDict[msg["sender_name"]] += 1
    return participantsDict


def sortdict(dicttosort):
    dicttosort = dict(sorted(dicttosort.items(), key=lambda item: item[1]))
    sort = [[], []]
    for i in list(msgcount):
        sort[0].append(i)
        sort[1].append(msgcount[i])
    return sort





def drawPieGraph(msgcount):
    sorteddict = sortdict(msgcount)
    msgSum = sum(sorteddict[1])
    sorteddict[0] = correctNames.correctNamess(sorteddict[0])
    for i in range(len(sorteddict[0])):
        sorteddict[0][i] = sorteddict[0][i] + " - " + str(sorteddict[1][i])\
                           + " (" + "%.2f" % round(sorteddict[1][i] * 100 / msgSum, 2) + "%)"

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax.pie(sorteddict[1], startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(sorteddict[0][i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment, **kw)

    plt.show()


root = tk.Tk()
root.withdraw()

mypath = filedialog.askdirectory()
msgcount = setParticipantsMsgcount(getParticipantsNames(getFiles(mypath)), getFiles(mypath))
print(msgcount)

drawPieGraph(msgcount)



