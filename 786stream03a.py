import streamlit as st

# App title and introductory verse
st.title("Bismillah-ir-Rahman-ir-Rahim")
st.header("Knowledge is the light that illuminates the path. 📚✨")
st.subheader('"Say: Are those who know equal to those who do not know?" - Quran (39:9)')

# Welcome message and Google Scholar profile link
st.write("### Welcome to my Google Scholar Showcase!")
st.write("""
This page highlights my academic contributions.  
[Visit my Google Scholar profile here](https://scholar.google.com/citations?user=AY3TwVUAAAAJ&hl=en).
""")

# Section: About Me
st.write("#### About Me:")
st.write("""
- **Name:** Your Full Name  
- **Affiliation:** Your University/Organization  
- **Research Interests:** AI, Machine Learning, Robotics, etc.  
""")

# Display a list of publications in an attractive format
st.write("### 📜 My Publications")
st.write("Below is a list of my research contributions, organized for easy browsing:")

# Data: List of publications
publications = [
    {"title": "Effect of parametric variation on generation and enhancement of chaos in erbium-doped fiber-ring lasers",
     "authors": "SZ Ali, MK Islam, M Zafrullah",
     "journal": "Optical Engineering 49 (10), 105002",
     "citations": 28,
     "year": 2010},
    {"title": "Secure Duobinary Signal Transmission in Optical Communication Networks for High Performance & Reliability",
     "authors": "F Qamar, MK Islam, SZA Shah, R Farhan, M Ali",
     "journal": "IEEE Access 5, 17795-17802",
     "citations": 23,
     "year": 2017},
    {"title": "Generation of higher degree chaos by controlling harmonics of the modulating signal in EDFRL",
     "authors": "SZ Ali, MK Islam, M Zafrullah",
     "journal": "Optik 122 (21), 1903-1909",
     "citations": 17,
     "year": 2011},
    # Add the rest of your papers here in similar format...
]

# Loop through each publication and display it in a collapsible panel
for pub in publications:
    with st.expander(f"📄 {pub['title']}"):
        st.write(f"**Authors:** {pub['authors']}")
        st.write(f"**Journal:** {pub['journal']}")
        st.write(f"**Cited By:** {pub['citations']} citations")
        st.write(f"**Year:** {pub['year']}")

# Thank you message
st.write("___")  # Divider
st.write("Thank you for exploring my research! 🌟 Stay curious and keep learning.")
