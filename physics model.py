import csv
with open('DATA FOR MODEL.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    pcd = list(reader)

#MODEL OF POWER CONSUMPTION
def powerconsumption(month,time):
  return #whatever we decide the graph to be
print(pcd)
