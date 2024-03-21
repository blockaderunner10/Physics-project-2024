import csv
import numpy as np
import matplotlib.pyplot as plt

#Importing and adjusting csv for Energy Consumption Data
with open('DATA FOR MODEL.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pcd = list(reader)

proportionsforhours = [[x[0], (x[1])] for x in pcd[1:26]]#Removing headers and grouping data to make objects

energyperday = [[x[3], (x[4])] for x in pcd[1:14]]

#MODEL OF POWER CONSUMPTION
def model(month,time):
    y=month-1 #Subtracting 1 to factor in for first element being 0th index in the array but 1st month (January), for example
    x=time-1
    
    sources=['Energy Demand','Tidal Supply', 'Solar Supply', 'Onshore Wind Supply','Net Energy']#Creating categories for x axis bar charts
    
    datatoplot=np.zeros((5,1)) #Creating an empty array for values to plot
    
    #Calculating Energy Demand per hour from data in csv
    datatoplot[0,0]=-float(proportionsforhours[x][1])*float(energyperday[y][1])

    print(datatoplot)
    
    plt.bar(sources, datatoplot[0:,0])
    plt.xlabel('Resource')
    plt.ylabel('Energy Demand/Supply in kWh per hour')
    plt.title(f"Energy Demand against our plan for renewable energy at {proportionsforhours[x][0]}:00 in {energyperday[y][0]}")
    plt.show()

model(2,21)#Testing with February 21:00
