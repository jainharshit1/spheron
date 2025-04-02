import streamlit as st
import time
import json

# Dummy evaluation metrics (simulate using your actual evaluation metrics later)
dummy_bleu_score = {"bleu": 0.7564}
dummy_rouge_score = {"rouge": {"rouge1": 0.654, "rougeL": 0.632}}

# --- Page Config ---
st.set_page_config(page_title="Fine-Tuning Pipeline Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center;'>Fine-Tuning Pipeline Dashboard</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center; font-size: 16px;'>
      Leverage Spheron’s decentralized GPU network to effortlessly fine-tune your AI models.
    </p>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar Inputs ---
st.sidebar.header("Configuration")
hf_token = st.sidebar.text_input("Hugging Face Token", type="password", help="Enter your Hugging Face token")
model_option = st.sidebar.selectbox("Select Model", options=["", "Llama 3", "Mistral", "SmolLM"], help="Choose the foundation model for fine-tuning")
uploaded_file = st.sidebar.file_uploader("Upload Training Dataset", type=["json", "csv", "jsonl"], help="Upload your training dataset for fine-tuning")

st.sidebar.subheader("Hyperparameter Configuration")
batch_size = st.sidebar.slider("Batch Size", 8, 64, 16, step=8)
learning_rate = st.sidebar.slider("Learning Rate", 0.0001, 0.01, 0.001, step=0.0001, format="%.4f")
epochs = st.sidebar.slider("Epochs", 1, 20, 5, step=1)

if not hf_token:
    st.sidebar.warning("Hugging Face token is required!")
if not model_option:
    st.sidebar.warning("Select a model to fine-tune!")

# --- Main Area ---
st.markdown("## Fine-Tuning Overview")
st.markdown(
    """
    Fine-tuning foundation models is essential for creating domain-specific AI applications. 
    However, the process is often complicated by technical challenges, high computational demands,
    and infrastructure overhead. Our pipeline leverages Spheron’s decentralized GPU network to streamline 
    the process, making customization accessible for all developers.
    """,
    unsafe_allow_html=True,
)

# --- Start Fine-Tuning Button ---
start_btn = st.button("Start Fine-Tuning", key="start")

if start_btn:
    # Check required fields
    if not hf_token or not model_option or not uploaded_file:
        st.error("Please fill in all required fields!")
    else:
        st.info("Starting fine-tuning pipeline...")
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Simulate dummy backend processing for fine-tuning
        for percent in range(0, 101, 10):
            time.sleep(1)  # simulate processing delay
            progress_bar.progress(percent)
            status_text.text(f"Processing... {percent}% complete")
        status_text.text("Finalizing fine-tuning process...")
        time.sleep(2)

        # --- Simulate Data Processing ---
        try:
            file_content = uploaded_file.getvalue().decode("utf-8")
            # Dummy reading: assume each line is a valid JSON record
            val_data = [json.loads(line.strip()) for line in file_content.splitlines() if line.strip()]
        except Exception as e:
            
            # st.error(f"Error reading file: {e}")
            val_data = []
        
        if not val_data:
            # st.warning("No valid data found. Using dummy data for demonstration.")
            val_data = [
                {"essay": "The quick brown fox jumps over the lazy dog.", "description": "A swift animal in action."},
                {"essay": "A journey of a thousand miles begins with a single step.", "description": "Emphasizes the importance of starting."}
            ]
        
        # --- Simulate Model Generation Process ---
        sample_inputs = [item["essay"] for item in val_data]
        references = [[item["description"]] for item in val_data]  # for BLEU format
        
        st.info("Simulating text generation and evaluation...")
        predictions = []
        for text in sample_inputs:
            time.sleep(0.5)  # simulate generation delay per sample
            # Dummy generation: just append a text snippet
            predictions.append(text + " [generated sample]")
        
        # Simulate evaluation: In a real scenario, you would compute these metrics.
        st.success("Fine-tuning complete. Model evaluated successfully.")

        # --- Display Evaluation Metrics ---
        st.markdown("## Evaluation Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Validation Loss", "0.234", delta=None)
        col2.metric("Perplexity", "12.45", delta=None)
        col3.metric("Token-Level Accuracy", "98%", delta=None)
        st.markdown(f"**BLEU Score:** {dummy_bleu_score['bleu']:.4f}")
        st.markdown(f"**ROUGE Score:** {dummy_rouge_score['rouge']}")