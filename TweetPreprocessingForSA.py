import TweetPrePrepForSA as SA
import csv

if __name__ == '__main__':
    # print(SA.preprocess_tweet("@perezjotaeme debería cambiar esto http://bit.ly/sarasa"))

    # Open/Create a file to append data
    # csvFile = open('Data files/UATokenizedForSA.csv', 'a')
    # csvRead = open('Data files/UnitedAirlinesTweets.csv', 'r')
    # csvFile = open('Data files/CGPTTokenizedForSA.csv', 'a')
    # csvRead = open('Data files/ChatGPTTweets.csv', 'r')
    csvFile = open('Data files/WCTokenizedForSA.csv', 'a')
    csvRead = open('Data files/WorldCupTweets.csv', 'r')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvReader = csv.reader(csvRead)

    count = 1
    for line in csvReader:
        print(SA.preprocess_tweet(line[1]))
        csvWriter.writerow([count, SA.preprocess_tweet(line[1])])
        count = count + 1
