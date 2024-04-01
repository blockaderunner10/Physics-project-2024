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

print(energyperday)
energypermonth=np.zeros((12,1))
for i in range (12):
    energypermonth[i][0]=float(energyperday[i][1])*float(daysinmonth[i][1])

months=['January','Febuary','March','April','May','june','july','august','september','october','november','December']
for i in range (0,11):
    plt.bar(months[i], energypermonth[i],color='green')
plt.xlabel('Months')
plt.ylabel('Energy consumption (kWh)')
plt.title('Energy consumed per month over a year')
plt.tick_params(axis='both', which='major', labelsize=6)
plt.show()
