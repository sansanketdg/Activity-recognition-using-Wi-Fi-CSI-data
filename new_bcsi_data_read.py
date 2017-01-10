import matplotlib.pyplot as plt
import pandas as pd
import linecache
import numpy as np
from scipy.fftpack import fft
import scipy
from scipy.signal import hilbert, butter, medfilt, wiener

# import glob
# path = "data_2/position1/subject1/"
#
# files = glob.glob(path + "*.txt")

filename = "data_2/position1/subject1/Falling_4.txt"
data_buffer = []
sample_frequency = float(linecache.getline(filename, 8).split('\t')[1].strip()) # signal frequency  in Hz

with open(filename, 'r') as f:
    data_buffer = pd.read_csv(filename, header=None, skiprows = 15)
    data_buffer.columns = ['values']


print("No of entries are " + str(len(data_buffer)))
print("Sample Frequency is " + str(sample_frequency))

#For File - Falling_1.txt
# i = 2000
# j = 1
# while( i + 18000 < len(data_buffer)):
#     plt.plot(data_buffer[i:i+13000], 'b')
#     plt.savefig(str(j) + "data_bunch.pdf")
#     plt.close()
#     j = j + 1
#     i = i + 18000

# #For File - Falling_5.txt
# i = 8000
# j = 1
# channel = []
# temp = []
# for iii in range(6):
#     channel.append([])

#For File - Falling_3.txt
i = 16000
j = 1
channel = []
temp = []
for iii in range(6):
    channel.append([])

while( i + 18000 < len(data_buffer)):
    six_channel_data = data_buffer[i:i+13000]
    # print(len(six_channel_data))
    plt.plot(six_channel_data, 'b')
    plt.show()
    # plt.savefig(str(j) + "data_bunch.pdf")
    # plt.close()
    j = j + 1
    i = i + 18000
    start = 1000
    for ii in range(6):
        temp.extend(np.asarray(six_channel_data[start:start+1000]))
        channel[ii].extend(np.asarray(six_channel_data[start:start+1000]))
        start = start + 2000

# plt.subplot(511)
# plt.plot(data_buffer[2000:15000], 'b')
# plt.subplot(512)
# plt.plot(data_buffer[20000:33000], 'b')
# plt.subplot(513)
# plt.plot(data_buffer[38000:51000], 'b')

# plt.plot(data_buffer, 'b')
# plt.show()

# print(len(temp))
# print(len(channel[0]))

### Original noisy channel
plt.subplot(311)
plt.title("channel data with noise")
plt.plot(channel[1], 'r')

### hilbert filtering of noisy channel
# analytic_signal = hilbert(channel[1])
# amplitude_envelope = np.abs(analytic_signal)
# plt.subplot(212)
# plt.plot(amplitude_envelope, 'r')
# plt.show()

### fft code
# ts_fourier  = np.fft.rfft(channel[1])
# random_phases = np.exp(np.random.uniform(0,np.pi,len(channel[1])/2+1)*1.0j)
# ts_fourier_new = ts_fourier*random_phases
# #new_ts = np.fft.irfft(ts_fourier_new)
# plt.subplot(212)
# plt.plot(ts_fourier_new, 'r')
# plt.show()

### scikit fft
# yf = fft(channel[1])
yf = scipy.fftpack.fft(channel[1])
plt.subplot(312)
fft_tranformed = 2.0/len(channel[1]) * np.abs(yf[0:int(len(channel[1])/2)])
plt.title("fft of channel data")
plt.plot(fft_tranformed, 'b')
#plt.show()

# ### Medfilt filtering of noist channel
# filtered_out = medfilt(fft_tranformed)
# plt.subplot(313)
# plt.plot(filtered_out, 'b')
# plt.show()

### hilbert filtering of noisy channel
# analytic_signal = hilbert(fft_tranformed)
# amplitude_envelope = np.abs(analytic_signal)
# plt.subplot(313)
# plt.plot(amplitude_envelope, 'b')
# plt.show()

#plt.close()

##### take the fourier transform of the data
# Y = np.fft.fft(data_buffer)/len(data_buffer)
# Y = Y[range(int(len(data_buffer)/2))]
# Y = scipy.fftpack.fft(data_buffer)
#plt.plot(abs(Y), 'r')
#plt.show()

### weiner filtering
#wi = wiener(channel[1], mysize=29, noise=0.5)
wi = wiener(fft_tranformed)
plt.subplot(313)
plt.title("wiener filtered fft data")
plt.plot(wi, 'g')
#plt.legend(loc='best')
plt.subplots_adjust(hspace=.5)
plt.show()

#### medfilt filtering
# t = data_buffer.astype(float)
# medfilt_return = medfilt2d(t)
# plt.plot(medfilt_return, 'b')
# plt.show()

#### hilbert filtering
# hilbert_return = np.real(hilbert(data_buffer))
# plt.plot(hilbert_return, 'y')
# plt.show()