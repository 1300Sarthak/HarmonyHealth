from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    file_path = 'messages.json'
    with open(file_path, 'r') as file:
        messages = json.load(file)

    questions = [
        "Can you remember three words: apple, table, and penny? I will ask you to recall them later.",
        "What did you have for breakfast today?",
        "Can you tell me about your childhood?",
        "Who was the first president of the United States?",
        "How are you feeling today?",
        "Do you feel anxious or stressed frequently?",
        "Have you noticed any changes in your behavior or personality recently?",
        "Can you recall the three words I asked you to remember earlier?"
    ]

    qa_dict = {}

    for i in range(len(messages)):
        if (messages[i]['type'] == 'assistant_message' and messages[i]['message']['content'] in questions):
            question = messages[i]['message']['content']
            # Check if the next message is a user response
            if messages[i + 1]['type'] == 'user_message':
                answer = messages[i + 1]['message']['content']
                emotion_scores = messages[i + 1]['models']['prosody']['scores']
                first_3_emotions = dict(list(emotion_scores.items())[:3])
                # Store the question as key and answer as value along with emotions
                qa_dict[question] = {
                    'answer': answer,
                    'emotions': first_3_emotions
                }

    return jsonify(qa_dict)

if __name__ == '__main__':
    app.run(debug=True)