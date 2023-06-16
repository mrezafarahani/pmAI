import requests
from dateutil.parser import parse
import openai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
TRELLO_API_BASE_URL = 'https://api.trello.com/1/'

def get_trello_board_tickets(trello_token, board_id):
    url = f'{TRELLO_API_BASE_URL}boards/{board_id}/cards'
    params = {'key': trello_token, 'fields': 'name,due'}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception if the request failed

    tickets = response.json()
    return tickets

def schedule_meeting(tickets):
    # Generate the agenda using the ChatGPT API
    print("In schedule Metting")
    print(tickets)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'I need to schedule a sprint planning meeting for these Trello tickets. Can you help me draft an agenda for this meeting? Tickets are {tickets}',
        temperature=0.5,
        max_tokens=100
    )

    agenda = response.choices[0].text.strip()

    print(f'Meeting Agenda:\n{agenda}')

def agenda(trello_token, board_id, participants):
    tickets = get_trello_board_tickets(trello_token, board_id)
    schedule_meeting(tickets)
    # for ticket in tickets:
    #     ticket_name = ticket['name']
    #     due_date_str = ticket.get('due')
    #     if due_date_str is not None:
    #         due_date = parse(due_date_str)
    #         schedule_meeting(ticket_name, due_date, participants)


@app.route('/start-job', methods=['POST'])
def start_job():
    data = request.get_json()
    print(data['trelloToken'])
    print(data['boardId'])
    print(data['participants'])
    agenda(data['trelloToken'], data['boardId'], data['participants'])

    # Here, you'd add the logic to handle the Trello API token, board ID,
    # and participants list, start the job to schedule meetings based on 
    # Trello tickets, and send invitations to the participants.

    # You may also want to add error handling code here to ensure that 
    # all required data was provided and is valid.

    return jsonify({'message': 'Job started successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
