import linecache
import pandas as pd
import matplotlib.pyplot as plt

filename = "data_2/position1/subject1/Sitting_3.txt"
data_buffer = []
sample_frequency = float(linecache.getline(filename, 8).split('\t')[1].strip()) # signal frequency  in Hz

with open(filename, 'r') as f:
    data_buffer = pd.read_csv(filename, header=None, skiprows = 15)
    data_buffer.columns = ['values']

print("No of entries are " + str(len(data_buffer)))
print("Sample Frequency is " + str(sample_frequency))

plt.plot(data_buffer, 'b')
plt.show()