from pyAudioAnalysis import audioFeatureExtraction as aF
import os
import numpy as np
import scipy.io.wavfile as wavfile

stWindow = 500
stStep = 500
mtWindow = 5000
mtStep = 5000

train_data_dir = "train_data"
classes = [ 
        "BassClarinet", "BassTrombone", "BbClarinet", "Cello", "EbClarinet", 
        "Marimba", "TenorTrombone", "Viola", "Violin", "Xylophone"]
filenames = [name for name in os.listdir(train_data_dir) 
        if name.endswith('.wav')]
filenames.sort()
labels = [name.split('_')[0] for name in filenames]
#feature extraction
features = np.array([])
for filename in filenames:
    path = os.path.join(train_data_dir, filename)
    [fs, x] = wavfile.read(path)
    mtFeatures, st = aF.mtFeatureExtraction(x, fs, mtWindow, mtStep, stWindow, stStep)
    feature = np.transpose(mtFeatures).mean(axis=0)
    

print len(features)
#train



