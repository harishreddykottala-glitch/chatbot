from flask import Flask, request, render_template
from google import genai
from google.genai import types

client = genai.Client(
    api_key="AIzaSyB5UzcM-fntJvFLRdAq1heC3cS9tIA_byE"
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat",methods=['GET','POST'])
def chat():
    user_message = request.json.get('message')
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Part.from_text(text= user_message ),
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    ),
)
    return response.text

if __name__ == "__main__":
    app.run(port=5000, debug=False)
