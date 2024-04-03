import csv 
import numpy as np
import matplotlib.pyplot as plt

#Importing and adjusting csv for Energy Consumption Data
with open('./DATA/DATA FOR MODEL.csv', newline='') as csvfile:
    reader0 = csv.reader(csvfile, delimiter=',')
    dfm = list(reader0)
with open('./DATA/WINDTURBINEDATA.csv', newline='') as csvfile:
    reader1 = csv.reader(csvfile, delimiter=',')
    wtd = list(reader1)
    
with open('./DATA/SOLARDATA.csv', newline='') as csvfile:
    reader2 = csv.reader(csvfile, delimiter=',')
    sd = list(reader2)

proportionsforhours = [[x[0], (x[1])] for x in dfm[1:26]]#Removing headers and grouping data`a to make objects

energyperday = [[x[3], (x[4])] for x in dfm[1:13]]

windturb = [[(x[5]), (x[6])] for x in wtd[1:13]]

solardata = [[(x[4]),(x[5]),(x[6])] for x in sd[1:13]]

#MODEL
def model(desiredmonthint,desiredtime,noofSP,noofWT):#Inputs will be month, time, number of Solar Panels, number of Wind Turbines, number of Tidal Turbines
    month=desiredmonthint-1
    time=desiredtime-1
    sources=['Energy Demand','Solar Supply', 'Onshore Wind Supply','Net Energy']#Creating categories for x axis bar charts
    
    datatoplot=np.zeros((4,1)) #Creating a zero based array for values to plot
    
    #Calculating Energy Demand per hour from data in csv
    datatoplot[0,0]=(-float(proportionsforhours[time][1])*float(energyperday[month][1]))/24
    
    #Calculating Power from Wind Turbines from wind speed data in csv
    datatoplot[2,0]=windcalcs(desiredmonthint,desireddiameter,desiredwindturb)/1000
    
    datatoplot[1,0]=netsolar
    
    datatoplot[3,0]=datatoplot[1,0]+datatoplot[2,0]+datatoplot[3,0]+datatoplot[0,0]
    
    print(datatoplot)
    
    #Plotting bar chart
    plt.bar(sources[0:3], datatoplot[0:3,0])
    plt.axhline(y=0,color='black',linewidth=1)
    plt.xlabel('Resource')
    plt.ylabel('Power Demand/Supply in kW')
    plt.title(f"Power Demand with our plan for renewable energy at {desiredtime}:00 in {desiredmonth}")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.bar(sources[0],datatoplot[0,0], color="red")
    #sets colours for all of the bar charts
    for i in range (0,4):
        if datatoplot[i,0]>0:
            plt.bar(sources[i],datatoplot[i,0],color='green')
        else:
            plt.bar(sources[i],datatoplot[i,0],color='red')
    
    plt.show()
    return datatoplot

def getDate():
    desiredmonth=input("Please enter the month you would like to model (Use the 3 letter formse.g. JAN or jan for January)")
    return desiredmonth

#creates a data dictionary for the months and their associated values
def getDateInt(desiredmonth):
    monthDict = {"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7,
                 "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12, "jan":1, "feb":2,
                 "mar":3, "apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,
                 "nov":11,"dec":12, "Jan":1, "Feb":2,"Mar":3, "Apr":4,"May":5,"Jun":6,
                 "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12, }
    if desiredmonth not in monthDict:
        while True:
            desiredmonth = input("Please re-enter the desired month in a 3 letter form (CAPS or no caps are allowed)")
            if desiredmonth in monthDict:
                break
    return monthDict[desiredmonth]

#creates a function to get the desired time
def getTime():
    desiredtime=int(input("Please enter the hour you wish to model (between 1 and 24 inclusive e.g. 13 for 1pm)"))
    while desiredtime >24:
        print("Your selected time does not exist")
        desiredtime =int(input("Please enter the hour you wish to model (between 1 and 24 inclusive e.g. 13 for 1pm)"))
        if desiredtime<=24:
            break
    while desiredtime <1:
        print("Your selected time does not exist")
        desiredtime =int(input("Please enter the hour you wish to model (between 1 and 24 inclusive e.g. 13 for 1pm)"))
        if desiredtime>=1:
            break
    return (desiredtime)

#creates a function to get the desired number of wind turbines
def getNoOfWindTurbines():
    desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
    while  desiredwindturb <0:
        print ("You can't a have negative number of wind turbines")
        desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
        if desiredwindturb>=0:
            break
    print ("suggested turbine diameters are: \n 103m used in the raith with farm \n 137m produced by GEVERNOVA \n 164m also produced by GEVERNOVA")
    desireddiameter=float(input("What diameter of wind turbine do you wish to model (m)?"))
    return (desiredwindturb,desireddiameter)

#Calculating power output of wind turbines
def windcalcs(desiredmonthint,desireddiameter,desiredwindturb):
    #Ouputs power output of wind turbines in W
    month=int(desiredmonthint)-1
    windeff=windturb[month][1]
    windspeed=windturb[month][0]
    Windpower1=(float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2
    netwind=Windpower1*desiredwindturb
    return netwind

#Creates a function to get the desired number/area of solar panels
def getNoOfSolarPanels():
    desiredsolarpanels=float(input("Please enter the number of solar panels you wish to put up"))
    while  desiredsolarpanels <0:
        print ("You can't a have negative number of solar panels")
        desiredwindturb=float(input("Please enter the number of solar panels you wish to put up"))
        if desiredwindturb>=0:
            break
    desiredarea=float(input("What area would you like your solar panel to be (m^2)?"))
    return (desiredsolarpanels,desiredarea)

def solarcalcs(desiredmonthint,desiredtime,desiredarea,desiredsolarpanels):
    month=desiredmonthint-1
    if desiredtime>float(solardata[month][2]) or desiredtime<float(solardata[month][1]):#If after sunset or before sunrise, no power
        netsolar=0
    else:
        sunhours=solardata[month][0]
        area=desiredarea
        netsolar= 0.2*float(area)*float(sunhours)*float(desiredsolarpanels)
    return netsolar
#Inputs

desiredmonth = getDate()
desiredmonthint = getDateInt(desiredmonth)
desiredtime = getTime()
desiredwindturb,desireddiameter = getNoOfWindTurbines()
netwind=windcalcs(desiredmonthint,desireddiameter,desiredwindturb)
desiredsolarpanels,desiredarea=getNoOfSolarPanels()
netsolar=solarcalcs(desiredmonthint,desiredtime,desiredarea,desiredsolarpanels)

#Ouptuts:

print("You are creating a graph at", desiredtime, desiredmonth, "(", desiredmonthint, ")")
print("Net wind =",windcalcs(desiredmonthint,desireddiameter,desiredwindturb))
print(f"Net solar = {netsolar}")
datatoplot=model(desiredmonthint,desiredtime,desiredsolarpanels,desiredwindturb)
print(f"Net Power = {datatoplot[3,0]}")
