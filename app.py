import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Quick Voice Note", page_icon="📝")
st.title("📝 Quick Voice Note")

audio_file = st.audio_input("Say your note out loud")

if audio_file is not None:
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:  
            note = recognizer.recognize_google(audio)

            f = open("quick_note.txt", "a")
            f.write(note+"\n")
            f.close()

            st.success("Note saved!")
            st.markdown(f"**Note:** {note}")

        except sr.UnknownValueError:
            st.error("Didn't catch that. Try again.")
        except Exception as e:
            st.error(f"Error: {e}")
