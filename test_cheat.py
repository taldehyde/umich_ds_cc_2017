from pyAudioAnalysis import audioTrainTest as aT
import os

classes = [ 
        "BassClarinet", "BassTrombone", "BbClarinet", "Cello", "EbClarinet", 
        "Marimba", "TenorTrombone", "Viola", "Violin", "Xylophone"]
test_dir = "test_data"
filenames = [name for name in os.listdir(test_dir) if name.endswith('.wav')]

for name in filenames:
    result = aT.fileClassification(os.path.join(test_dir, name), "svmModel","svm")
    print "{},{}".format(name, classes[int(result[0])]) 
