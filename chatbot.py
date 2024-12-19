import openai
import os

# Set your OpenAI API key
openai.api_key = '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'

def generate_custom_response(prompt: str, custom_features: dict):
    try:
        # Use the correct chat-based API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Update to a chat model like "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=custom_features.get("temperature", 0.7),  # Control creativity
            max_tokens=custom_features.get("max_tokens", 150),  # Control response length
            top_p=custom_features.get("top_p", 1),  # Control diversity
            frequency_penalty=custom_features.get("frequency_penalty", 0),  # Penalty for repeated phrases
            presence_penalty=custom_features.get("presence_penalty", 0),  # Penalty for new topics
        )

        # Extract the response text from the response format
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text

    except Exception as e:
        return f"Error: {str(e)}"

def create_dynamic_prompt(user_input):
    return f"""
    You are an assistant designed to help with technical explanations. Provide a clear and concise explanation in simple terms:
    
    User Input: {user_input}
    
    Answer:
    """

# Define the custom features for fine-tuning behavior
custom_features = {
    "temperature": 0.5,  # Set creativity level to medium
    "max_tokens": 200,   # Limit the response length
    "top_p": 1.0,        # Use full token space
    "frequency_penalty": 0,  # No penalty for repetition
    "presence_penalty": 0,   # No penalty for introducing new topics
}

# User input for the LLM
user_input = "Explain the concept of deep learning in simple terms."

# Create a dynamic prompt
prompt = create_dynamic_prompt(user_input)

# Generate the response
response = generate_custom_response(prompt, custom_features)

# Print the response
print("Generated Response:\n", response)
