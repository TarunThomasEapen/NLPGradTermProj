import csv
from huggingface_hub.inference_api import InferenceApi

if __name__ == '__main__':
    inference = InferenceApi(repo_id="TweebankNLP/bertweet-tb2_wnut17-ner",
                             token='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')

    # Open/Create a file to append data
    # csvRead = open('Data files/UATokenized.csv', 'r')
    # csvFile = open('Data files/UANER.csv', 'a')
    # csvRead = open('Data files/CGPTTokenized.csv', 'r')
    # csvFile = open('Data files/CGPTNER.csv', 'a')
    csvRead = open('Data files/WCTokenized.csv', 'r')
    csvFile = open('Data files/WCNER.csv', 'a')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvReader = csv.reader(csvRead)

    count = 1
    for respline in csvReader:
        resp = inference(respline[1])
        for line in resp:
            print(line['word'])
            csvWriter.writerow([count, line['word']])
        count = count + 1
