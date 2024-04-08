from bardapi import Bard
import openai
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

def call_gemini(query):
   GOOGLE_API_KEY='Gemini_API_KEY'
   genai.configure(api_key=GOOGLE_API_KEY)
   model = genai.GenerativeModel('gemini-pro')
   answer = model.generate_content(query)
   return (answer.text)
def call_bard(query):
   bard = Bard()
   answer = bard.get_answer(query)
   return (answer['content'])
def call_chat_gpt(prompt, model="gpt-3.5-turbo"):
    openai.api_key = 'openai_api_key'
    #print(prompt)
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
         temperature = 0.5 # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]