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

proportionsforhours = [[x[0], (x[1])] for x in dfm[1:26]]#Removing headers and grouping data to make objects

energyperday = [[x[3], (x[4])] for x in dfm[1:14]]

windturb = [[(x[5]), (x[6])] for x in wtd[1:12]]


def model(month,time,noofSP,noofWT,noofTT) -> None:
    """Models the data and plots it to a matplotlib graph.

    Args:
        month (str): 3 Letter form of the month you wish to model for
        time (int): 24 Hour representation of the time you wish to model for
        noofSP (_type_): Number of Solar Panels
        noofWT (_type_): Number of Wind Turbines
        noofTT (_type_): Number of Tidal Turbines
    """
    
    sources=['Energy Demand','Sewage Supply', 'Solar Supply', 'Onshore Wind Supply','Net Energy'] # Creating categories for x axis bar charts
    
    datatoplot=np.zeros((5,1)) #Creating a zero based array for values to plot
    
    datatoplot[0,0]=-float(proportionsforhours[time][1])*float(energyperday[month][1]) #Calculating Energy Demand per hour from data in csv
    
    datatoplot[3,0]=windcalcs(desired_month_int,desired_diameter,desired_wind_turb)/1000 #Calculating Power from Wind Turbines from wind speed data in csv
    
    datatoplot[4,0]=datatoplot[1,0]+datatoplot[2,0]+datatoplot[3,0]+datatoplot[0,0]
    
    print(datatoplot)
    
    plt.bar(sources[0:4], datatoplot[0:4,0]) # Set initial sources for graph
    plt.axhline(y=0,color='black',linewidth=1) # Plot a straight line from y=0 to infinity
    plt.xlabel('Resource') # Set the X-axis label
    plt.ylabel('Power Demand/Supply in kW') # Set the Y-Axis label
    plt.title(f"Power Demand with our plan for renewable energy at {desired_time}:00 in {desired_month}") # Configure graph title
    plt.tick_params(axis='both', which='major', labelsize=6) 
    plt.bar(sources[0],datatoplot[0,0], color="red") # Set addition source for graph

    if datatoplot[3,0]>0: # Is the X above 0?
        plt.bar(sources[3],datatoplot[3,0],color='green') # Positive X, so display green
    else: # If not.
        plt.bar(sources[3],datatoplot[3,0],color='red') # Negative X, so display red

    if datatoplot[4,0]>0: # Is the Y above 0?
        plt.bar(sources[4],datatoplot[4,0],color='green') # Positive Y, so display green
    else: # If not.
        plt.bar(sources[4],datatoplot[4,0],color='red') # Negative Y, so display red
    
    plt.show() # Show the output graph.


def getDate() -> str:
    """Takes the 3 letter form of the month the user wishes to model for.

    Returns:
        str: 3 Letter form of the month you wish to model for
    """

    desiredmonth = str(input("Please enter the month you would like to model (Use the 3 letter formse.g. JAN or jan for January)"))
    return desiredmonth


def getDateInt(desiredmonth) -> int:
    """Returns the integer form of the month the user wishes to model

    Args:
        desiredmonth (str): 3 Letter form of the month you wish to model for

    Returns:
        int: Month number for the requested month - 1
    """

    monthDict = {"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7,
                 "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12}

    while desiredmonth.upper() not in monthDict: # While the month entered is not in the dictionary.
        desiredmonth = str(input("Please re-enter the desired month in a 3 letter form (CAPS or no caps are allowed)"))

    return monthDict[desiredmonth] - 1


def getTime() -> int:
    """Requests the 24-hour representation of the hour the user wishes to model.

    Returns:
        int: 24-hour representation of model time - 1
    """

    desiredtime = int(input("Please enter the hour you wish to model (between 1 and 24 inclusive e.g. 13 for 1pm)"))

    while desiredtime > 24 or desiredtime < 1: # If the time entered is bigger than 24 or less than 1, ask for new time
        print("Your selected time does not exist")
        desiredtime = int(input("Please enter the hour you wish to model (between 1 and 24 inclusive e.g. 13 for 1pm)"))       
        
    return desiredtime- 1


def getNoOfWindTurbines() -> tuple:
    """Takse input for the number of wind turbines the user wants to model.

    Returns:
        tuple: tuple of the number of wind turbines and the diameter of the turbines
    """
    desiredwindturb = float(input("Please enter the number of wind turbines you wish to put up"))
    while  desiredwindturb < 0:
        print ("you can't have negative wind turbines")
        desiredwindturb = float(input("Please enter the number of wind turbines you wish to put up"))

    desireddiameter=float(input("What diameter of wind turbine do you wish to model (m)?"))
    return (desiredwindturb, desireddiameter)


def windcalcs(month, desireddiameter, desiredwindturb) -> float:
    """Calculates the power output of the wind turbines

    Args:
        month (int): The month being modeled
        desireddiameter (float): The diameter of the turbines
        desiredwindturb (float): The number of wind turbines to be modeled

    Returns:
        float: Net Power Output of all turbines in `W`
    """

    windeff=windturb[month][1]
    windspeed=windturb[month][0]
    Windpower1=(float(windeff)*0.5*1.3)*(float(windspeed)**(3))*((np.pi)/4)*float(desireddiameter)**2
    netwind=Windpower1*desiredwindturb
    return netwind


if __name__ == "__main__": # Check that the file is being run as a program and not a module.
    desired_month = getDate() # Get the 3-letter month. 
    desired_month_int = getDateInt(desired_month) # Get the integer representation of the month.

    desired_time = getTime() # Get the time to be modeled.

    desired_wind_turb, desired_diameter = getNoOfWindTurbines() # Get the number of wind turbines and their diameter
    net_wind=windcalcs(desired_month_int,desired_diameter,desired_wind_turb) # Calculate the net wind for the given month, number of turbines and their diameter

    print(f"You are creating a graph at {desired_time} {desired_month}, ({desired_month_int})")
    print(f"Net wind: {net_wind}")
    model(desired_month_int, desired_time, 0, desired_wind_turb, 0)