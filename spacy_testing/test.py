import spacy
input_dir = "C:\\next\\python\\brain5_20"
nlp = spacy.load(input_dir)

sentences =[
    "They are considering to get a JCL Personal loan",
    "personal loan, car loan, house loan, personal financing, business loan",
    "personal loans, car loans, house loans, housing loans, personal financings, business loan",
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
    # print(s)
    doc = nlp(u"'%s'" %s)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
# 
# for s in sentences:
#     # doc = nlp(u'(s for s in sentences)')
#     doc = nlp(u's')
#     print(doc)


