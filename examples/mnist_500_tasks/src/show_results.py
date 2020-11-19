import os
import csv
import time
import argparse
# import matplotlib.pyplot as plt

def summary(filepath, result_path):
    with open(filepath, 'r') as f:
        csv_read = csv.reader(f)
        with open(result_path, 'a') as r:
            csv_write = csv.writer(r)
            for line in csv_read:
                csv_write.writerow(line)

def main():
    parser = argparse.ArgumentParser(description='Display Results')
    parser.add_argument('--number', type=int, default=500, 
                        help='The number of learning rates')
    args = parser.parse_args()
    
    path = '.'
    # Waiting for all results
    while(len([lists for lists in os.listdir(path)]) <= args.number):
        time.sleep(1)

    result_path = './result/'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath) and file[:-4]=='.csv':
            summary(filepath, os.path.join(result_path, 'results.csv'))


if __name__ == '__main__':
    main()
