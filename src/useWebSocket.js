import { useEffect, useState } from 'react';

const useWebSocket = (url) => {
    const [socket, setSocket] = useState(null);
    const [numbers, setNumbers] = useState([]);
    const [echoes, setEchoes] = useState([]);

    useEffect(() => {
        const ws = new WebSocket(url);
        setSocket(ws);

        ws.onopen = () => {
            console.log('WebSocket connection opened');
        };

        ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            console.log('Received message from server:', message);

            switch (message.type) {
                case 'number':
                    setNumbers(prevNumbers => [...prevNumbers, message.data]);
                    break;
                case 'echo':
                    setEchoes(prevEchoes => [...prevEchoes, message.data]);
                    break;
                default:
                    console.log('Unknown message type:', message.type);
            }
        };

        ws.onclose = () => {
            console.log('WebSocket connection closed');
        };

        ws.onerror = (error) => {
            console.log('WebSocket error:', error);
        };

        return () => {
            ws.close();
        };
    }, [url]);

    const sendMessage = (type, data) => {
        if (socket) {
            socket.send(JSON.stringify({ type, data }));
        }
    };

    return { numbers, echoes, sendMessage };
};

export default useWebSocket;
