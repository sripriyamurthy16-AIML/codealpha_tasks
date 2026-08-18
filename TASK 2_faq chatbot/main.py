import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="FAQFlow",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #f4f6ff;
}

.block-container {
    max-width: 850px;
    padding-top: 3rem;
}

h1 {
    color: #312e81 !important;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #475569;
    font-size: 17px;
    margin-bottom: 30px;
}

label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

textarea,
input {
    color: #1e293b !important;
    background-color: white !important;
}

div.stButton > button {
    width: 100%;
    background-color: #6366f1 !important;
    color: white !important;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 700;
}

div.stButton > button:hover {
    background-color: #4f46e5 !important;
}

.answer-box {
    background-color: white;
    color: #1e293b;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #c7d2fe;
    margin-top: 20px;
    line-height: 1.6;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 45px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.title("🤖 FAQFlow")

st.markdown(
    '<div class="subtitle">'
    'Ask a question and get the most relevant answer using NLP.'
    '</div>',
    unsafe_allow_html=True
)

# ---------------- FAQ DATA ----------------

faqs = {
    "What is cloud computing?":
        "Cloud computing is the delivery of computing services such as servers, storage, databases, networking and software over the Internet.",

    "What are the benefits of cloud computing?":
        "The main benefits of cloud computing include scalability, flexibility, cost savings, easy access and reduced infrastructure maintenance.",

    "What is SaaS?":
        "SaaS stands for Software as a Service. It allows users to access software applications through the Internet without installing them locally.",

    "What is IaaS?":
        "IaaS stands for Infrastructure as a Service. It provides virtualized computing resources such as servers, storage and networking.",

    "What is PaaS?":
        "PaaS stands for Platform as a Service. It provides developers with a platform to build, test and deploy applications.",

    "Is cloud computing secure?":
        "Cloud computing can be secure when proper security measures such as authentication, encryption and access control are implemented.",

    "What is cloud storage?":
        "Cloud storage allows users to store and access their data on remote servers through the Internet.",

    "What is a public cloud?":
        "A public cloud provides computing resources to multiple customers through a cloud service provider.",

    "What is a private cloud?":
        "A private cloud is a cloud environment dedicated to a single organization.",

    "What is a hybrid cloud?":
        "A hybrid cloud combines public cloud services with private cloud infrastructure."
}

questions = list(faqs.keys())
answers = list(faqs.values())

# ---------------- TEXT PREPROCESSING ----------------

stop_words = set(stopwords.words("english"))


def preprocess(text):
    tokens = word_tokenize(text.lower())

    tokens = [
        word for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    return " ".join(tokens)


processed_questions = [
    preprocess(question)
    for question in questions
]

# ---------------- TF-IDF ----------------

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)

# ---------------- FIND BEST ANSWER ----------------

def get_answer(user_question):

    processed_question = preprocess(user_question)

    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )[0]

    best_index = similarity_scores.argmax()
    best_score = similarity_scores[best_index]

    if best_score < 0.20:
        return (
            "Sorry, I couldn't find a suitable answer. "
            "Please try asking about cloud computing, "
            "SaaS, IaaS, PaaS, cloud storage or cloud security."
        )

    return answers[best_index]


# ---------------- USER INPUT ----------------

st.markdown("### 💬 Ask your question")

user_question = st.text_input(
    "Question",
    placeholder="Example: What are the benefits of cloud computing?",
    label_visibility="collapsed"
)

# ---------------- BUTTON ----------------

if st.button("Get Answer ✨"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:

        answer = get_answer(user_question)

        st.markdown("### 🤖 FAQFlow")

        st.markdown(
            f"""
            <div class="answer-box">
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        🤖 FAQFlow<br><br>
        Built with Python • Streamlit • NLTK • TF-IDF • Cosine Similarity
    </div>
    """,
    unsafe_allow_html=True
)
