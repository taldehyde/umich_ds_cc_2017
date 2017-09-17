from pyAudioAnalysis import audioTrainTest as aT
import os

train_dir = 'train_data'

dir_names = [os.path.join(train_dir, name) for name in os.listdir(train_dir) if
        os.path.isdir(os.path.join(train_dir, name))]

print dir_names

aT.featureAndTrain(dir_names, 0.5, 0.5, aT.shortTermWindow, aT.shortTermStep,
        "svm", "svmCheat", False)
