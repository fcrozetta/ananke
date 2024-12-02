const BASE_URL = 'http://localhost:8000/moirai';

export const getHello = async (): Promise<{ job_id: string }> => {
	try {
		const response = await fetch(`${BASE_URL}/hello`);
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		const data = await response.json();
		return data;
	} catch (error) {
		console.error('Error fetching hello:', error);
		throw error;
	}
};

export const connectToWebSocket = (jobId: string): WebSocket => {
	const socket = new WebSocket(`ws://localhost:8000/moirai/${jobId}`);

	socket.onopen = () => {
		console.log('WebSocket connection opened');
	};

	socket.onmessage = (event) => {
		try {
			const message = JSON.parse(event.data);
			console.log('WebSocket JSON message received:', message);
		} catch (e) {
			console.log('WebSocket text message received:', event.data);
		}
	};

	socket.onerror = (error) => {
		console.error('WebSocket error:', error);
	};

	socket.onclose = () => {
		console.log('WebSocket connection closed');
	};

	return socket;
};
