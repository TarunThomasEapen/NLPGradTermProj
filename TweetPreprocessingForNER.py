import TweetTokenizerForNER as tk
import csv

if __name__ == '__main__':

    # Open/Create a file to append data
    # csvFile = open('UATokenized.csv', 'a')
    # csvRead = open('UnitedAirlinesTweets.csv', 'r')
    # csvFile = open('CGPTTokenized.csv', 'a')
    # csvRead = open('ChatGPTTweets.csv', 'r')
    csvFile = open('Data files/WCTokenized.csv', 'a')
    csvRead = open('Data files/WorldCupTweets.csv', 'r')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvReader = csv.reader(csvRead)

    count = 1
    for line in csvReader:
        print(tk.normalizeTweet(line[1]))
        csvWriter.writerow([count, tk.normalizeTweet(line[1])])
        count = count + 1
