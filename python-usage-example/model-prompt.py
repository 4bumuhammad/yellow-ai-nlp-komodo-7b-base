import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda:0" if torch.cuda.is_available() else "cpu"

model_dir = "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/komodo-7b-base"

# tokenizer = AutoTokenizer.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True,force_download=True)
tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
# model = AutoModelForCausalLM.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True,force_download=True)
model = AutoModelForCausalLM.from_pretrained(model_dir, local_files_only=True)
model = model.to(device)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

full_prompt = "Candi borobudur adalah"

tokens = tokenizer(full_prompt, return_tensors="pt").to(device)
output = model.generate(tokens["input_ids"], eos_token_id=tokenizer.eos_token_id)

print(tokenizer.decode(output[0], skip_special_tokens=True))
# Candi borobudur adalah candi yang terletak di Magelang, Jawa Tengah.