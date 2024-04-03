import numpy as np

#Functions that allow users to input the windspeed, diameter of wind turbine and wind turbine efficiency
def getwindspeed():
    windspeed=float(input("Please enter the wind speed (in ms^-1)"))
    return windspeed
windspeed=getwindspeed()

def getdiameter():
    print ("Suggested wind turbine diameters are: \n 103m - used in the Raith Wind Farm \n 137m - produced by GEVERNOVA \n 164m - produced by GEVERNOVA")
    desireddiameter=float(input("Please enter your desired diameter of your wind turbine (m)"))
    return desireddiameter
desireddiameter=getdiameter()

def getwindeff():
    windeff=float(input("Please enter the efficiency of the wind turbine as a decimal"))
    return windeff
windeff=getwindeff()

#Outputs the power of the wind turbine in kilowatts
windpowerkwatts=((float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2)/1000
print(f"At a wind speed of {windspeed} ms^-1, with an efficiency of {windeff}, a wind turbine will produce {round(windpowerkwatts,2)} kW of Power")

#Functions that allows the user to input the number of solar hours, area of solar panel and solar panel efficiency
def getsolarhours():
    solarhours=float(input("Please enter the number of sun hours in the day"))
    return solarhours
solarhours=getsolarhours()

def getarea():
    desiredarea=float(input("Please enter your desired area of your solar panel (m^2)"))
    return desiredarea
desiredarea=getarea()

def getsolareff():
    solareff=float(input("Please enter the efficiency of the solar panel as a decimal"))
    return solareff
solareff=getsolareff()

#Outputs the power of the solar panel in kilowatts
solarpowerkwatts=float(solareff)*float(desiredarea)*float(solarhours)
print(f"For a day with {solarhours} sun hours, a {desiredarea}m^2 solar panel, with an efficiency of {solareff} will produce {solarpowerkwatts} kW of power")           
