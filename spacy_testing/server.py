from __future__ import unicode_literals, print_function
import json
import spacy
import plac # wrapper over argparse
import random
from pathlib import Path
# from tqdm import tqdm #loading bar
from spacy.util import minibatch, compounding
from training_data import TRAIN_DATA

nlp1 = spacy.load('en_core_web_sm')
# Add entity recognizer to model if it's not in the pipeline
# new entity label = 'FSERV' stands for financial services
LABEL = 'FSERV'

# with open("hi.json", "r") as file:
#     TRAIN_DATA = file.read()

@plac.annotations(
    model=("en_core_web_sm", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("C:\\next\\python\\brain5_20", "option", "o", Path),
    n_iter=(20, "option", "n", int))

# def main(model=None, new_model_name='fserv', output_dir=None, n_iter=10):
def main(model="en_core_web_sm", new_model_name='fserv', output_dir="C:\\next\\python\\brain5_20", n_iter=20):
    # """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')
    
    ner.add_label(LABEL)   # add new entity label to entity recognizer
    if model is None:
        optimizer = nlp.begin_training()
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.25,
                           losses=losses)
            print('Losses', losses)

    # test the trained model
    test_text = 'RHB Easy-Pinjaman Ekspres, JCL Personal loan, AEON i-Cash Personal Financing are some examples of personal loans available in Malaysia.'
    test_text = test_text.lower()
    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)
        print("a", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)

if __name__ == '__main__':
    plac.call(main)


