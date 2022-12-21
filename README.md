# NLPGradTermProj

TweetCollector.py - Tweet collection logic using Tweepy

TweetNormalizerForNER.py - Tweet Normalisation method taken from NER model github page
TweetPreprocessingForNER.py - Preprocess collected tweets using the previous python file

TweetNormalizerForSA.py - Tweet Normalisation method taken from Sentiment Analysis model github page
TweetPreprocessingForSA.py - Preprocess collected tweets using the previous python file

NER.py - deploying the NER model using the HuggingFace's Transformer package

InferenceAPIForNER.py - Extracting named entities using HuggingFace's Inference API for the NER model
InferenceAPIForSA.py - Extracting sentiment analysis using HuggingFace's Inference API for the SA model

Folder - Stanford Stanza Implementation
StanzaImpl.py - Stanza's NER and SA models are deployed and results extracted

Folder - Data files. Contains the Tweets and Results
UnitedAirlinesTweets.csv - Tweets collected for #UnitedAirlines
UATokenized.csv - Tweets preprocessed for NER
UATokenizedForSA.csv - Tweets preprocessed for SA
UANER.csv - Reults from NER
UASA.csv - Results from Sentiment Analysis

ChatGPTTweets.csv - Tweets collected for #ChatGPT
CGPTTokenized.csv - Tweets preprocessed for NER
CGPTTokenizedForSA.csv - Tweets preprocessed for SA
CGPTNER.csv - Reults from NER
CGPTSA.csv - Results from Sentiment Analysis

WorldCupTweets.csv - Tweets collected for #WorldCup
WCTokenized.csv - Tweets preprocessed for NER
WCTokenizedForSA.csv - Tweets preprocessed for SA
WCNER.csv - Reults from NER
WCSA.csv - Results from Sentiment Analysis

Folder Data files/Stanza Results of the evaluation pipeline
For #UnitedAirlines tweets
UANER.csv - Reults from NER
UASA.csv - Results from Sentiment Analysis

For #ChatGPT tweets
CGPTNER.csv - Reults from NER
CGPTSA.csv - Results from Sentiment Analysis

For #WorldCup tweets
WCNER.csv - Reults from NER
WCSA.csv - Results from Sentiment Analysis
