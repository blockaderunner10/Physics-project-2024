import csv
import numpy as np
with open('DATA FOR MODEL.csv', newline='') as csvfile: #Importing our csv of data for model of power consumption
    reader = csv.reader(csvfile, delimiter=',')
    pcd = list(reader)

proportionsforhours = [[x[0], (x[1])] for x in pcd[1:]]#Removing the headings off the columns 'Proportion of daily energy consumption consumed in the given hour'

energyperhour = [[x[3], (x[4])] for x in pcd[1:]]#Removing the headings off the columns 'Average energy consumption per hour (in kWh)'

#MODEL OF POWER CONSUMPTION
def powerconsumption(month,time):
    x=month
    y=time
    return proportionsforhours[x][1]
