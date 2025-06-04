import streamlit as st
import random
#st.markdown("# Page 2 ❄️")



st.markdown(
    """
    <style>
    /* Set background image */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470'); /* Replace with your image URL */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Optional: Make text easier to read on image */
    h1, h2, h3, h4, h5, h6, p, div {
        color: #ffffff;
        text-shadow: 1px 1px 2px #000000;
    }

    /* Optional: make chat input and boxes more visible */
    .block-container {
        background-color: rgba(.2, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#st.set_page_config(page_title="Instant Mental Health Toolkit", layout="centered")

st.title(" Instant Mental Health Toolkit 🧘")
st.write("Feeling overwhelmed? Take a moment. Choose what you need right now:")

# --- Menu Options ---
option = st.selectbox("Choose your support:", [
    "-- Select --",
    "🎵 Uplifting or Calming Music",
    "📖 Read Something Gentle",
    "🎮 Relaxing Games",
    "🛠️ Instant Relief Tools",
    "📘 Resource Center"
])

# --- MUSIC ---
if option == "🎵 Uplifting or Calming Music":
    st.subheader("🎵 Music for Your Mood")
    music_links = {
        "Happy Energy Boost": "https://www.youtube.com/watch?v=OesMEEalJho",
        "Nature Sounds": "https://www.youtube.com/watch?v=G8nNGk6LHaM&t=118s",
        "Instrumental Music": "https://www.youtube.com/watch?v=piaCLiAKm3o",
        "Classical Music": "https://www.youtube.com/watch?v=WQhFl7RdBh8"
    }
    for name, url in music_links.items():
        st.markdown(f"[{name}]({url})")

# --- READING ---
elif option == "📖 Read Something Gentle":
    st.subheader("📚 Relaxing Reads")

    st.markdown("""
    - [🧘 Mindfulness Poems](https://dailymindfulness.com/poems)
    - [📖 Zen Habits Blog](https://zenhabits.net/)
    - [🌸 Tiny Buddha Stories](https://tinybuddha.com/blog-posts/)
    - [🕊️ The Kids Story](https://learnenglishkids.britishcouncil.org/listen-watch/short-stories)
    - [📗 Inspiring Stories](https://www.sunnyskyz.com/feel-good-stories)
    """)


# --- GAMES ---
elif option == "🎮 Relaxing Games":
    st.subheader("🎮 Light, Relaxing Games")
    st.markdown("- [Sudoku](https://sudoku.com/)")
    st.markdown("- [Coloring Game](https://www.roomrecess.com/pages/ColoringPagesForKids.html)")
    st.markdown("- [2048 Game](https://play2048.co/)")
    st.markdown("- [Calm Piano Tiles](https://www.crazygames.com/game/piano-tiles)")

# --- INSTANT TOOLS ---
elif option == "🛠️ Instant Relief Tools":
    st.subheader("🛠️ Coping Tools")

    # List of coping strategies
    tools = [
        "Choose a coping tool",
        "🌬️ Breathing Exercise (4-7-8)",
        "🧘 Guided Meditation",
        "📝 Journaling Prompt"
    ]

    selected_tool = st.radio("Select a tool to explore:", tools)

    # Tool: Breathing Exercise
    if selected_tool == "🌬️ Breathing Exercise (4-7-8)":
        st.markdown("**Breathing Technique: 4-7-8**")
        st.markdown("Inhale for 4 seconds → Hold for 7 seconds → Exhale for 8 seconds")
        st.markdown("Try following this calming breathing bubble video:")
        st.video("https://www.youtube.com/watch?v=EYQsRBNYdPk")

    # Tool: Guided Meditation
    elif selected_tool == "🧘 Guided Meditation":
        st.markdown("**Light Physical Activity & Meditation**")
        st.markdown("Gentle movement and meditation can help reset your mind.")
        st.markdown("Try this guided video:")
        st.video("https://www.youtube.com/watch?v=vj0JDwQLof4")

    # Tool: Journaling
    elif selected_tool == "📝 Journaling Prompt":
        st.markdown("**Feeling heavy? Lighten your mind by writing it out here:**")
        journal_text = st.text_area("Write what you're feeling...")

        if journal_text:
            st.download_button(
                label="📥 Download Your Journal Entry",
                data=journal_text,
                file_name="my_journal_entry.txt",
                mime="text/plain"
            )

# --- RESOURCES ---
elif option == "📘 Resource Center":
    st.subheader("📘 Help & Support – Germany")

    st.write("**Emergency Help**")
    st.markdown("""
    - **TelefonSeelsorge (24/7, free, anonymous):**
        - 🌐 [telefonseelsorge.de](https://www.telefonseelsorge.de/)
    - **International Helpline Berlin (English support):**
        - 📞 030 44 01 06 07
    - **Nummer gegen Kummer (Youth Helpline):**
        - 📞 116 111
    """)

    st.write("**Therapist Finders**")
    st.markdown("""
    - [Federal Chamber of Psychotherapists](https://www.psychotherapiesuche.de/)
    - [Therapie.de](https://www.therapie.de/)
    """)

    st.write("**Articles & Self-Help Resources**")
    st.markdown("""
    - [Handbook Germany – Mental Health](https://handbookgermany.de/en/mental-health)
    - [Expatica – Mental Health in Germany](https://www.expatica.com/de/healthcare/healthcare-services/mental-health-in-germany-346138/)
    - [How to Manage a Panic Attack](https://www.healthline.com/health/how-to-stop-a-panic-attack)
    """)

# --- Default ---
else:
    st.info("Please select an option above to begin.")
#st.sidebar.markdown("# Page 2 ❄️")
