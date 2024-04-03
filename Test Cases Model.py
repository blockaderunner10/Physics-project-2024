import numpy as np

def getwindspeed():
    windspeed=float(input("Please enter the wind speed (in ms^-1)"))
    while  windspeed <0:
        print ("You can't a have wind speed")
        windspeed=float(input("Please enter the number of solar panels you wish to put up in between wind turbines"))
        if windspeed>=0:
            break
    return windspeed
windspeed=getwindspeed()

def getdiameter():
    desireddiameter=float(input("Please enter your desired diamter of wind turbine (m)"))
    return desireddiameter
desireddiameter=getdiameter()

def getwindeff():
    windeff=float(input("Please enter the efficiency of the wind turbine as a decimal"))
    return windeff
windeff=getwindeff()

windpowerkwatts=((float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2)/1000
print(f"At a wind speed of {windspeed} ms^-1, with an efficiency of {windeff}, a wind turbine will produce {windpowerkwatts} kilowatts of Power")
