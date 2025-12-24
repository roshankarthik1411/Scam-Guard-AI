import streamlit as st
from scam_classifier import build_scam_classifier_chain
from scam_news import fetch_scam_news


st.set_page_config(
    page_title="ScamGuard AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ ScamGuard AI")
st.subheader("Detect scam messages using Generative AI")

st.write(
    "Paste a message below to check whether it is a scam, not a scam, or uncertain."
)

# ---------- GLOBAL SLIDER (always visible) ----------
st.markdown("### 📰 Related Safety & Scam News Settings")

max_results = st.slider(
    "Number of news articles",
    min_value=0,
    max_value=10,
    value=5,
    step=1
)

st.divider()

# ---------- USER INPUT ----------
user_input = st.text_area(
    "Enter message",
    height=150,
    placeholder="Example: Your bank account will be suspended. Click this link immediately."
)

if st.button("Analyze Message"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner("Analyzing..."):
            chain = build_scam_classifier_chain()
            result = chain.invoke(
                {"user_message": user_input}
            )

        st.success("Analysis Complete")

        # ---------- RESULTS ----------
        st.markdown("### 🔍 Classification")
        st.write(result.classification)

        st.markdown("### 🎯 Intent")
        st.write(result.intent_type)

        st.markdown("### 🧠 Reasoning")
        st.write(result.reasoning)

        # ---------- NEWS SECTION (works for scam + not scam) ----------
        if max_results > 0:
            st.markdown("### 📰 Related News")

            # intent_type is a LIST → extract safely
            intent_value = result.intent_type[0] if result.intent_type else ""

            if result.classification.lower() == "scam" and intent_value:
                search_term = intent_value.replace("_", " ")
            else:
                search_term = user_input

            news = fetch_scam_news(
                search_term,
                max_results=max_results
            )

            if not news:
                st.info("No related news articles found.")
            else:
                if result.classification.lower() != "scam":
                    st.info(
                        "ℹ️ This message is not classified as a scam. "
                        "Showing general safety-related news for awareness."
                    )

                for item in news:
                    st.markdown(f"**{item['title']}**")
                    st.write(item["content"][:300] + "...")
                    st.markdown(f"[Read more]({item['url']})")
                    st.divider()
