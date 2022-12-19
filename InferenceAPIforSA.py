import csv
from huggingface_hub.inference_api import InferenceApi

if __name__ == '__main__':
    inference = InferenceApi(repo_id="finiteautomata/bertweet-base-sentiment-analysis",
                             token='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')

    # Open/Create a file to append data
    # csvRead = open('Data files/UATokenizedForSA.csv', 'r')
    # csvFile = open('Data files/UASA.csv', 'a')
    # csvRead = open('Data files/CGPTTokenizedForSA.csv', 'r')
    # csvFile = open('Data files/CGPTSA.csv', 'a')
    csvRead = open('Data files/WCTokenizedForSA.csv', 'r')
    csvFile = open('Data files/WCSA.csv', 'a')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvReader = csv.reader(csvRead)

    count = 1
    for respline in csvReader:
        resp = inference(respline[1])
        csvWriter.writerow([count, resp])
        count = count + 1
