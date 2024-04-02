import csv 
import numpy as np
import matplotlib.pyplot as plt

#Importing and adjusting csv for Energy Consumption Data
with open('./DATA/DATA FOR MODEL.csv', newline='') as csvfile:
    reader0 = csv.reader(csvfile, delimiter=',')
    dfm = list(reader0)
with open('./DATA/WIND_TURBINE_DATA.csv', newline='') as csvfile:
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


def model():
    print(energyperday)
    energypermonth=np.zeros((12,1))
    for i in range (12):
        energypermonth[i][0]=float(energyperday[i][1])*float(daysinmonth[i][1])
        print ('thing 2',i, energypermonth[i])
    months=['January','Febuary','March','April','May','june','july','august','september','october','november','December']
    for i in range (0,11):
        plt.bar(months[i], energypermonth[i],color='green')
    plt.xlabel('Months')
    plt.ylabel('Energy consumption (kWh)')
    plt.title('Energy consumed per month over a year')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    
    
def getinfowind():
    desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
    while  desiredwindturb <0:
        print ("You can't a have negative number of wind turbines")
        desiredwindturb=float(input("Please enter the number of wind turbines you wish to put up"))
        if desiredwindturb>=0:
            break
    desireddiameter=float(input("What diameter of wind turbine do you wish to model (m)?"))
    return (desiredwindturb,desireddiameter)

def windcalc(desiredwindturb,desireddiameter):  #WIND CALC DOES NOT WORK, NEEDS FIXED, OUTPUT VALUE TOO HIGH
    windpermonth=np.zeros((12,1))
    for i in range (12):
        windeff=windturb[i][1]
        print(f"windeff={windeff}")
        windspeed=windturb[i][0]
        print(f"windspeed={windspeed}")
        Windpower1=(float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2
        netwind=((((Windpower1)/1000)*(float(daysinmonth[i][1])*24)))*desiredwindturb
        print (f"power by wind in kW = {netwind}")
        windpermonth[i][0]=netwind 
        print ('energy produced by wind in a month=', windpermonth[i])
    return(windpermonth)

desiredwindturb,desireddiameter=getinfowind()
windpermonth=windcalc(desiredwindturb,desireddiameter)
model()


