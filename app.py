import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Quick Voice Note", page_icon="📝")
st.title("📝 Quick Voice Note")

if st.button("🎤 Record Note"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        with st.spinner("🎤 Listening... Please speak clearly"):
            try:
                audio = recognizer.listen(mic, timeout=5)
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
