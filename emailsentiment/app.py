# from crypt import methods
import pickle
# from turtle import title
# from urllib import request
from keras_preprocessing.sequence import pad_sequences
import re
import spacy
from nlppreprocess import NLP
# from flask import Flask, render_template, request
# import os
# import json


# app = Flask(__name__)

split_strings_days = ["On Mon", "On Tue", "On Wed", "On Thur", "On Fri", "On Sat", "On Sun"]
split_strings_months = ["On Jan", "On Feb", "On Mar", "On Apr", "On May", "On June", "On July", "On Aug", "On Sept", "On Oct", "On Nov", "On Dec"]


nlp = NLP(
       replace_words=True,
       remove_stopwords=True,
       remove_numbers=True,
       lemmatize=False,
       lemmatize_method='wordnet'
      )


def clean_email_case_1(email): # days
    split_email:list = []
    for i in range(len(split_strings_days)):
        split_email = email.split(split_strings_days[i])
        if len(split_email) > 1:
            break
        else:
            continue
        
    text = split_email[0]
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    filtered_string = ""
    for token in doc:
        # print(token, token.pos_)
        if token.pos_ in ['PROPN']:
            # new_token = " <{}>".format(token.ent_type_)
            new_token = ""
        elif token.pos_ == "PUNCT":
            new_token = token.text
        else:
            new_token = " {}".format(token.text)
        filtered_string += new_token
        
    filtered_string = filtered_string[1:]
    filtered_string = filtered_string.lower()
    pattern=r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))';
    match = re.findall(pattern, filtered_string)
    for m in match:
        url = m[0]
        filtered_string = filtered_string.replace(url, '')
    return filtered_string


def clean_email_case_2(email): # months
    split_email:list = []
    for i in range(len(split_strings_months)):
        split_email = email.split(split_strings_months[i])
        if len(split_email) > 1:
            break
        else:
            continue
        
    text = split_email[0]
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    filtered_string = ""
    for token in doc:
        # print(token, token.pos_)
        if token.pos_ in ['PROPN']:
            # new_token = " <{}>".format(token.ent_type_)
            new_token = ""
        elif token.pos_ == "PUNCT":
            new_token = token.text
        else:
            new_token = " {}".format(token.text)
        filtered_string += new_token
        
    filtered_string = filtered_string[1:]
    filtered_string = filtered_string.lower()
    pattern=r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))';
    match = re.findall(pattern, filtered_string)
    for m in match:
        url = m[0]
        filtered_string = filtered_string.replace(url, '')
    return filtered_string


def clean_email_case_3(email): # from
    split_strings_from = "From:"
    split_email:list = []
    for i in range(len(split_strings_from)):
        split_email = email.split(split_strings_from[i])
        if len(split_email) > 1:
            break
        else:
            continue
        
    text = split_email[0]
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    filtered_string = ""
    for token in doc:
        # print(token, token.pos_)
        if token.pos_ in ['PROPN']:
            # new_token = " <{}>".format(token.ent_type_)
            new_token = ""
        elif token.pos_ == "PUNCT":
            new_token = token.text
        else:
            new_token = " {}".format(token.text)
        filtered_string += new_token
        
    filtered_string = filtered_string[1:]
    filtered_string = filtered_string.lower()
    pattern=r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))';
    match = re.findall(pattern, filtered_string)
    for m in match:
        url = m[0]
        filtered_string = filtered_string.replace(url, '')
    return filtered_string


def get_email_case(email):

  # st = time.time()
  base_index_months = 1000000
  for i in range(len(split_strings_months)):
    index = re.search(split_strings_months[i], email)
    if index == None:
      continue
    elif index.start() < base_index_months:
      base_index_months = index.start()
    else:
      continue

  base_index_days = 1000000
  for i in range(len(split_strings_days)):
    index = re.search(split_strings_days[i], email)
    if index == None:
      continue
    elif index.start() < base_index_days:
      base_index_days = index.start()
    else:
      continue

  base_index_from = 1000000
  index = re.search("From:", email)
  if index == None:
      print("")
  elif index.start() < base_index_from:
      base_index_from = index.start()
  else:
      print("")

  if base_index_from < base_index_days and base_index_from < base_index_days:
    filtered_email = clean_email_case_3(email)

  elif base_index_days < base_index_months and base_index_days < base_index_months:
    filtered_email = clean_email_case_1(email)

  else:
    filtered_email = clean_email_case_2(email)

  # et = time.time()
  return filtered_email


def rule_engine(email):
    interested_bi_grams = ["we are", "interested in"]     
    interested_quad_grams = ["thanks for reaching out", "would be happy to", "like to learn more", "please let me know", "would like to learn", "to learn more about", "hi thanks for reaching"]
    not_interested_quad_grams = ["interested at this time", "not interested at this", "we are not interested", "am not interested at", "we are all set", "are not interested at", "for reaching out we"]


    if email == "":
        count_cannotbedetermined += 1
    else:
        email = str.lower(email)
        count_bi = 0
        for i in range(len(interested_bi_grams)):
            if interested_bi_grams[i] in email:
                count_bi += 1

        count_quad = 0
        for i in range(len(interested_quad_grams)):
            if interested_quad_grams[i] in email:
                count_quad += 1

        P = 20 * count_bi + 40 * count_quad

        count_quad = 0
        for i in range(len(not_interested_quad_grams)):
            if not_interested_quad_grams[i] in email:
                count_quad += 1

        N = 40 * count_quad

        if "unsubscribe" in email:
            return 1
        elif P >= 40 and N <= 20:
            return 2
        
        elif P <= 20 and N >= 40:
            return 3
        else:
            return 4


def get_sentiment(email):

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    cleaned_email = get_email_case(email)
    ans = rule_engine(cleaned_email)
    
    if ans == 1:
        return "Unsubscribe"
    elif ans == 2:
        return "Interested"
    elif ans == 3:
        return "Not interested"
    else:
        print("cannot be determined")
        print("going to AI approach")

        test = [cleaned_email]
        test_vec = tokenizer.texts_to_sequences(test)
        test_vec = pad_sequences(test_vec, 79)
        y_pred = loaded_model.predict(test_vec)
        print(y_pred)
        if y_pred.argmax(axis = 1) == 0:
            return "Interested"
        else:
            return "Not interested"


f = open('test.json', "r")

data = f.read()

print(get_sentiment(data))

# Iterating through the json
# list
# for i in data['Emails']:
# 	print(i)

# # Closing file
# f.close()



# @app.route("/")
# def hello():
#     return render_template('getemail.html')
#     # return "hello there"



# @app.route("/", methods=['POST'])
# def get_email():
#     text = request.form['emailthread']
#     sentiment = get_sentiment(text)
#     return sentiment


# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5002))
#     app.run(debug=True, host='0.0.0.0', port=port)
