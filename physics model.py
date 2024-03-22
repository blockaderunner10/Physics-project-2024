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
def model(month,time,noofSP,noofWT,noofTT):#Inputs will be month, time, number of Solar Panels, number of Wind Turbines, number of Tidal Turbines
    month=month-1 #Subtracting 1 to factor in for first element being 0th index in the array but 1st month (January), for example
    time=time-1 
    
    sources=['Energy Demand','Tidal Supply', 'Solar Supply', 'Onshore Wind Supply','Net Energy']#Creating categories for x axis bar charts
    
    datatoplot=np.zeros((5,1)) #Creating an empty array for values to plot
    
    #Calculating Energy Demand per hour from data in csv
    datatoplot[0,0]=float(proportionsforhours[time][1])*float(energyperday[month][1])

    print(datatoplot)
    
    #Plotting bar chart
    plt.bar(sources, datatoplot[0:,0])
    plt.xlabel('Resource')
    plt.ylabel('Energy Demand/Supply in kWh per hour')
    plt.title(f"Energy Demand against our plan for renewable energy at {proportionsforhours[time][0]}:00 in {energyperday[month][0]}")
    plt.show()

def getdate():
    desiredmonth=input("please enter your desired month (use the 3 letter forms all caps)")
    if desiredmonth=="JAN":
        desiredmonthint=1
    if desiredmonth=="FEB":
        desiredmonthint=2
    if desiredmonth=="MAR":
        desiredmonthint=3
    if desiredmonth=="APR":
        desiredmonthint=4
    if desiredmonth=="MAY":
        desiredmonthint=5
    if desiredmonth=="JUN":
        desiredmonthint=6
    if desiredmonth=="JUL":
        desiredmonthint=7
    if desiredmonth=="AUG":
        desiredmonthint=8
    if desiredmonth=="SEP":
        desiredmonthint=9
    if desiredmonth=="OCT":
        desiredmonthint=10
    if desiredmonth=="NOV":
        desiredmonthint=11
    if desiredmonth=="DEC":
        desiredmonthint=12
    else:
        print("Input not recognised please re-run the program")
    desiredmonthint2=desiredmonthint
    return (desiredmonthint2,desiredmonth)
    print(desiredmonthint2, desiredmonth)
    
desiredmonth, desiredmonthint2 =getdate()
print(desiredmonth) 
model(desiredmonth,12,0,0,0)#Testing with February 12:00
