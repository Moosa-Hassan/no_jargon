from config import GEMINI_API_KEY
from google import genai

## simple module to explain a text

client = genai.Client(api_key=GEMINI_API_KEY)


def explain_text(mode,text):
    system_prompt = f"""
    Rewrite provided text such that an everyday person would be able to understand it.
    Guidelines:
    1- Use simple, everyday words.
    2- Avoid jargon, technical terms and  complex words.
    3- Preserve the orignal meaning fully intact.
    4- Adjust level of simplify according to selected mode:
        - very simple : understandable by a middle school studnet
        - simple : understandable by a high school studnet.
        - normal : understandable by the average adult.
    5- If text contains technical terms, explain in plain language.
    6- Do not add new information.
    7- Do not remove important information.
    8- Keep tone neutral and clear.
    
    Rewrite the following text: {text}
    Mode : {mode}    
    """
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=system_prompt
    ) # a request send to gemini
    return response.text