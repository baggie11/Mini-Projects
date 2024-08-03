#Importing all the required libraries
import streamlit as st
from streamlit_mic_recorder import speech_to_text
from googletrans import Translator
from gtts import gTTS
from IPython.display import Audio,display
import io


st.set_page_config("Language translator")



st.title("A simple language translator!")

st.write("")
st.write("")

#text to speech
def text_to_speech(text,lang):
    tts = gTTS(text = text,lang = lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    #display the audio
    audio_data = fp.read()
    st.audio(audio_data, format="audio/mp3", autoplay=True)


#function to translate
def translate(text):
    st.subheader("Message Recorded:")
    st.text(text)
    st.write(" ")
    st.write(" ")
    option = st.selectbox("Select a language:",languages)
    if option != " ":
        st.write("Chosen language is :",option)
        index = languages.index(option)
        code = codes[index]

        #create a translator object
        translator = Translator()
        #translate the sentence
        translation = translator.translate(text,src = "en",dest = code)

        #write the translation to the website
        st.write("Translated content : " + translation.text)

        text_to_speech(translation.text,code)



#datas 
languages = [" ","Afrikaans", "Arabic", "Bengali", "Bulgarian", "Cantonese", "Catalan", "Chinese", "Croatian", "Czech", "Danish", "Dutch",
              "English", "Filipino", "Finnish", "French", "German", "Greek", "Gujarati", "Hebrew", "Hindi", "Hungarian", "Icelandic", 
              "Indonesian", "Italian", "Japanese", "Javanese", "Kannada", "Khmer", "Korean", "Latvian", "Lithuanian", "Malay", 
              "Malayalam", "Marathi", "Nepali", "Norwegian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Serbian", 
              "Sinhala", "Slovak", "Spanish", "Sundanese", "Swahili", "Swedish", "Tamil", "Telugu", "Thai", "Turkish", "Ukrainian",
                "Urdu", "Vietnamese", "Welsh"]


#codes for the languages
codes = [" ","af", "ar", "bn", "bg", "yue", "ca", "zh-CN", "hr", "cs", "da", "nl", "en", "fil", "fi", "fr", "de", "el", "gu", "he", 
         "hi", "hu", "is", "id", "it", "ja", "jv", "kn", "km", "ko", "lv", "lt", "ms", "ml", "mr", "ne", "no", "pl", "pt", "pa",
           "ro", "ru", "sr", "si", "sk", "es", "su", "sw", "sv", "ta", "te", "th", "tr", "uk", "ur", "vi", "cy"]


input_mode = st.selectbox("Select the input mode",[" ","Audio","Text"])
button = False
text = None
if input_mode == "Audio":
    st.write("Speak aloud the text to be translated!")
    text = speech_to_text(
                language='en',
                start_prompt="""START RECORDING""",
                stop_prompt="STOP RECORDING",
                just_once=False,
                #use_container_width=False,
                callback=None,
                args=(),
                kwargs={},
                key=None)
    if text is not None:
        translate(text)
        
elif input_mode == "Text":
    text = st.text_area("Enter the text to be translated!")
    button = st.button("Enter")
    if text is not None or text != "":
        translate(text)


    



    
        
