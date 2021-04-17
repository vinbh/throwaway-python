import shelve,pickle

with  open("/Users/vinayak.bhatt/Downloads/Airplane_Crashes_and_Fatalities_Since_1908.csv") as csv_file:
    csv_dict = pickle.load(csv_file)

for var in csv_dict:
    print(var)
