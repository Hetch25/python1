import pandas
data = pandas.read_csv('Proyect2/weather.csv')
print(data)

data_dict = data.to_dict()
print(data_dict)

#to access to a column
data_temp = data['Temp'].to_list()
print(data_temp)
#first way
print(data['Temp'].mean())
#second way
print(sum(data_temp) / len(data_temp))
#find the biggest value in data_temp
print(data['Temp'].max())