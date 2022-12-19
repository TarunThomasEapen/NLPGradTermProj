from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("TweebankNLP/bertweet-tb2_wnut17-ner")

model = AutoModelForTokenClassification.from_pretrained("TweebankNLP/bertweet-tb2_wnut17-ner")


generator = pipeline(task="token-classification", model=model, tokenizer=tokenizer)

print(generator(
    "@USER What are #ElonMusk and #JaredKushner doing together at the #WorldCup ? ? ! !"
))  # doctest: +SKIP
