import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="LingoFlow",
    page_icon="🌐",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* MAIN PAGE */
.stApp {
    background: #f4f6ff;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HEADER */
.header {
    text-align: center;
    padding: 20px 0 30px;
}

.hero-icon {
    font-size: 48px;
}

.header h1 {
    color: #312e81 !important;
    font-size: 46px;
    font-weight: 800;
    margin: 5px 0;
}

.header h1 span {
    color: #6366f1 !important;
}

.header p {
    color: #475569 !important;
    font-size: 18px;
}

/* ALL LABELS */
label,
.stSelectbox label,
.stTextArea label {
    color: #1e293b !important;
    font-weight: 700 !important;
}

/* TEXT AREA */
textarea {
    background-color: #ffffff !important;
    color: #1e293b !important;
    border: 2px solid #c7d2fe !important;
    border-radius: 14px !important;
}

/* PLACEHOLDER */
textarea::placeholder {
    color: #64748b !important;
}

/* SELECT BOX */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #1e293b !important;
    border: 1px solid #c7d2fe !important;
}

/* SELECTED TEXT */
div[data-baseweb="select"] span {
    color: #1e293b !important;
}

/* TRANSLATE BUTTON */
div.stButton > button {
    background: #6366f1 !important;
    color: white !important;
    border-radius: 12px !important;
    height: 50px;
    font-weight: 700;
    border: none;
}

div.stButton > button:hover {
    background: #4f46e5 !important;
    color: white !important;
}

/* SECTION HEADINGS */
h2, h3 {
    color: #1e293b !important;
}

/* NORMAL TEXT */
.stMarkdown p {
    color: #475569;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #64748b !important;
    font-size: 13px;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)



# ---------------- HEADER ----------------

st.markdown(
    '<div class="header">'
    '<div class="hero-icon">🌐</div>'
    '<h1>Lingo<span>Flow</span></h1>'
    '<p>Translate ideas. Connect worlds.</p>'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- LANGUAGES ----------------

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Tamil": "ta"
}


# ---------------- LANGUAGE SELECTION ----------------

col1, col2, col3 = st.columns([5, 1, 5])

with col1:
    source_name = st.selectbox(
        "From",
        list(languages.keys())
    )

with col2:
    st.write("")
    st.write("")
    st.markdown(
        "<div style='text-align:center;font-size:28px;color:#4f46e5;'>⇄</div>",
        unsafe_allow_html=True
    )

with col3:
    target_name = st.selectbox(
        "To",
        list(languages.keys())
    )

source = languages[source_name]
target = languages[target_name]


# ---------------- INPUT ----------------

st.markdown("### ✍️ Your Text")

text = st.text_area(
    "Your text",
    placeholder="Type or paste something here...",
    height=180,
    label_visibility="collapsed"
)


# ---------------- TRANSLATE ----------------

translate_button = st.button("Translate ✨")


if translate_button:

    if text.strip() == "":
        st.warning("Please enter some text to translate.")

    elif source == target:
        st.info("Source and target languages are the same.")

    else:

        try:

            with st.spinner("Translating..."):

                translated = GoogleTranslator(
                    source=source,
                    target=target
                ).translate(text)

            st.markdown(
                """
                <div class="result-box">
                    <div class="result-title">
                        🌍 TRANSLATION
                    </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div style="
                    background-color: #ffffff;
                    color: #111827;
                    padding: 20px;
                    border-radius: 12px;
                    border: 1px solid #c7d2fe;
                    font-size: 22px;
                    line-height: 1.6;
                    margin-top: 10px;
                ">
                    {translated}
                </div>
                """,
                unsafe_allow_html=True
            )


            st.markdown("</div>", unsafe_allow_html=True)

        except Exception:

            st.error(
                "Something went wrong while translating. "
                "Please check your internet connection and try again."
            )


# ---------------- HOW IT WORKS ----------------

st.markdown(
    "<h2 class='how-title'>How LingoFlow Works</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='how-subtitle'>Translate anything in just three easy steps.</p>",
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3)


with step1:
    st.markdown(
        """
        <div class="step">
            <div class="step-number">01 ✍️</div>
            <h3>Write</h3>
            <p>Enter the text you want to translate.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


with step2:
    st.markdown(
        """
        <div class="step">
            <div class="step-number">02 🌍</div>
            <h3>Choose</h3>
            <p>Select the language you want to translate into.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


with step3:
    st.markdown(
        """
        <div class="step">
            <div class="step-number">03 ✨</div>
            <h3>Translate</h3>
            <p>Click the button and get your translation instantly.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        🌐 LingoFlow
        <br><br>
        Built with Python • Streamlit • Google Translator
    </div>
    """,
    unsafe_allow_html=True
)
