#Importing all the required libraries
import streamlit as st
from streamlit_mic_recorder import speech_to_text
from googletrans import Translator


st.set_page_config("Language translator")



st.title("A simple language translator!")

st.write("")
st.write("")

def translate(text):
    st.subheader("Message Recorded:")
    st.write(text)
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
        st.write(translation.text)


#datas 
languages = [" ","Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian", "Bengali", 
                         "Bosnian", "Bulgarian", "Catalan", "Cebuano", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)", 
                         "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto", "Estonian", "Filipino", "Finnish", 
                         "French", "Frisian", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian Creole", "Hausa", 
                         "Hawaiian", "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian", "Irish", "Italian", 
                         "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Kinyarwanda", "Korean", "Kurdish (Kurmanji)", "Kyrgyz", 
                         "Lao", "Latin", "Latvian", "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam",
                           "Maltese", "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian", "Odia", "Pashto", 
                           "Persian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Samoan", "Scots Gaelic", "Serbian",
                             "Sesotho", "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili",
                               "Swedish", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Turkish", "Ukrainian", "Urdu", "Uzbek", 
                               "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"]

#codes for the languages
codes = [" ","af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", 
                  "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", 
                  "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la",
                    "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "or", "ps", "fa", "pl", "pt", 
                    "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta",
                      "tt", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]

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
    translate(text)

    
        

