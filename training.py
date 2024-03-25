from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import torch

class MyDataset(Dataset):
    def __init__(self, csv_file, tokenizer, max_length, max_rows=1000):
        self.data = pd.read_csv(csv_file, nrows=max_rows)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = str(self.data.iloc[idx, 0])
        inputs = self.tokenizer(text, padding="max_length", truncation=True, max_length=self.max_length, return_tensors="pt")
        return inputs

# Load pre-trained GPT model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token  # Set padding token to end of sentence token

# Fine-tuning parameters
epochs = 3
learning_rate = 5e-5
batch_size = 4
max_length = 128

# Load data and create DataLoader
dataset = MyDataset('Traffic_Crashes_-_Crashes_20240317.csv', tokenizer, max_length, max_rows=1000)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Load pre-trained GPT model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Fine-tuning loop
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

iteration = 0
for epoch in range(epochs):
    for batch in dataloader:
        inputs = batch["input_ids"].to(device)
        labels = batch["input_ids"].to(device)
        
        outputs = model(inputs, labels=labels)
        loss = outputs.loss

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        
        iteration += 1
        if iteration % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Iteration [{iteration}], Loss: {loss.item()}")

    print(f"Epoch [{epoch+1}/{epochs}] completed.")

# Save the fine-tuned model and tokenizer
model.save_pretrained("fine_tuned_model")
tokenizer.save_pretrained("fine_tuned_model")
