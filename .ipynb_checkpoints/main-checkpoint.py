import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_csv("hf://datasets/thomasat/diet-planning/reasoning-dataset.csv")

print(df.head())
print(df["Prompt"][0])

from transformers import GPT2Tokenizer, GPT2Model

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Load the model (GPT-2 Small)
model = GPT2Model.from_pretrained('gpt2')

def tokenize_function(example):
  return tokenizer(example["Prompt"])

tokenized_dataset = df.map(tokenize_function, batched=True, remove_columns=["Prompt"])
tokenized_dataset

#1.4 Step 3: Group Tokens for Language Modeling
block_size = 128

def group_texts(examples):
    concatenated = sum(examples['input_ids'], [])
    concatenated_attention_mask = sum(examples['attention_mask'], [])
    total_length = (len(concatenated) // block_size) * block_size

    result = {
        'input_ids': [concatenated[i:i + block_size] for i in range(0, total_length, block_size)],
        'attention_mask': [concatenated_attention_mask[i:i + block_size] for i in range(0, total_length, block_size)]
    }

    result["labels"] = result["input_ids"].copy()
    return result

lm_dataset = tokenized_dataset.map(group_texts, batched=True)
lm_dataset["train"][0]

# 1.5 Step 4: Load a Pretrained Model for Language Modeling

from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(model_name) # Note: we are using gpt2