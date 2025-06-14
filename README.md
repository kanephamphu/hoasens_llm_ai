# Fine-Tuning GPT-2 for News Generation

This project fine-tunes the GPT-2 language model on a news dataset for conditional text generation.

## 📁 Project Structure
---
├── news_dataset.jsonl # Training data (one JSON object per line, with "text" key)
├── hoasens_tokenize.py # Tokenizes dataset and saves to disk
├── train_model.py # Fine-tunes GPT-2 using Hugging Face Trainer
├── train_llm.sh # Script to launch training
├── evaluate.py # Inference script to generate text
├── my_finetuned_gpt2/ # Saved model output after training
├── my_finetuned_gpt2_datasets/ # Tokenized dataset
├── my_finetuned_gpt2_tokenizer/ # Tokenizer config
└── README.md
---

## 🔧 Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

🚀 Train the Model
```
./train_llm.sh
```

📊 Evaluate the Model
```
python3 evaluate.py
```