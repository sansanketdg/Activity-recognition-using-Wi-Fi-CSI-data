import matplotlib.pyplot as plt
import os
import pandas as pd

import glob
path = "data_2/position1/subject1/"
activity = "Falling"

filename = glob.glob(path + "Sitting*.txt")

data_buffer1 = []
data_buffer2 = []
data_buffer3 = []
data_buffer4 = []
data_buffer5 = []


with open(filename[0], 'r') as f:
    data_buffer1 = pd.read_csv(f, header=None, skiprows = 15)
    data_buffer1.columns = ['values']
    data_buffer1 = data_buffer1['values'].values


with open(filename[1], 'r') as f:
    data_buffer2 = pd.read_csv(f, header=None, skiprows = 15)
    data_buffer2.columns = ['values']
    data_buffer2 = data_buffer2['values'].values

with open(filename[2], 'r') as f:
    data_buffer3 = pd.read_csv(f, header=None, skiprows = 15)
    data_buffer3.columns = ['values']
    data_buffer3 = data_buffer3['values'].values

with open(filename[3], 'r') as f:
    data_buffer4 = pd.read_csv(f, header=None, skiprows = 15)
    data_buffer4.columns = ['values']
    data_buffer4 = data_buffer4['values'].values


with open(filename[4], 'r') as f:
    data_buffer5 = pd.read_csv(f, header=None, skiprows = 15)
    data_buffer5.columns = ['values']
    data_buffer5 = data_buffer5['values'].values

#Declare an empty six-channel-dataset-array
six_channel_data = []

### For File - Sitting_1.txt
START = 2000
SIZE_OF_6CHANNEL_SET = 13000
SILENT = 5000   # Area between 2 6channel data sets in graph
FILE1_DATA_SIZE = len(data_buffer1)

while( START + (SIZE_OF_6CHANNEL_SET + SILENT) < FILE1_DATA_SIZE):
    sample = data_buffer1[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)]
    # plt.plot(sample, 'b')
    # plt.show()
    six_channel_data.extend(data_buffer1[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)])
    START = START + (SIZE_OF_6CHANNEL_SET + SILENT)

print(len(six_channel_data))
df = pd.DataFrame(six_channel_data, columns=["column"])
#csv_filename = "6_channel_data_" + activity + ".csv"
csv_filename = filename[1].strip(".txt") + "_parse_output.csv"
df.to_csv(csv_filename, index=False)

six_channel_data = []

### For File - Sitting_2.txt
START = 11000
SIZE_OF_6CHANNEL_SET = 13000
SILENT = 5000   # Area between 2 6channel data sets in graph
FILE2_DATA_SIZE = len(data_buffer2)

while( START + (SIZE_OF_6CHANNEL_SET + SILENT) < FILE2_DATA_SIZE):
    sample = data_buffer2[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)]
    plt.plot(sample, 'b')
    plt.show()
    six_channel_data.extend(data_buffer2[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)])
    START = START + (SIZE_OF_6CHANNEL_SET + SILENT)

print(len(six_channel_data))
df = pd.DataFrame(six_channel_data, columns=["column"])
#csv_filename = "6_channel_data_" + activity + ".csv"
csv_filename = filename[1].strip(".txt") + "_parse_output.csv"
df.to_csv(csv_filename, index=False)

six_channel_data = []


# df = pd.DataFrame(six_channel_data, columns=["column"])
# #csv_filename = "6_channel_data_" + activity + ".csv"
# csv_filename = filename[0].strip(".txt") + "_parse_output.csv"
# df.to_csv(csv_filename, index=False)
#
# six_channel_data = []
#
# ### For File - Falling_2.txt
# START = 2500
# SIZE_OF_6CHANNEL_SET = 13000
# SILENT = 5000  # Area between 2 6channel data sets in graph
# FILE2_DATA_SIZE = len(data_buffer2)
#
# while( START + (SIZE_OF_6CHANNEL_SET + SILENT) < FILE2_DATA_SIZE):
#     six_channel_data.extend(data_buffer2[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)])
#     START = START + (SIZE_OF_6CHANNEL_SET + SILENT)
#
# print(len(six_channel_data))
#
# df = pd.DataFrame(six_channel_data, columns=["column"])
# #csv_filename = "6_channel_data_" + activity + ".csv"
# csv_filename = filename[1].strip("Falling*.txt") + "_parse_output.csv"
# df.to_csv(csv_filename, index=False)
#
# six_channel_data = []
#
# ### For File - Falling_3.txt
# START = 15000
# SIZE_OF_6CHANNEL_SET = 13000
# SILENT = 5000  # Area between 2 6channel data sets in graph
# FILE3_DATA_SIZE = len(data_buffer3)
#
# while( START + (SIZE_OF_6CHANNEL_SET + SILENT) < FILE3_DATA_SIZE):
#     six_channel_data.extend(data_buffer3[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)])
#     START = START + (SIZE_OF_6CHANNEL_SET + SILENT)
#
# print(len(six_channel_data))
#
# df = pd.DataFrame(six_channel_data, columns=["column"])
# #csv_filename = "6_channel_data_" + activity + ".csv"
# csv_filename = filename[2].strip(".txt") + "_parse_output.csv"
# df.to_csv(csv_filename, index=False)
#
# six_channel_data = []
#
# ### For File - Falling_4.txt
# START = 16000
# SIZE_OF_6CHANNEL_SET = 13000
# SILENT = 5000  # Area between 2 6channel data sets in graph
# FILE4_DATA_SIZE = len(data_buffer4)
#
# while( START + (SIZE_OF_6CHANNEL_SET + SILENT) < FILE4_DATA_SIZE):
#     six_channel_data.extend(data_buffer4[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)])
#     START = START + (SIZE_OF_6CHANNEL_SET + SILENT)
#
# print(len(six_channel_data))
#
# df = pd.DataFrame(six_channel_data, columns=["column"])
# #csv_filename = "6_channel_data_" + activity + ".csv"
# csv_filename = filename[3].strip(".txt") + "_parse_output.csv"
# df.to_csv(csv_filename, index=False)
#
# six_channel_data = []
#
# ### For File - Falling_5.txt
# START = 8000
# SIZE_OF_6CHANNEL_SET = 13000
# SILENT = 5000  # Area between 2 6channel data sets in graph
# FILE5_DATA_SIZE = len(data_buffer5)
#
# while( START + (SIZE_OF_6CHANNEL_SET + SILENT) < FILE5_DATA_SIZE):
#     six_channel_data.extend(data_buffer5[START:(START + SIZE_OF_6CHANNEL_SET + SILENT)])
#     START = START + (SIZE_OF_6CHANNEL_SET + SILENT)
#
# print(len(six_channel_data))
#
# df = pd.DataFrame(six_channel_data, columns=["column"])
# #csv_filename = "6_channel_data_" + activity + ".csv"
# csv_filename = filename[4].strip(".txt") + "_parse_output.csv"
# df.to_csv(csv_filename, index=False)
#
# six_channel_data = []