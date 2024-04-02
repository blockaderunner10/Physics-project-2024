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
daysinmonth= [(1,31), (2,28), (3,31), (4,30), (5,31), (6,30), (7,31),(8,31), (9,30), (10,31), (11,30), (12,31)]
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def model():
    energypermonth=np.zeros((12,1))
    for i in range (12):
        energypermonth[i][0]=float(energyperday[i][1])*float(daysinmonth[i][1])
    for i in range (0,12):
        plt.bar(months[i], energypermonth[i],color='red')
    plt.xlabel('Months')
    plt.ylabel('Energy consumption (kWh)')
    plt.title('Energy consumed per month over a year')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return energypermonth
    
def getinfowind():
    desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
    while  desiredwindturb <0:
        print ("You can't a have negative number of wind turbines")
        desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
        if desiredwindturb>=0:
            break
    desireddiameter=float(input("What diameter of wind turbine do you wish to model (m)?"))
    return (desiredwindturb,desireddiameter)

def getNoOfSolarPanels():
    desiredsolarpanels=float(input("Please enter the number of solar panels you wish to put up"))
    while  desiredsolarpanels <0:
        print ("You can't a have negative number of solar panels")
        desiredwindturb=float(input("Please enter the number of solar panels you wish to put up"))
        if desiredwindturb>=0:
            break
    desiredarea=float(input("What area would you like your solar panel to be (m^2)?"))
    return (desiredsolarpanels,desiredarea)

def windcalc(desiredwindturb,desireddiameter):
    windenergykWhpermonth=np.zeros((12,1))
    for i in range (12):
        windeff=windturb[i][1]
        windspeed=windturb[i][0]
        windpowerwatts=(float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2
        windenergykWhpermonth[i][0]=((((windpowerwatts)/1000)*(float(daysinmonth[i][1])*24)))*desiredwindturb
        plt.bar(months[i], windenergykWhpermonth[i],color='green')
    plt.xlabel('Months')
    plt.ylabel('Energy produced by wind turbines (kWh)')
    plt.title(f"Energy produced by {int(desiredwindturb)} ({desireddiameter}m) wind turbines per month")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return(windenergykWhpermonth)

def solarcalcs(desiredarea,desiredsolarpanels):
    monthlysolarenergyinkWh=np.zeros((12,1))
    for j in range (12):
        for i in range (24):
            if i>float(solardata[j][2]) or i<float(solardata[j][1]):#If after sunset or before sunrise, no energy
                hourlysolarenergyinkWh=0
            else:
                sunhours=solardata[j][0]
                hourlysolarenergyinkWh= 0.2*float(desiredarea)*float(sunhours)*float(desiredsolarpanels)
                monthlysolarenergyinkWh[j][0]+=hourlysolarenergyinkWh*daysinmonth[j][1]*24
        plt.bar(months[j],monthlysolarenergyinkWh[j][0],color='green')
    plt.xlabel('Months')
    plt.ylabel('Energy produced by solar panels (kWh)')
    plt.title(f"Energy produced by {int(desiredsolarpanels)} ({desiredarea}m^2) solar panels per month")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return monthlysolarenergyinkWh

def netenergy(energypermonth,windenergykWhpermonth,monthlysolarenergyinkWh):
    monthlynetenergyinkWh=np.zeros((12,1))
    for i in range (12):
        monthlynetenergyinkWh[i][0]=-energypermonth[i][0]+windenergykWhpermonth[i][0]+monthlysolarenergyinkWh[i][0]
        if monthlynetenergyinkWh[i]>0:
            plt.bar(months[i],monthlynetenergyinkWh[i][0],color='green')
        else:
            plt.bar(months[i],monthlynetenergyinkWh[i][0],color='red')
    plt.xlabel('Months')
    plt.ylabel('Net Energy per Month (kWh)')
    plt.title(f"Net Energy per month with {int(desiredsolarpanels)} ({desiredarea}m^2) solar panels and {int(desiredwindturb)} ({desireddiameter}m blade) wind turbines")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return monthlynetenergyinkWh

def storage(monthlynetenergyinkWh):
    storageinkWh=np.zeros((12,1))
    for i in range (12):
        storageinkWh[i][0]=storageinkWh[i-1][0]+monthlynetenergyinkWh[i][0]
        if storageinkWh[i]>0:
            plt.bar(months[i],storageinkWh[i][0],color='green')
        else:
            plt.bar(months[i],storageinkWh[i][0],color='red')
    plt.xlabel('Months')
    plt.ylabel('Energy in Storage at the start each month (in kWh)')
    plt.title(f"Energy in Storage at the start each month with {int(desiredsolarpanels)} ({desiredarea}m^2) solar panels and {int(desiredwindturb)} ({desireddiameter}m blade) wind turbines")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return storageinkWh

desiredwindturb,desireddiameter=getinfowind()
desiredsolarpanels,desiredarea=getNoOfSolarPanels()
windenergykWhpermonth=windcalc(desiredwindturb,desireddiameter)
monthlysolarenergyinkWh=solarcalcs(desiredarea,desiredsolarpanels)
energypermonth=model()
monthlynetenergyinkWh=netenergy(energypermonth,windenergykWhpermonth,monthlysolarenergyinkWh)
storageinkWh=storage(monthlynetenergyinkWh)
