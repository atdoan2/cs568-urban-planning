from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("fine_tuned_model")
model = GPT2LMHeadModel.from_pretrained("fine_tuned_model")

# Define a function to interact with the model
def ask_question(question, max_length=50, temperature=0.7, top_k=50):
    input_text = "Question: " + question + " Answer:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate answer with adjusted temperature
    output = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,  # Adjusted temperature parameter
        top_k=top_k,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        num_return_sequences=1,
    )

    # Decode and return the answer
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer

# Main loop to interact with the model
while True:
    question = input("Ask a question (type 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    else:
        # Default temperature value
        temperature = 0.7
        response = ask_question(question, temperature=temperature)
        
        # If no response generated, lower the temperature to force a response
        if not response:
            temperature = 0.5  # Lower temperature for less randomness
            response = ask_question(question, temperature=temperature)
            # Indicate that the response is generated with a lower temperature
            response = f"[Lower Temperature Response] {response}"
        
        print("Response:", response)
