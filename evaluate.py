from transformers import AutoModelForCausalLM, AutoTokenizer

# Load fine-tuned model and tokenizer
model = AutoModelForCausalLM.from_pretrained("./my_finetuned_gpt2")
tokenizer = AutoTokenizer.from_pretrained("./my_finetuned_gpt2_tokenizer")  # Use the saved tokenizer

# GPT-2 requires this if pad_token was not set during pretraining
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

# Input prompt
input_text = "How old are you?"

# Tokenize
inputs = tokenizer(input_text, return_tensors="pt")

# Generate text
output = model.generate(
    **inputs,
    max_new_tokens=300,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    top_k=50
)

# Decode and print result
print(tokenizer.decode(output[0], skip_special_tokens=True))
