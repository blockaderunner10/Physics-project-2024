import csv
with open('DATA FOR MODEL.csv', newline='') as csvfile: #Importing our csv of data for model of power consumption
    reader = csv.reader(csvfile, delimiter=',')
    pcd = list(reader)

pcd = [[x[0], float(x[1])] for x in pcd[1:]]#Removing the headings of the csv file
print(pcd)

#MODEL OF POWER CONSUMPTION
def powerconsumption(month,time):
  return #whatever we decide the graph to be
