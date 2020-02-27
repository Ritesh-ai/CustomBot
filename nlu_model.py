import os
import json
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig      # It not takes the path of the File instead it needs the Json file itself to run the code.
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, config, model_dir):
    """
    data      = The data used for the training of the model. 
    config    = Configuration file used for the training the data.
    model_dir = Directory where we are going to save our model after it got trained.

    """
    # Read the config_spacy.json as JSON 
    with open(config) as f: config = json.load(f)

    training_data = load_data(data)
    trainer = Trainer(RasaNLUModelConfig(config))
    trainer.train(training_data)

    model_directory = trainer.persist(model_dir, fixed_model_name= "weathernlu")


def run_nlu(config):
    # Read the config_spacy.json as JSON 
    with open(config) as f: config = json.load(f)

    interpreter = Interpreter.load('./models/nlu/default/weathernlu')
    
    print(interpreter.parse("I am planning my holiday to India. I wonder what is the weather out there."))

if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    run_nlu('config_spacy.json')