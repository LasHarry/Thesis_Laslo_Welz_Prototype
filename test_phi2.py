import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

if torch.cuda.is_available():
    device = torch.device("cuda")
    torch.cuda.set_device(0)  # Set the GPU device (change the index according to your system)
    torch.cuda.device(device)  # Set the default CUDA device
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU instead.")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype=torch.float32, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

query = 'Instruction: Which is the best open-source Large Language Model?'


inputs = tokenizer(query, return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_length=500)
text = tokenizer.batch_decode(outputs)[0]
print(text)
