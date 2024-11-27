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

# Data: Full list of publications
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
    {"title": "Comparative analysis of chaotic properties of optical chaos generators",
     "authors": "SZ Ali, MK Islam, M Zafrullah",
     "journal": "Optik-International Journal for Light and Electron Optics",
     "citations": 17,
     "year": 2011},
    {"title": "A generalized higher order neural network for aircraft recognition in a video docking system",
     "authors": "SZ Ali, MA Choudhry",
     "journal": "Neural computing & applications 19 (1), 21-32",
     "citations": 14,
     "year": 2010},
    {"title": "Secure optical QAM transmission using chaos message masking",
     "authors": "F Qamar, MK Islam, R Farhan, M Ali, SZ Ali Shah",
     "journal": "Journal of Optical Communications 43 (3), 421-428",
     "citations": 11,
     "year": 2022},
    {"title": "Design Issues of Digital and Analog Chaotic RoF Link Using Chaos Message Masking",
     "authors": "DA Mazhar, SZA Shah, MK Islam, F Qamar",
     "journal": "IEEE Access 7, 174042-174050",
     "citations": 10,
     "year": 2019},
    {"title": "Effect of message parameters in additive chaos modulation in Erbium Doped Fiber Ring Laser (EDFRL)",
     "authors": "SZ Ali, MK Islam, M Zafrullah",
     "journal": "Optik-International Journal for Light and Electron Optics 124 (18), 3746-3750",
     "citations": 10,
     "year": 2013},
    {"title": "Effect of transmission fiber on dense wavelength division multiplexed (DWDM) chaos synchronization",
     "authors": "SZ Ali, MK Islam, M Zafrullah",
     "journal": "Optik 124 (12), 1108-1112",
     "citations": 10,
     "year": 2013},
    {"title": "Erbium-doped fiber ring laser dynamical analysis for chaos message masking scheme",
     "authors": "SZ Ali, MK Islam",
     "journal": "Optica Applicata 47 (3), 395-410",
     "citations": 7,
     "year": 2017},
    {"title": "128-QAM dual-polarization chaotic long-haul system performance evaluation",
     "authors": "F Qamar, MK Islam, R Shahzadi, SZ Ali, M Ali",
     "journal": "Journal of Optical Communications 44 (s1), s1873-s1881",
     "citations": 6,
     "year": 2024},
    {"title": "Effect of transmission fiber and amplifier noise on optical chaos synchronization",
     "authors": "SZ Ali, MK Islam, M Zafrullah",
     "journal": "Optical review 19, 320-327",
     "citations": 5,
     "year": 2012},
    {"title": "DWDM system analysis by varying different erbium doped fiber parameters",
     "authors": "F Qamar, K Islam, R Farhan, M Ali, SZ Ali, A Shahzad",
     "journal": "2018 International Conference on Engineering and Emerging Technologies …",
     "citations": 2,
     "year": 2018},
    {"title": "First observation of Quasi-Chaos in Erbium doped fiber ring laser",
     "authors": "SZ Ali",
     "journal": "Chaos Modelling and Simulation (CMSIM) Journal",
     "citations": 2,
     "year": 2016},
    {"title": "Control of optical chaos spectrum in semiconductor laser for secure RoF communication",
     "authors": "DA Mazhar, SZ Ali, MK Islam",
     "journal": "Optica Applicata 52 (4)",
     "citations": 1,
     "year": 2022},
    {"title": "Statistical dependence analysis of Erbium doped fiber ring lasers (EDFRL) chaos",
     "authors": "SZ Ali, MK Islam",
     "journal": "Results in Optics 5, 100167",
     "citations": 1,
     "year": 2021},
    {"title": "Second observation of Quasi–Chaos in Erbium doped fiber ring laser",
     "authors": "SZ Ali",
     "journal": "Chaos Modelling and Simulation (CMSIM) Journal",
     "citations": 1,
     "year": 2016},
    {"title": "Generation of ultra-high bandwidth chaos in EDFRL using Moiré grating",
     "authors": "SZ Ali, MK Islam, DA Mazhar",
     "journal": "Results in Optics 12, 100453",
     "citations": 0,
     "year": 2023},
    {"title": "Non-Shilnikov Chaos in Erbium doped Fiber Ring Laser (pp 257-266)",
     "authors": "SZAMKI M Sohail Khalid",
     "journal": "Chaos Modelling and Simulation(CMSIM) Journal 2017 (2), 257-266",
     "citations": 0,
     "year": 2017},
    {"title": "Nonlinear Fiber Optics Nonlinear Fiber Optics, 2001",
     "authors": "SZ ALI, MK ISLAM, M ZAFRULLAH",
     "journal": "Optical review 19 (5), 320-327",
     "citations": 0,
     "year": 2012},
    {"title": "GENERATION AND CONTROL OF CHAOS FOR SECURE OPTICAL COMMUNICATION USING EDFRL",
     "authors": "SZA Shah",
     "journal": "Department of Electrical Engineering University of Engineering and",
     "citations": 0,
     "year": 2021}
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
