from flask import Flask, request
import openai
import os
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API Key
openai.api_key = os.getenv('sk-4f07InOguDO9y2-m2W_ZsycYDghjxN5n7nKrq2_lfuT3BlbkFJ_kTd3gZEWxHQBJr4Cc1q7lhq-B8ixyM2LiZRUPen4A')

# WhatsApp webhook route
@app.route('/demo-reply', methods=['POST'])
def whatsapp_reply():
    # Get the incoming message
    incoming_msg = request.values.get('Body', '').strip()

    # Prepare the OpenAI API request
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=incoming_msg,
        max_tokens=150
    )
    
    # Get GPT's response
    gpt_reply = response.choices[0].text.strip()

    # Prepare Twilio response
    twilio_resp = MessagingResponse()
    twilio_resp.message(gpt_reply)

    return str(twilio_resp)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
