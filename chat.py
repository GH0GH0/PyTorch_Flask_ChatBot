import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

nom_fichier = 'chat.json'


FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Gallic"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])


    return "I do not understand..."



# def stocker_chat(message,reponse):
#     data = {}
#     data['Chat'] = []
#     data['Chat'].append({
#         'message-user': 'message',
#         'reponse': 'reponse'
#     })
   
#     with open(nom_fichier, 'w') as outfile:
#         json.dump(data, outfile, indent=4)
    
#     with open(nom_fichier,'r') as json_file:
   
#     y = {
#         'message-user': message,
#         'reponse': reponse
#         }
  
#     # appending data to emp_details 
#     data['Chat'].append(y)

# def write_json(data,message, filename='chat.json'):
#     with open(filename,'w') as f:
#         json.dump(data, f, indent=4)
      
      
# with open(nom_fichier) as json_file:
#     data = json.load(json_file)
      
#     temp = data['Chat']
  
#     # python object to be appended
#     y = {   "message-user": "message",
#             "reponse": "reponse"
#         }
  
  
#     # appending data to emp_details 
#     temp.append(y)

