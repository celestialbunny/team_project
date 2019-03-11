import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

#### to get start_char & end_char for FSERV
# initialise the Matcher with a vocab.
# the matcher must always share the same vocab with the documents it will operate on
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['personal loan', 'personal financing', 'housing loan', 'car loan', 'home loan', 'islamic personal loan', 'small business loan', 'business loan']

# terminology_list = [
#     'personal loan',
#     'Personal Loan',
#     'Personal loans',
#     'Personal Loans',
#     'personal loans',
#     'personal financing',
#     'Personal financing',
#     'Personal Financing',
#     'housing loan',
#     'housing loans',
#     'Housing Loan',
#     'Housing Loans',
#     'home loan',
#     'home loans',
#     'Home loan',
#     'Home Loan',
#     'Home Loans',
#     'property loan',
#     'property loans',
#     'Property Loan',
#     'Property Loans',
#     'car loan',
#     'car loans',
#     'Car Loan',
#     'Car Loans',
#     'Car financing',
#     'islamic personal loan',
#     'islamic personal loans',
#     'Islamic Personal Loan',
#     'Islamic Personal Loans',
#     'Islamic Financing Loan',
#     'Islamic Financing Loans',
#     'Islamic Loans',
#     'Islamic loans',
#     'Islamic loan',
#     'Islamic Loan',
#     'small business loan',
#     'small business loans',
#     'Small Business Loan',
#     'Small Business Loans',
#     'business loan',
#     'business loans',
#     'Business Loan',
#     'Business Loans',
#     ]

sentence = "AEON i-Cash Personal Financing has approved financing amount of up to RM 100,000 and interest rates as low as 0.66% per month."

doc = nlp(u"'%s'" %sentence)
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc[start:end]  # the matched span
    # print(match_id, string_id, start, end, span.text, span.start_char, span.end_char)
    print(doc, span.text, span.start_char, span.end_char)

doc1 = nlp(u"'%s'" %sentence)

for ent in doc1.ents:
    print(doc, ent.text, ent.start_char, ent.end_char, ent.label_)

# ---------------------------------------------------------------------------------------------
# matcher = Matcher(nlp.vocab)
# # add match ID "HelloWorld" with no callback and one pattern
# pattern = [{'LOWER': 'google'}, {'IS_PUNCT': True}, {'LOWER': 'world'}]
# matcher.add('HelloWorld', None, pattern)
# ​
# doc = nlp(u'Hello, world! Hello world!')
# matches = matcher(doc)
# for match_id, start, end in matches:
#     string_id = nlp.vocab.strings[match_id]  # get string representation
#     span = doc[start:end]  # the matched span
#     print(match_id, string_id, start, end, span.text)

# nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

# for ent in doc.ents:
#     print(doc, ent.text, ent.start_char, ent.end_char, ent.label_)