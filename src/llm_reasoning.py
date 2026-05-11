from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_llm_reasoning(account_name):

    prompt = f"""
    You are an accounting AI assistant.

    A trial balance account could not
    be confidently mapped to the chart of accounts.

    Account Name:
    {account_name}

    Provide:
    1. Most likely accounting category
    2. Why this mapping may be uncertain
    3. Whether human review is required

    Keep answer concise and professional.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content