from pathlib import Path

from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser

from dataset_loader import load_scam_dataset, build_few_shot_examples
from prompt import scam_detection_prompt
from schema import ScamDetectionResult
from config import GOOGLE_API_KEY


# ---------- PATH SETUP (CROSS-PLATFORM & SAFE) ----------
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset.csv"


def build_scam_classifier_chain():
    # ---- Load dataset ----
    if not DATASET_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATASET_PATH}")

    examples = load_scam_dataset(DATASET_PATH)
    few_shot_text = build_few_shot_examples(examples)

    # ---- LLM ----
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=GOOGLE_API_KEY,
    )

    # ---- Output parser ----
    parser = PydanticOutputParser(
        pydantic_object=ScamDetectionResult
    )

    # ---- Prompt ----
    prompt = scam_detection_prompt.partial(
        few_shot_examples=few_shot_text,
        format_instructions=parser.get_format_instructions(),
    )

    # ---- Chain ----
    chain = prompt | llm | parser
    return chain
