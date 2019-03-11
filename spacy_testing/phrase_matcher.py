import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

#### to get start_char & end_char for FSERV
# initialise the Matcher with a vocab.
# the matcher must always share the same vocab with the documents it will operate on
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['personal loan', 'personal financing', 'housing loan', 'car loan', 'home loan', 'islamic personal loan', 'small business loan', 'business loan']
# only run nlp.make_doc(text) to speed things up
pattern = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *pattern)

sentence = "personal loans in Malaysia"

doc = nlp(u"'%s'" %sentence)

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc[start:end]  # the matched span
    # print(match_id, string_id, start, end, span.text, span.start_char, span.end_char)
    print(doc, span.text, span.start_char, span.end_char)

doc1 = nlp(u"'%s'" %sentence)

for ent in doc1.ents:
    print(doc1, ent.text, ent.start_char, ent.end_char, ent.label_)
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