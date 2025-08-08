from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_summary_and_reply(subject, body):
    prompt = f"""
    Subject: {subject}
    Body: {body}
    ---
    Classify the urgency of the email in High or Normal or Low, summarize the intent of the email in one sentence and generate a reply accordingly.
    Format:
    Urgency: <urgency>
    Summary: <summary>
    Reply: <reply>
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional email assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    try:
        urgency = content.split("Urgency:")[1].split("Summary:")[0].strip()
        summary = content.split("Summary:")[1].split("Reply:")[0].strip()
        reply = content.split("Reply:")[1].strip()
    except:
        summary = "Could not parse summary."
        reply = "Could not parse reply."

    return urgency, summary, reply
