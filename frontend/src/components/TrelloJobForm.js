import React, { useState } from 'react';
import axios from 'axios';

const TrelloJobForm = () => {
  const [trelloToken, setTrelloToken] = useState('');
  const [boardId, setBoardId] = useState('');
  const [participants, setParticipants] = useState('');
  const [error, setError] = useState(null);

  const submitForm = async (e) => {
    e.preventDefault();
    
    const participantList = participants.split(',').map(email => email.trim());
    
    try {
      await axios.post('http://localhost:5001/start-job', {
        trelloToken,
        boardId,
        participants: participantList,
      });
      alert('Job started successfully');
      setError(null);
    } catch (error) {
      setError('An error occurred while starting the job.');
      console.error(error);
    }
  };

  return (
    <div>
      {error && <div className="error">{error}</div>}
      <form onSubmit={submitForm}>
        <label>
          Trello Token:
          <input
            type="text"
            value={trelloToken}
            onChange={(e) => setTrelloToken(e.target.value)}
          />
        </label>
        <label>
          Trello Board ID:
          <input
            type="text"
            value={boardId}
            onChange={(e) => setBoardId(e.target.value)}
          />
        </label>
        <label>
          Participants (comma separated emails):
          <input
            type="text"
            value={participants}
            onChange={(e) => setParticipants(e.target.value)}
          />
        </label>
        <button type="submit">Start Job</button>
      </form>
    </div>
  );
};

export default TrelloJobForm;
