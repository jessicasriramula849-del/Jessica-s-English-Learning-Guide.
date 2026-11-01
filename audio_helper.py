import io
import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS

@st.cache_data(show_spinner=False)
def generate_speech_audio(text: str, accent: str = "com", slow: bool = False) -> bytes:
    """
    Generates mp3 bytes using gTTS.
    accent: 'com' (US), 'co.uk' (UK), 'ca' (Canada), 'com.au' (Australia)
    """
    try:
        clean_text = text.strip()
        if not clean_text:
            return b""
        tts = gTTS(text=clean_text, lang='en', tld=accent, slow=slow)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()
    except Exception:
        return b""

def play_audio_widget(text: str, key_suffix: str = "", label: str = "🔊 Listen to Jessica", accent: str = "com", slow: bool = False):
    """
    Renders an audio player for the given text.
    """
    audio_bytes = generate_speech_audio(text, accent=accent, slow=slow)
    if audio_bytes:
        st.audio(audio_bytes, format="audio/mp3")
    else:
        render_web_speech_button(text, button_text=label, key_id=f"ws_{key_suffix}")

def render_web_speech_button(text: str, button_text: str = "🔊 Pronounce", speed: float = 0.9, accent: str = "en-US", key_id: str = "btn", theme: str = "ocean"):
    """
    Renders an instant browser Web Speech API button with zero latency and colorful styling.
    theme options: 'ocean' (blue), 'sunset' (orange-pink), 'emerald' (mint-green), 'berry' (purple)
    """
    escaped_text = text.replace('"', '&quot;').replace("'", "\\'").replace("\n", " ")

    theme_styles = {
        "ocean": "background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%); color: #ffffff; box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25); border: 1px solid rgba(255, 255, 255, 0.4);",
        "sunset": "background: linear-gradient(135deg, #f97316 0%, #ec4899 100%); color: #ffffff; box-shadow: 0 4px 10px rgba(236, 72, 153, 0.25); border: 1px solid rgba(255, 255, 255, 0.4);",
        "emerald": "background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: #ffffff; box-shadow: 0 4px 10px rgba(16, 185, 129, 0.25); border: 1px solid rgba(255, 255, 255, 0.4);",
        "berry": "background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); color: #ffffff; box-shadow: 0 4px 10px rgba(109, 40, 217, 0.25); border: 1px solid rgba(255, 255, 255, 0.4);"
    }
    btn_style = theme_styles.get(theme, theme_styles["ocean"])

    html_code = f"""
    <div style="margin: 6px 0;">
        <button id="btn_{key_id}" onclick="speakText_{key_id}()" 
            style="{btn_style}
                   border-radius: 20px; padding: 7px 16px; font-size: 13.5px; font-weight: 700; 
                   cursor: pointer; display: inline-flex; align-items: center; gap: 8px; 
                   font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
                   letter-spacing: 0.02em; transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);">
            <span>{button_text}</span>
        </button>
        <script>
            function speakText_{key_id}() {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    var text = "{escaped_text}";
                    var msg = new SpeechSynthesisUtterance(text);
                    msg.lang = '{accent}';
                    msg.rate = {speed};
                    
                    var btn = document.getElementById("btn_{key_id}");
                    var origText = btn.innerHTML;
                    btn.innerHTML = "<span>✨ Speaking...</span>";
                    btn.style.transform = "scale(0.96)";
                    
                    msg.onend = function() {{
                        btn.innerHTML = origText;
                        btn.style.transform = "scale(1)";
                    }};
                    msg.onerror = function() {{
                        btn.innerHTML = origText;
                        btn.style.transform = "scale(1)";
                    }};
                    
                    window.speechSynthesis.speak(msg);
                }} else {{
                    alert('Web Speech API is not supported in this browser.');
                }}
            }}
        </script>
    </div>
    """
    components.html(html_code, height=52)
