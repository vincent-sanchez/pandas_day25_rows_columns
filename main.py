import pandas

# Import data into Pandas dataframe
data = pandas.read_csv("weather_data.csv")

# Create dictionary
data_dict = data.to_dict()
#print(data_dict)

# Create list
temp_list = data["temp"].to_list()
#print(len(temp_list))

# Average Method 1: Using for loop to aggregate and calculate.
num = 0
den = len(temp_list)
for item in temp_list:
    num = num+item
avg = num/den

print("Average Method 1: For Loop")
print("-----------------------")
print("Numerator: " + str(num))
print("Denominator: " + str(den))
print("Average: " + str(avg))
print("\n")

# Average Method 2: Using Python native sum() function.
num = sum(temp_list)
den = len(temp_list)
avg = num/den

print("Average Method 2: Python Native Sum Function")
print("-----------------------")
print("Numerator: " + str(num))
print("Denominator: " + str(den))
print("Average: " + str(avg))
print("\n")

# Average Method 3: Using Pandas native avg() function.
num = data["temp"].sum()
den = len(temp_list)
avg = data["temp"].mean()

print("Average Method 3: Pandas Average")
print("-----------------------")
print("Numerator: " + str(num))
print("Denominator: " + str(den))
print("Average: " + str(avg))
print("\n")

# Max Method 1: Using Pandas max() funciton.
print("Max Method 1: Pandas max()")
print("-----------------------")
print("Max: " + str(data["temp"].max()))
print("\n")

# Get Max Temp Day: Using Pandas
print("Get Max Temp Day")
print("-----------------------")
print(data[data["temp"] == data["temp"].max()]["day"])
print("\n")

# Get Monday's Temp in Farenheit: Using Pandas
print("Get Monday's Temp in Farenheit")
print("-----------------------")
print((data[data["day"]=="Monday"]["temp"]*1.8)+32)
print("\n")