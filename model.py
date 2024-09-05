
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F


model_path = "./local_model/"

model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

def predict_text(text):
    try:
        # tokenize text
        input = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length")
        
        # predict human/ai
        with torch.no_grad():
            output = model(**input)

        logit = output.logits
        
        prediction = logit.argmax().item()
        probabilities = F.softmax(logit, dim=1)
        score = probabilities[0][prediction].item()

        return prediction, score
    
    except Exception as e:
        return "Error {e}"




if __name__  == "__main__":

    text = """
    The earth and moon are celestial bodies that orbits around the sun. what constitutes the planetary revolutions and such. i want to go home and see if the text is human or ai. what can i do for my life? what is in it for me?
    """

    pred, score = predict_text(text)  
    score = round(score * 100, 2)
    print(pred, score)

