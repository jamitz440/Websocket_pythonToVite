import { useState } from 'react';
import useWebSocket from './useWebSocket';

const App = () => {
    const { numbers, echoes, sendMessage } = useWebSocket('ws://localhost:8765');
    const [input, setInput] = useState('');

    const handleSend = () => {
      if(input !== ""){
        sendMessage('echo', input);}
        setInput('');
    };

    const handleStart = () => {
        sendMessage("button", 'start');
    };

    const handleStop = () => {
        sendMessage("button", 'stop');
    };

    return (
        <div>
            <h1>WebSocket Real-Time Updates</h1>
                  <input
                      type="text"
                      value={input}
                      onChange={(e) => setInput(e.target.value)}
                      placeholder="Type a message"
                  />
                  <button onClick={handleSend}>Send Echo</button>
                  <button onClick={handleStart}>Start</button>
                  <button onClick={handleStop}>Stop</button>
            <div>
                <h2>Numbers</h2>
                <ul>
                    {numbers.map((num, index) => (
                        <li key={`num-${index}`}>{num}</li>
                    ))}
                </ul>
            </div>
            <div>
                <h2>Echo Messaes</h2>
                <ul>
                    {echoes.map((msg, index) => (
                        <li key={`echo-${index}`}>{msg}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default App;
