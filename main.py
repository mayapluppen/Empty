import tkinter as gui
from unicodedata import decimal
import math
import function as function
import csv 
import os
import datetime
import constants
import os

window = gui.Tk()

#Steg 1

for filename in os.listdir(os.getcwd()):
    if 'csv' in filename:
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            #Get files with correct format
            if constants.filePrefix in filename:
                dateSuffix = filename[-8:-6]
                if int(dateSuffix) <= constants.endDate and int(dateSuffix) >= constants.startDate:
                    print(filename)