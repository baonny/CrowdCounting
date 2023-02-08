import pandas as pd, numpy as np
import matplotlib.pyplot as plt

def generatelist(raw):
    int_list = []
    string_list = raw.split('\n')
    for num in string_list:
        if num != '':
            int_list.append(int(num))
    return int_list

def generateResults(numList, frames, fileExt):
    if fileExt in ['mp4', 'avi', 'mov']:

        avgPeople = round(np.average(numList),2)

        df = pd.DataFrame(numList)
        rolling20 = df.rolling(round(frames/20)).mean()
        
        plt.plot(range(len(rolling20)), rolling20)
        plt.xlabel("Frame")
        plt.ylabel("# of People")
        plt.title("Average People over Time: " + str(avgPeople))

        file_path = "result.png"
        plt.savefig(file_path)
        return None
    else:
        return numList[0]
    


