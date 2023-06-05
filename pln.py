import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import webbrowser

def preprocess_text(text):
    # Tokenização das palavras
    tokens = word_tokenize(text)

    # Remoção das stopwords
    stop_words = set(stopwords.words('portuguese'))
    filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    # Junção das palavras processadas em uma string
    processed_text = ' '.join(stemmed_tokens)

    return processed_text

# def pesquisar(query):
#     processed_query = preprocess_text(query)
#     url = f"https://www.google.com/search?q={processed_query}"
#     webbrowser.open(url)

def pesquisar(query):
    processed_query = preprocess_text(query)
    url = f"https://www.google.com/search?q={processed_query}"
    webbrowser.open_new_tab(url)

def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {query}")
        pesquisar(query)
    except Exception as e:
        print("Desculpe, não entendi. Por favor, repita.")
        return None
