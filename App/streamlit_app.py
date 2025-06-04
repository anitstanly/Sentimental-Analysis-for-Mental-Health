import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Happy Helper", icon="🌞")
page_1 = st.Page("deber.py", title="Emotion Detector", icon="🌿")
page_2 = st.Page("chatboat1.py", title="Supportive Chatboat", icon="🤖")
page_3 = st.Page("page_2.py", title="Instant Mental Health Toolkit", icon="🧘")

# Set up navigation
pg = st.navigation([main_page,page_1 ,page_2,page_3 ])

# Run the selected page
pg.run()
