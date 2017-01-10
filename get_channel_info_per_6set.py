import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

DEBUG = 1
activity = "Falling"

path = "data_2/position1/subject1/"
filename = glob.glob(path + "*_parse_output.csv")

current_file = filename[4]

with open(current_file, 'r') as f:
    data_buffer1 = pd.read_csv(f, header=None, skiprows = 1)
data_buffer1.columns = ['values']
data_buffer1 = data_buffer1['values'].values

print(data_buffer1[0:10])
print(len(data_buffer1))

LENGTH = len(data_buffer1)

PHASE = 1100
SILENT = 1000
PERIOD = 18000
INIT_THRESH = 8
MAX_THRESH = 14
START = 1
SHIFT = 200

n = 0
ALL_CHANNELS_FEATURES = []
while (n < LENGTH):
    ## Extract every 6channel set to process
    sample_set_of_6CH = data_buffer1[n:n+18000]
    LEN = len(sample_set_of_6CH)
    print(LEN)
    #sample_ = np.zeros(LEN, 1)
    sample_ = np.zeros((LEN,), dtype=np.int)
    n = n + 18000

    THRESH = INIT_THRESH

    while THRESH < MAX_THRESH:

        ## Max/Min/DC(median) in the entire 6channel set
        max_ = max(sample_set_of_6CH)
        min_ = min(sample_set_of_6CH)
        DC = np.median(sample_set_of_6CH)

        ## Find 6 channels
        for nn in range(0, len(sample_set_of_6CH)-1):
            if(abs(sample_set_of_6CH[nn] - sample_set_of_6CH[nn + 1]) > THRESH):
                sample_[nn] = 1;


        channels = np.zeros((6,4), dtype=np.int)

        k = 0
        channel_count = 0
        while (k < PERIOD):
            if(sample_[k] == 1 and channel_count < 6):
                single_channel = sample_set_of_6CH[k + SHIFT: k + PHASE - SHIFT]
                channels[channel_count][0] = k + SHIFT
                channels[channel_count][1] = k + PHASE-SHIFT;
                channels[channel_count][2] = min(single_channel)
                channels[channel_count][3] = max(single_channel)
                channel_count = channel_count + 1
                k = k + PHASE + SILENT
            else:
                k = k + 1
        if(channel_count == 6):
            break
        else:
            THRESH = THRESH + 1

    if (DEBUG == 1):
        plt.plot(sample_)
        plt.show()

        plt.plot(sample_set_of_6CH)
        DC_list = np.full((LEN, 1), DC).tolist()
        plt.plot(range(0,LEN), DC_list, 'r-')
        for rr in range(0, 6):
            plt.plot([channels[rr][0], channels[rr][1]], [channels[rr][2], channels[rr][3]])
        plt.show()

    channels_list = channels.tolist()
    channels_list.append([DC])
    ALL_CHANNELS_FEATURES.extend([channels_list])


print(ALL_CHANNELS_FEATURES[0])
print(len(ALL_CHANNELS_FEATURES))

df = pd.DataFrame(ALL_CHANNELS_FEATURES, columns=["ch1_feature", "ch2_feature", "ch3_feature", "ch4_feature", "ch5_feature", "ch6_feature", "DC_feature"])
csv_filename = current_file.strip("_parse_output.csv") + "_get_channel_output.csv"
df.to_csv(csv_filename, index=False)

