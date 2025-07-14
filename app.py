from flask import Flask, render_template, request
import spacy 

# We initialize spacy 

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")  # Here we load the spacy model to use