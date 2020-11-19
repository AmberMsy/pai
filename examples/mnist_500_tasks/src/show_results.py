import os
import csv
import time
import argparse
import shutil
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def summary(filepath, result_path):
    with open(filepath, 'r') as f:
        csv_read = csv.reader(f)
        with open(result_path, 'a') as r:
            csv_write = csv.writer(r)
            for line in csv_read:
                csv_write.writerow(line)

def draw(file):
    print("Start Draw")
    results = np.genfromtxt(file, delimiter=",", names=["LR","ACC"])
    # pd.read_csv(file)
    plt.plot(results["LR"], results["ACC"])
    plt.savefig('eva.png')
    # plt.show()


def main():
    parser = argparse.ArgumentParser(description='Display Results')
    parser.add_argument('--number', type=int, default=500, 
                        help='The number of learning rates')
    args = parser.parse_args()
    
    path = './data/'
    if not os.path.exists(path):
        os.makedirs(path)
    # Waiting for all results
    while(len([lists for lists in os.listdir(path)]) < args.number):
        for file in os.listdir('.'):
            if file[-4:]=='.csv':
                shutil.move(file, os.path.join(path, file))
        time.sleep(1)
    for file in os.listdir('.'):
        if file[-4:]=='.csv':
            shutil.move(file, os.path.join(path, file))

    result_path = './result/'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath) and file[-4:]=='.csv':
            summary(filepath, os.path.join(result_path, 'results.csv'))

    draw(os.path.join(result_path, "results.csv"))


if __name__ == '__main__':
    main()
