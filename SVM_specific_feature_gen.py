import pandas as pd
import numpy as np
import glob

path = "data_2/position1/subject1/"
filename = glob.glob(path + "*_get_channel_output.csv")

for each_file in filename:

    with open(each_file, 'r') as f:
        data_buffer1 = pd.read_csv(f, header=None, skiprows = 1)

    data_buffer1.columns = ["ch1_feature", "ch2_feature", "ch3_feature", "ch4_feature", "ch5_feature", "ch6_feature", "DC_feature"]
    #data_buffer1 = data_buffer1['values'].values
    channel1_features = data_buffer1['ch1_feature'].values
    channel2_features = data_buffer1['ch2_feature'].values
    channel3_features = data_buffer1['ch3_feature'].values
    channel4_features = data_buffer1['ch4_feature'].values
    channel5_features = data_buffer1['ch5_feature'].values
    channel6_features = data_buffer1['ch6_feature'].values
    DC_feature = data_buffer1['DC_feature'].values

    LEN = len(channel1_features)
    CH1_ = []
    CH2_ = []
    CH3_ = []
    CH4_ = []
    CH5_ = []
    CH6_ = []
    DC_ = []
    for i in range(0, 10):

        DC_.append(int(float(DC_feature[i].strip("[]"))))
        CH1_.append(int(channel1_features[i].strip("[]").split(',')[3]) - int(channel1_features[i].strip("[]").split(',')[2]))
        CH2_.append(int(channel2_features[i].strip("[]").split(',')[3]) - int(channel2_features[i].strip("[]").split(',')[2]))
        CH3_.append(int(channel3_features[i].strip("[]").split(',')[3]) - int(channel3_features[i].strip("[]").split(',')[2]))
        CH4_.append(int(channel4_features[i].strip("[]").split(',')[3]) - int(channel4_features[i].strip("[]").split(',')[2]))
        CH5_.append(int(channel5_features[i].strip("[]").split(',')[3]) - int(channel5_features[i].strip("[]").split(',')[2]))
        ## No need to take care of 6th channel missing as already its default value will be 0
        CH6_.append(int(channel6_features[i].strip("[]").split(',')[3]) - int(channel6_features[i].strip("[]").split(',')[2]))
    # print(DC_)
    # print(CH1_)
    # print(CH2_)
    # print(CH3_)
    # print(CH4_)
    # print(CH5_)
    # print(CH6_)
    print(len(DC_))
    #print(len(CH1_))
    SVM_FEATURES = np.concatenate((DC_,  CH1_, CH2_, CH3_, CH4_, CH5_, CH6_))
    print(len(SVM_FEATURES))
    #print(SVM_FEATURES)

    #list_svm_features = SVM_FEATURES.tolist()
    df = pd.DataFrame(SVM_FEATURES, columns=["features"])
    csv_filename = each_file.strip("_get_channel_output.csv") + "_SVM_features.csv"
    df.to_csv(csv_filename, index=False)


