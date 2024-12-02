<script>
	import { getHello, connectToWebSocket } from '../../services/moirai';
	let message = '';
	let jobId = '';
	let socket = null;
	let wsMessages = [];

	async function handleButtonClick() {
		try {
			const response = await getHello();
			message = `Hello received: ${JSON.stringify(response)}`;
			jobId = response.job_id;
			socket = connectToWebSocket(jobId);

			socket.onmessage = (event) => {
				wsMessages = [...wsMessages, event.data];
			};
		} catch (error) {
			console.error('Error:', error);
		}
	}
</script>

<main>
	<h1>Moirai Page</h1>
	<button on:click={handleButtonClick}>Call Hello and Connect</button>
	<p>{message}</p>
	<p>{jobId && `Connected to job ID: ${jobId}`}</p>
	<ul>
		{#each wsMessages as wsMessage}
			<li>{wsMessage}</li>
		{/each}
	</ul>
</main>
