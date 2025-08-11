from flask import Flask, request, jsonify
from backend.llm_reply import generate_summary_and_reply
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route('/process-email', methods=['POST'])
def process_email():
    data = request.json
    subject = data.get('subject')
    body = data.get('body')

    urgency, summary, reply = generate_summary_and_reply(subject, body)

    return jsonify({
        'urgency': urgency,
        'summary': summary,
        'reply': reply
    })

if __name__ == '__main__':
    app.run(debug=True)
