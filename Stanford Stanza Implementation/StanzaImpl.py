import csv

import stanza

if __name__ == '__main__':

    nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
    nlp1 = stanza.Pipeline(lang='en', processors='tokenize,sentiment', tokenize_no_ssplit=True)

    # Open/Create a file to append data
    # csvRead = open('../Data files/UnitedAirlinesTweets.csv', 'r')
    # csvFile = open('../Data files/Stanza/UANER.csv', 'a')
    # csvFile2 = open('../Data files/Stanza/UASA.csv', 'a')
    # csvRead = open('../Data files/ChatGPTTweets.csv', 'r')
    # csvFile = open('../Data files/Stanza/CGPTNER.csv', 'a')
    # csvFile2 = open('../Data files/Stanza/CGPTSA.csv', 'a')
    csvRead = open('../Data files/WorldCupTweets.csv', 'r')
    csvFile = open('../Data files/Stanza/WCNER.csv', 'a')
    csvFile2 = open('../Data files/Stanza/WCSA.csv', 'a')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvWriter2 = csv.writer(csvFile2)
    csvReader = csv.reader(csvRead)

    count = 1
    for respline in csvReader:
        doc = nlp(respline[1])
        for sent in doc.sentences:
            for ent in sent.ents:
                csvWriter.writerow([count, "entity: " + ent.text + "\ttype: " + ent.type])

        doc1 = nlp1(respline[1])
        for i, sentence in enumerate(doc1.sentences):
            csvWriter2.writerow([count, "%d -> %d" % (i, sentence.sentiment)])
        count = count + 1





