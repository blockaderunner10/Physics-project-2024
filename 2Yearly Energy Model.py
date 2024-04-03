import csv
import numpy as np
import matplotlib.pyplot as plt

#Importing and adjusting csv data
with open('./DATA/DATA FOR MODEL.csv', newline='') as csvfile:
    reader0 = csv.reader(csvfile, delimiter=',')
    dfm = list(reader0)
with open('./DATA/WINDTURBINEDATA.csv', newline='') as csvfile:
    reader1 = csv.reader(csvfile, delimiter=',')
    wtd = list(reader1)
    
with open('./DATA/SOLARDATA.csv', newline='') as csvfile:
    reader2 = csv.reader(csvfile, delimiter=',')
    sd = list(reader2)

#Removing headers and grouping data to make objects that can be referenced later
proportionsforhours = [[x[0], (x[1])] for x in dfm[1:26]]
energyperday = [[x[3], (x[4])] for x in dfm[1:13]]
windturb = [[(x[5]), (x[6])] for x in wtd[1:13]]
solardata = [[(x[4]),(x[5]),(x[6])] for x in sd[1:13]]

#Creating an array for the number of days in each month so this can be referenced later
daysinmonth= [(1,31), (2,28), (3,31), (4,30), (5,31), (6,30), (7,31),(8,31), (9,30), (10,31), (11,30), (12,31)]

#Month names which will form the x-axis of graphs later
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#Model of energy consumption, which reads in data from the csv
#We have a column of proportion of yearly energy consumed per day, so multiplying this by the number of days in the month will give the monthly energy consumption in kWh
def model():
    energypermonth=np.zeros((12,1))
    for i in range (12):
        energypermonth[i][0]=float(energyperday[i][1])*float(daysinmonth[i][1])
        plt.bar(months[i], energypermonth[i],color='red')
    plt.xlabel('Months')
    plt.ylabel('Energy consumption (kWh)')
    plt.title('Energy consumed per month over a year')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return energypermonth

#Functions that allow the user to input how many and what dimension wind turbines they want 
def getinfowind():
    desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
    while  desiredwindturb <0:
        print ("You can't a have negative number of wind turbines")
        desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
        if desiredwindturb>=0:
            break
    print ("Suggested wind turbine diameters are: \n 103m - used in the Raith Wind Farm \n 137m - produced by GEVERNOVA \n 164m - produced by GEVERNOVA")
    desireddiameter=float(input("What diameter of wind turbine do you wish to model (m)?"))
    return (desiredwindturb,desireddiameter)

#Functions that allow the user to input how many and what dimension solar panels they want (both in between the wind turbines and on houses)
def getNoOfSolarPanels1():
    desiredsolarpanels1=float(input("Please enter the number of solar panels you wish to put up in between wind turbines"))
    while  desiredsolarpanels1 <0:
        print ("You can't a have negative number of solar panels")
        desiredsolarpanels1=float(input("Please enter the number of solar panels you wish to put up in between wind turbines"))
        if desiredsolarpanels1>=0:
            break
    desiredarea1=float(input("What area would you like these solar panels to be (m^2)?"))
    return (desiredsolarpanels1,desiredarea1)

def getNoOfSolarPanels2():
    desiredsolarpanels2=float(input("Please enter the number of solar panels you wish to put up on houses"))
    while  desiredsolarpanels2 <0:
        print ("You can't a have negative number of solar panels")
        desiredsolarpanels2=float(input("Please enter the number of solar panels you wish to put up"))
        if desiredsolarpanels2>=0:
            break
    desiredarea2=float(input("What area would you like these solar panels to be (m^2)?"))
    return (desiredsolarpanels2,desiredarea2)


