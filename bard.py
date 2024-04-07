from bardapi import Bard
import openai
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

def call_gemini(query):
   GOOGLE_API_KEY='AIzaSyCGGVSjIAMmr9tIJ6Bb0VilDcGNTx2bdvY'
   genai.configure(api_key=GOOGLE_API_KEY)
   model = genai.GenerativeModel('gemini-pro')
   answer = model.generate_content(query)
   return (answer.text)
def call_bard(query):
   bard = Bard()
   answer = bard.get_answer(query)
   return (answer['content'])
def call_chat_gpt(prompt, model="gpt-3.5-turbo"):
    openai.api_key = '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'
    #print(prompt)
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
         temperature = 0.5 # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]