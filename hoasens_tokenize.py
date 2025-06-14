from datasets import load_dataset
from transformers import AutoTokenizer

# Load JSONL dataset
dataset = load_dataset("json", data_files="news_dataset.jsonl", split="train")

# Load and configure tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # GPT2 doesn't have pad token by default

# Tokenization function
def tokenize_fn(example):
    tokens = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=512,
    )
    tokens["labels"] = tokens["input_ids"].copy()  # Add labels for training
    return tokens

# Apply tokenization
tokenized_dataset = dataset.map(tokenize_fn, batched=True, remove_columns=["text"])

# ✅ Save tokenized dataset to disk (for Trainer)
tokenized_dataset.save_to_disk("./my_finetuned_gpt2_datasets")

# ✅ Save tokenizer for reuse
tokenizer.save_pretrained("./my_finetuned_gpt2_tokenizer")
