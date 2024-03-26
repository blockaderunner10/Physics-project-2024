import csv
import numpy as np
import matplotlib.pyplot as plt

#Importing and adjusting csv for Energy Consumption Data
with open('./DATA/DATA FOR MODEL.csv', newline='') as csvfile:
    reader0 = csv.reader(csvfile, delimiter=',')
    dfm = list(reader0)
'''
with open('./DATA/DATA FOR MODEL.csv', newline='') as csvfile:
    reader0 = csv.reader(csvfile, delimiter=',')
    pcd = list(reader0)
    '''
with open('./DATA/WIND_TURBINE_DATA.csv', newline='') as csvfile:
    reader1 = csv.reader(csvfile, delimiter=',')
    wtd = list(reader1)

proportionsforhours = [[x[0], (x[1])] for x in dfm[1:26]]#Removing headers and grouping data to make objects

energyperday = [[x[3], (x[4])] for x in dfm[1:14]]

windturb = [[(x[3]), (x[4]), (x[5])] for x in wtd[1:12]]

#MODEL OF POWER CONSUMPTION
def model(month,time,noofSP,noofWT,noofTT):#Inputs will be month, time, number of Solar Panels, number of Wind Turbines, number of Tidal Turbines
    month=month-1 #Subtracting 1 to factor in for first element being 0th index in the array but 1st month (January), for example
    time=time-1 
    
    sources=['Energy Demand','Sewage Supply', 'Solar Supply', 'Onshore Wind Supply','Net Energy']#Creating categories for x axis bar charts
    
    datatoplot=np.zeros((5,1)) #Creating a zero based array for values to plot
    
    #Calculating Energy Demand per hour from data in csv
    datatoplot[0,0]=-float(proportionsforhours[time][1])*float(energyperday[month][1])
    
    #Calculating Power from Wind Turbines from wind speed data in csv
    datatoplot[3,0]=float(windturb[month][2])*desiredwindturb/(1000)
    print ("WINDPOWER CHECK", float(windturb[month][2])*desiredwindturb/(1000))
    
    datatoplot[4,0]=datatoplot[1,0]+datatoplot[2,0]+datatoplot[3,0]+datatoplot[0,0]
    
    print(datatoplot)
    
    
    #Plotting bar chart
    plt.bar(sources[0:3], datatoplot[0:3,0])
    plt.axhline(y=0,color='black',linewidth=1)
    plt.xlabel('Resource')
    plt.ylabel('Power Demand/Supply in kW')
    plt.title(f"Power Demand with our plan for renewable energy at {proportionsforhours[time][0]}:00 in {energyperday[month][0]}")
    plt.tick_params(axis='both', which='major', labelsize=6)
    
    if datatoplot[4,0]>0:
        plt.bar(sources[4],datatoplot[4,0],color='green')
    else:
        plt.bar(sources[4],datatoplot[4,0],color='red')
    
    plt.show()

def getdate():
    desiredmonth=input("Please enter the month you would like to model (Use the 3 letter forms in all caps e.g. JAN for January)")
    match desiredmonth:
        case "JAN":
            desiredmonthint=1
        case "FEB":
            desiredmonthint=2
        case "MAR":
            desiredmonthint=3
        case "APR":
            desiredmonthint=4
        case "MAY":
            desiredmonthint=5
        case "JUN":
            desiredmonthint=6
        case "JUL":
            desiredmonthint=7
        case "AUG":
            desiredmonthint=8
        case "SEP":
            desiredmonthint=9
        case "OCT":
            desiredmonthint=10
        case "NOV":
            desiredmonthint=11
        case "DEC":
            desiredmonthint=12
    return (desiredmonthint,desiredmonth)
    print(desiredmonthint2, desiredmonth)
    
def gettime():
    desiredtime=int(input("Please enter the hour you wish to model (between 1 and 24 inclusive e.g. 13 for 1pm)"))
    return (desiredtime)

def noofwindturbines():
    desiredwindturb=int(input("Please enter the number of wind turbines you wish to put up"))
    return (desiredwindturb)
    

desiredmonth, desiredmonthint =getdate()
desiredtime=gettime()
desiredwindturb=noofwindturbines()
print("You are creating a graph at",desiredtime, desiredmonthint, "(", desiredmonth, ")") 

model(desiredmonth,desiredtime,0,desiredwindturb,0)
