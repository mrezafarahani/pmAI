import React from 'react';
import TrelloJobForm from './components/TrelloJobForm';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Trello Meeting Scheduler</h1>
      </header>
      <main>
        <TrelloJobForm />
      </main>
    </div>
  );
};

export default App;
