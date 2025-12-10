import streamlit as st
import edge_tts
import asyncio
import tempfile

# -------------------------------------------
# Kira29.1 - Multilingual Neural TTS System
# Author: Hasnain Chavhan
# -------------------------------------------

st.set_page_config(page_title="Kira29.1 - TTS", layout="centered")
st.title("🔊 Kira29.1 - Text-to-Speech Generator")

# Text input field
text = st.text_area("Enter Text:", height=150)

# Supported languages + neural voices
language_voice_map = {  
    'Marathi (mr)': {
        'male': 'mr-IN-ManoharNeural',
        'female': 'mr-IN-AarohiNeural'
    },
    'Hindi (hi)': {
        'male': 'hi-IN-MadhurNeural',
        'female': 'hi-IN-SwaraNeural'
    },
    'Bengali (bn)': {
        'male': 'bn-IN-PrabirNeural',
        'female': 'bn-IN-TanishaaNeural'
    },
    'Tamil (ta)': {
        'male': 'ta-IN-ValluvarNeural',
        'female': 'ta-IN-PallaviNeural'
    }
}

# UI Select Fields
language = st.selectbox("Select Language", list(language_voice_map.keys()))
voice_type = st.selectbox("Select Voice", ['male', 'female'])

# Resolve selected voice ID
voice_id = language_voice_map[language][voice_type]


# ------------- TTS ENGINE -------------
async def generate_tts_file(text: str, voice: str) -> str:
    """Generate MP3 file from text using Edge-TTS and return file path."""
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_path = tmp_file.name
    tmp_file.close()

    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(tmp_path)
        return tmp_path
    except Exception as e:
        raise RuntimeError(f"Error generating TTS: {e}")


# ------------- STREAMLIT LOGIC -------------
if st.button("🎧 Generate Audio"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            audio_path = asyncio.run(generate_tts_file(text, voice_id))

            st.success("✔ Audio generated successfully!")

            # Play audio
            with open(audio_path, "rb") as audio:
                audio_bytes = audio.read()
                st.audio(audio_bytes, format="audio/mp3")

                # Download button
                st.download_button(
                    label="⬇ Download Audio",
                    data=audio_bytes,
                    file_name="kira_tts_output.mp3",
                    mime="audio/mp3"
                )

        except Exception as err:
            st.error(f"❌ Something went wrong: {err}")
