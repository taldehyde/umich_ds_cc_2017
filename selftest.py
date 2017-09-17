from pyAudioAnalysis import audioTrainTest as aT
import os

classes = [ 
        "BassClarinet", "BassTrombone", "BbClarinet", "Cello", "EbClarinet", 
        "Marimba", "TenorTrombone", "Viola", "Violin", "Xylophone"]
test_dir = "selftest_data"
filenames = [name for name in os.listdir(test_dir) if name.endswith('.wav')]

total = len(filenames)
count = 0
for name in filenames:
    result = aT.fileClassification(os.path.join(test_dir, name), "svmModel","svm")
    if name.split('_')[0] == classes[int(result[0])]:
        count += 1

print "{}%".format(float(count)/total*100)
