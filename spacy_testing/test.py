import spacy
input_dir = "C:\\Users\\User\\Desktop\\Back_end\\spacy_testing\\brain_testing"
nlp = spacy.load(input_dir)

sentences =[
    "They are considering to get a JCL Personal loan",
    "Islamic personal loan",
    "Apple is looking at buying U.K. startup for $1 billion",
    "Compare Malaysian housing loans with our housing loan calculator.",
    "for a new mortgage loan or refinance your mortgage with Citibank's competitive mortgage loan",
    "Donald John Trump (born June 14, 1946) is the 45th and current president of the United States.",
    "Get the latest news, updates, and happenings at Google.",
    # "Singapore officially the Republic of Singapore is an island city-state in Southeast Asia.",
    ]



# doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for s in sentences:
    print(s)
    doc = nlp(u"'%s'" %s)
# 
# for s in sentences:
#     # doc = nlp(u'(s for s in sentences)')
#     doc = nlp(u's')
#     print(doc)


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
