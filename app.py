import streamlit as st
from datetime import datetime

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Innovators Meetup 2026",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# GLOBAL STYLING
# -------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.hero {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 100px 30px;
    border-radius: 24px;
    text-align: center;
    color: white;
    margin-bottom: 60px;
}

.section {
    background: white;
    padding: 60px;
    border-radius: 24px;
    margin-bottom: 60px;
    box-shadow: 0px 15px 40px rgba(0,0,0,0.05);
}

.section h2 {
    margin-bottom: 25px;
}

.agenda-item {
    padding: 20px 0;
    border-bottom: 1px solid #eee;
}

.highlight {
    background: #0f172a;
    color: white;
    padding: 70px;
    border-radius: 24px;
    text-align: center;
    margin-bottom: 60px;
}

.footer {
    text-align: center;
    padding: 60px 20px;
    font-size: 18px;
}

.footer a {
    font-weight: bold;
    text-decoration: none;
    color: #0f172a;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------
st.markdown(f"""
<div class="hero">
    <h1>🚀 AI Innovators Meetup 2026</h1>
    <h3>Where Entrepreneurs, Builders & Visionaries Connect</h3>
    <p>Atlanta, GA | {datetime.now().strftime("%B %d, %Y")}</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# FLYER SECTION
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎨 Official Event Flyer")
st.image("ai_meetup_flyer_letter.png", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# ABOUT SECTION
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🌍 About The Event")

st.write("""
The AI Innovators Meetup is a high-impact gathering designed for forward-thinking 
entrepreneurs, business leaders, developers, marketers, and creators who are serious 
about implementing artificial intelligence into real-world business systems.

This is not theory. This is applied AI.

Expect live demonstrations, system walkthroughs, automation frameworks, 
and actionable strategies you can deploy immediately.
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# WHY ATTEND
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🔥 Why You Should Attend")

st.markdown("""
• Learn how to integrate AI into your existing business  
• Discover automation frameworks that reduce overhead  
• See live builds of AI-powered funnels  
• Connect with high-level entrepreneurs  
• Position yourself ahead of the AI curve  
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# SPEAKER SECTION
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎤 Featured Speaker & AI Showcase")

st.image("IMG_0581.JPG", use_container_width=True)

st.write("""
Experience live demonstrations covering:

• AI workflow automation  
• Local AI model deployment  
• AI chat systems for business  
• Intelligent content generation  
• Scaling with AI infrastructure  
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# AGENDA SECTION
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🗓 Event Agenda")

agenda = [
    ("5:30 PM", "Registration & Strategic Networking"),
    ("6:00 PM", "Opening Keynote – The AI Shift"),
    ("6:30 PM", "Live AI Funnel Build"),
    ("7:15 PM", "Automation Framework Breakdown"),
    ("8:00 PM", "Panel Discussion: AI & Business 2026"),
    ("8:45 PM", "Q&A + Mastermind Networking"),
    ("9:30 PM", "Closing + Exclusive Opportunities")
]

for time, event in agenda:
    st.markdown(f"""
    <div class="agenda-item">
        <strong>{time}</strong><br>
        {event}
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# WHO SHOULD ATTEND
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎯 Who This Is For")

st.markdown("""
• Entrepreneurs ready to scale  
• Business owners seeking automation  
• Developers building AI tools  
• Content creators using AI workflows  
• Agency owners & consultants  
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# NETWORKING HIGHLIGHT
# -------------------------------------------------
st.markdown("""
<div class="highlight">
    <h2>🤝 This Is A Room Of Builders</h2>
    <p>Collaborate. Strategize. Build partnerships. Launch smarter.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# FAQ SECTION
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("❓ Frequently Asked Questions")

st.markdown("""
**Do I need technical experience?**  
No. This event is designed for both technical and non-technical professionals.

**Will there be live demonstrations?**  
Yes — real AI systems will be built and shown live.

**Is networking included?**  
Absolutely. Strategic networking is a major focus.
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# RSVP SECTION
# -------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎟 Reserve Your Spot")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
attendance = st.selectbox("Will you attend?", ["Yes", "Maybe", "No"])

if st.button("Confirm Attendance"):
    st.success("You're officially on the list. See you at the event!")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("""
<div class="footer">
    🚀 Powered by Intelligent AI Systems<br><br>
    Visit Our Main AI Platform:<br><br>
    <a href="https://entremotivator.com" target="_blank">
        Entremotivator.com
    </a>
</div>
""", unsafe_allow_html=True)
