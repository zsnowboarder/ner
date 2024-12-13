#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install date-spacy


# In[3]:


import spacy
from date_spacy import find_dates

nlp = spacy.load("en_core_web_md")
nlp.add_pipe("find_dates", before="ner")


# In[37]:


text = """On December 10, 2024 at 1200h, Victim John was walking on the street in 300 block Main Street. Suspect Tom assaulted John. Witness Mary (1997/01/01) called police. PC 9204 Dave Thompson arrived and arrested suspect."""

# Process the text
doc = nlp(text)

# Function to redact entities
def replace_entities(doc):
    new_text = text
    prev_ent = ""
    for ent in doc.ents:
        if ent.label_ in ["PERSON"]:
            new_text = new_text.replace(ent.text, f"[{ent.label_}]")
            prev_ent = ent.label_
        elif ent.label_ == "DATE" and prev_ent == "PERSON":
            new_text = new_text.replace(ent.text, f"[{ent.label_}]")
            prev_ent = ent.label_ 
    return new_text

# Replace entities in the text
replaced_text = replace_entities(doc)
#print(replaced_text)


# for ent in doc.ents:
#     print(ent.text, ent.label_)

# In[ ]:




