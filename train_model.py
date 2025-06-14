from transformers import AutoModelForCausalLM, Trainer, TrainingArguments, AutoTokenizer
from datasets import load_from_disk
\
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenized_dataset = load_from_disk("./my_finetuned_gpt2_datasets")  # change path as needed

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
model.save_pretrained("./my_finetuned_gpt2")

