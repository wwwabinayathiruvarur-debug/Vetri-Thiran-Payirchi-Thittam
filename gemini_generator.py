import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)


class GeminiDocumentGenerator:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-3.8-flash")

    def generate_document(self, document_type, parties, terms, dates):

        prompt = f"""
Create a professional legal document.

Document Type:
{document_type}

Parties:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Generate a well-structured document with:
1. Title
2. Parties
3. Effective Date
4. Terms and Conditions
5. Responsibilities
6. Confidentiality where appropriate
7. Termination where appropriate
8. Signature section

Use clear and formal language.
Do not invent important facts that were not provided.
"""

        response = self.model.generate_content(prompt)

        return response.text