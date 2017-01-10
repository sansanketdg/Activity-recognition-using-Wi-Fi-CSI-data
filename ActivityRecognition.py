import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

temp = pd.read_csv("data/trial1.csv")
channel1_receiver2 = temp.ix[:, 30:31]
#plt.plot(channel1_receiver2, 'r')
channel1_receiver3 = temp.ix[:, 60:61]


#plt.plot(channel1_receiver3, 'b')
#channel1_receiver2
# First, design the Buterworth filter
# N = 15  # Filter order
# Wn = 0.01  # Cutoff frequency
# B, A = signal.butter(N, Wn, output='ba')
#
# # Second, apply the filter
# tempf = signal.filtfilt(B, A, channel1_receiver2)
#
# # Make plots
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# plt.plot(channel1_receiver2, 'b-')
# plt.plot(tempf, 'r-',linewidth=2)
#plt.show()