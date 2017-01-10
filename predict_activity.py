from sklearn.externals import joblib
import pandas as pd
import time
import os
import pygame
from pygame import mixer
from collections import Counter
import sched, time
s = sched.scheduler(time.time, time.sleep)

clf = joblib.load('activity_recognizer_model.pkl')
last_revision = 'temp string during start of the program'

def getActivityName(predicted_out):
    count = 0
    total = 0
    most_common, count = Counter(predicted_out.iloc[:, 0]).most_common(1)[0]
    #print(most_common)
    #print(count)
    total = len(predicted_out.iloc[:, 0])
    print(total)

    if(count/total > 0.5):
        try:
            mixer.init()
            #volume = pygame.mixer.music.get_volume()
            volume = 1.0
            pygame.mixer.music.set_volume(volume)
            if(most_common == 1):
                mixer.music.load('audio/falling.wav')
                print("Falling activity detected")
            elif(most_common == 2):
                mixer.music.load('audio/running_on_path.wav')
                print("Running on path activity detected")
            elif(most_common == 3):
                mixer.music.load('audio/running_on_spot.wav')
                print("Running on the spot activity detected")
            elif(most_common == 4):
                mixer.music.load('audio/sitting.wav')
                print("Sitting activity detected")
            elif(most_common == 5):
                mixer.music.load('audio/sitting_down.wav')
                print("Sitting down on floor activity detected")
            elif(most_common == 6):
                mixer.music.load('audio/standing.wav')
                print("Standing activity detected")
            else:
                print("couldnt predict")
                mixer.music.load('audio/falling.wav')
            mixer.music.play()
            time.sleep(3)
        except pygame.error:
            print("Error to user pygame mixer")

    else:
        print("No Falling activity")

def getLastRevisionLine():
    input = "revision.csv"
    with open(input, 'rb') as fh:
        first = next(fh).decode()

        fh.seek(-1024, 2)
        last = fh.readlines()[-1].decode()
    return last

def predict_activity(sc):
    global last_revision
    sample_test = pd.DataFrame()
    print("------------------------------")
    print("Inside predict activities")
    os.system('gdrive revision list 0B7IDjH2Kr7A-OHloUHgyaEFrdmc > revision.csv')
    with open('revision.csv', 'r') as f:
        ## read last line of the revision list output saved in revision.csv file
        text1 = getLastRevisionLine()
        ## extract the revision-id
        revision_id = text1.split(" ")
        print("Revision id for file - " + revision_id[0])
    if(last_revision != revision_id[0]):
        last_revision = revision_id[0]
        os.system('gdrive revision download --force 0B7IDjH2Kr7A-OHloUHgyaEFrdmc ' + revision_id[0])
        #os.system('gdrive download --force 0B7IDjH2Kr7A-OHloUHgyaEFrdmc')

        test_sample = pd.read_csv('sample_data.csv', header = None, sep=',')

        sample_test = sample_test.append(test_sample)
        predicted_out = pd.DataFrame(clf.predict(sample_test.iloc[:, 1:]))
        # test_sample['predicted_output'] = predicted_out
        # test_sample.to_csv("temp.csv", sep=',')
        getActivityName(predicted_out)
    else:
        print("No change in file...waiting for 10 sec to check again!")
    s.enter(10, 1, predict_activity, (sc,))

s = sched.scheduler(time.time, time.sleep)
s.enter(1, 1, predict_activity, (s,))
s.run()