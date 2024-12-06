from openai import OpenAI
from app.config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)


class Generator:
    def generate_answer(self, query, context):
        # Construct the prompt
        prompt = (
            f"Context: {context}\n\n"
            f"Question: {query}\n"
            f"Answer:"
        )
        
        # Call the OpenAI ChatCompletion API
        response =  client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with a valid model, e.g., "gpt-4" or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.8
        )
        
        # Extract the response content
        return response.choices[0].message