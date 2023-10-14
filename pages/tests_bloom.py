import streamlit as st
from transformers import pipeline
from deep_translator import GoogleTranslator
from textblob import TextBlob
import spacy


# Titre de l'application
st.title("Interact with a Bloomz LLM")

# Sélection du modèle
model_option = st.sidebar.selectbox("Sélectionner un modèle", ["Local", "Hugging Face"])

# Charger le modèle de génération de texte de Hugging Face
text_generation_pipeline = pipeline("text-generation", model="./bloomz-560m-sft-chat")
translator = GoogleTranslator(source='auto')
nlp = spacy.load("fr_core_news_sm")


def summarize_text(text):
    # Implémentez votre logique de résumé ici
    # Par exemple, utilisez un modèle de résumé pré-entraîné
    # Renvoyez le texte résumé
    return "Résumé du texte non disponible pour le moment."

def analyze_sentiment(text):
    # Utilisez TextBlob pour l'analyse de sentiment
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def extract_named_entities(text):
    # Utilisez spaCy pour l'extraction des entités nommées
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    return entities

def translate_text(text, language="en"):
    # Utilisez deep_translator pour traduire le texte
    translated_text = translator.translate(text, target=language)
    return translated_text

def generate_questions_answers(text):
    # Generate a list of questions and answers.
    questions_answers = []
    for question in ["What is the main idea of the text?", "What are the key points of the text?", "What are the implications of the text?"]:
        # Generate an answer to the question.
        generated_text = text_generation_pipeline(text, max_length=200, do_sample=True, temperature=0.7, top_p=0.9)[0]['generated_text']

        # Add the question and answer to the list.
        questions_answers.append({"question": question, "answer": generated_text})

    return questions_answers

# Saisie d'un texte de prompt
prompt = st.text_input("Texte de prompt")

if prompt:
    # Générer et afficher le texte
    st.write("Texte généré :")
    generated_text = text_generation_pipeline(prompt, max_length=200, do_sample=True, temperature=0.7, top_p=0.9)[0]['generated_text']
    st.write(generated_text)

    # Résumé automatique du texte
    if st.checkbox("Résumé du texte"):
        summary = summarize_text(generated_text)
        st.write("Résumé du texte :")
        st.write(summary)

    # Traduction automatique
    if st.checkbox("Traduction du texte"):
        translated_text = translate_text(generated_text, language="en")
        st.write("Texte traduit :")
        st.write(translated_text)

    # Génération de questions-réponses
    if st.checkbox("Génération de questions-réponses"):
        questions_answers = generate_questions_answers(generated_text)
        st.write("Questions-réponses :")
        st.write(questions_answers)

    # Analyse de sentiment
    if st.checkbox("Analyse de sentiment"):
        sentiment = analyze_sentiment(generated_text)
        st.write("Analyse de sentiment :")
        st.write(sentiment)

    # Extraction d'entités nommées
    if st.checkbox("Extraction d'entités nommées"):
        entities = extract_named_entities(generated_text)
        st.write("Entités nommées dans le texte :")
        st.write(entities)
        
    # Analyse de la syntaxe
    if st.checkbox("Analyse de la syntaxe"):
        # Implémentez l'analyse de la syntaxe ici, par exemple avec un modèle d'analyse syntaxique
        syntax_tree = "Arbre syntaxique du texte"  # Remplacez ceci par l'arbre syntaxique généré
        st.write("Analyse de la syntaxe du texte :")
        st.write(syntax_tree)