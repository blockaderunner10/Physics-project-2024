import csv
import numpy as np
import matplotlib.pyplot as plt

with open('DATA FOR MODEL.csv', newline='') as csvfile: #Importing our csv of data for model of power consumption
    reader = csv.reader(csvfile, delimiter=',')
    pcd = list(reader)

proportionsforhours = [[x[0], (x[1])] for x in pcd[1:26]]

energyperday = [[x[3], (x[4])] for x in pcd[1:14]]

#MODEL OF POWER CONSUMPTION
def model(month,time):
    x=month-1 #Subtracting 1 to factor in for first element being 0th index but 1st month (January), for example
    y=time-1
    datatoplot=np.zeros((5,1))
    datatoplot[0,0]=-float(proportionsforhours[x][1])*float(energyperday[y][1])
    sources=['Energy Demand','Tidal Supply', 'Solar Supply', 'Onshore Wind Supply','Net Energy']
    print(datatoplot)
    plt.bar(sources, datatoplot[0:,0])
    plt.xlabel('Resource')
    plt.ylabel('Energy Demand/Supply in kWh per hour')
    plt.title('dkvks')
    plt.show()

powerconsumption(2,5)
#{proportionsforhours[y][0]} o'clock on a given day in {energyperday[x][0]}
#monthandtime=str(energyperday[x][0] + proportionsforhours[y][0])