#Wind energy calculations
def windcalc(desiredwindturb,desireddiameter):
    windenergykWhpermonth=np.zeros((12,1)) #Creates an empty array for the wind energy data to go into
    for i in range (12):
        windspeed=windturb[i][0] #Reads in the average wind speed in that month from the csv
        windeff=windturb[i][1] #Reads in the efficiency of wind turbines at that speed from the csv
        windpowerwatts=(float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2 #Calculates the power produced by a wind turbine at that wind speed and efficiency
        windenergykWhpermonth[i][0]=((((windpowerwatts)/1000)*(float(daysinmonth[i][1])*24)))*desiredwindturb #Calculates the energy produced in a month in kWh
        plt.bar(months[i], windenergykWhpermonth[i],color='green') #Plots on the graph
    plt.xlabel('Months')
    plt.ylabel('Energy produced by wind turbines (kWh)')
    plt.title(f"Energy produced by {int(desiredwindturb)} ({desireddiameter}m) wind turbines per month")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return(windenergykWhpermonth)

#Solar energy calculations
def solarcalcs(desiredarea1,desiredsolarpanels1,desiredarea2,desiredsolarpanels2):
    monthlysolarenergyinkWh=np.zeros((12,1)) #Creates an empty array for the solar energy data to go into
    for j in range (12):
        irradiance=solardata[j][0] #Reads in the average irradiance in that month from the csv
        #Calculating solar power for both the solar panels in the wind farm and on houses
        solarpowerinkW= ((0.2*float(desiredarea1)*float(irradiance)*float(desiredsolarpanels1))+(0.2*float(desiredarea2)*float(irradiance)*float(desiredsolarpanels2)))/1000
        #1kW for 1 hour = 1kWh, so sum and multiply by the number of days in the month
        monthlysolarenergyinkWh[j][0]=solarpowerinkW*daysinmonth[j][1]*24 #Converts to monthly
        plt.bar(months[j],monthlysolarenergyinkWh[j][0],color='green') #Plots on graph
    plt.xlabel('Months')
    plt.ylabel('Energy produced by solar panels (kWh)')
    plt.title(f"Energy produced by the solar panels per month")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return monthlysolarenergyinkWh

#This function takes in all of the previously calculated data (energy consumed per month and energy produced by solar and wind per month), and plots a graph of net energy
def netenergy(energypermonth,windenergykWhpermonth,monthlysolarenergyinkWh):
    monthlynetenergyinkWh=np.zeros((12,1))
    for i in range (12):
        monthlynetenergyinkWh[i][0]=-energypermonth[i][0]+windenergykWhpermonth[i][0]+monthlysolarenergyinkWh[i][0]
        if monthlynetenergyinkWh[i]>0:#If you have a surplus the bar will be green
            plt.bar(months[i],monthlynetenergyinkWh[i][0],color='green')
        else:#If you have a deficit the bar will be red
            plt.bar(months[i],monthlynetenergyinkWh[i][0],color='red')
    plt.xlabel('Months')
    plt.ylabel('Net Energy per Month (kWh)')
    plt.title(f"Net Energy per Month with your inputted renewable plan")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return monthlynetenergyinkWh

#This function takes in the monthly net energy and will output the energy in storage per month (cumulative)
def storage(monthlynetenergyinkWh):
    storageinkWh=np.zeros((12,1))
    for i in range (12):
        storageinkWh[i][0]=storageinkWh[i-1][0]+monthlynetenergyinkWh[i][0]#This calculates cumulative energy over the year (energy in storage)
        if storageinkWh[i]>0:
            plt.bar(months[i],storageinkWh[i][0],color='green')
        else:
            plt.bar(months[i],storageinkWh[i][0],color='red')
    plt.xlabel('Months')
    plt.ylabel('Energy in Storage at the start each month (in kWh)')
    plt.title(f"Energy in Storage at the start each month with your inputted renewable plan")
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    return storageinkWh
#You want to optimise the numbers that you input, so that this entire graph has bars = 0 or green
#This means that you have enough energy in storage to run the town at all times

#This is a stacked bar chart of the energy produced by the two sources (in kWh) over the months of the year, for comparison
def ProportionofGeneration(windenergykWhpermonth,monthlysolarenergyinkWh):
    x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    y1=windenergykWhpermonth.flatten()
    y2=monthlysolarenergyinkWh.flatten()
    if None in windenergykWhpermonth or None in monthlysolarenergyinkWh:
        print ("Please enter data")
    plt.bar(x, y1, color='orange',label='Wind Energy')
    plt.bar(x, y2, bottom=y1, color='green',label='Solar Energy')#You want the second bar to start when the first finishes
    plt.legend()
    plt.show()
    return (y1,y2,x)


desiredwindturb,desireddiameter=getinfowind()
desiredsolarpanels1,desiredarea1=getNoOfSolarPanels1()
desiredsolarpanels2,desiredarea2=getNoOfSolarPanels2()
windenergykWhpermonth=windcalc(desiredwindturb,desireddiameter)
monthlysolarenergyinkWh=solarcalcs(desiredarea1,desiredsolarpanels1,desiredarea2,desiredsolarpanels2)
energypermonth=model()
monthlynetenergyinkWh=netenergy(energypermonth,windenergykWhpermonth,monthlysolarenergyinkWh)
storageinkWh=storage(monthlynetenergyinkWh)
(y1,y2,x)=ProportionofGeneration(windenergykWhpermonth,monthlysolarenergyinkWh)
