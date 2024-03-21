print ("test")
import csv
with open('DATAFORMODEL.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pcd = list(reader)

#MODEL OF POWER CONSUMPTION
def powerconsumption(month,time):
  return #whatever we decide the graph to be
