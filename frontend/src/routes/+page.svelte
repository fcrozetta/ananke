<script lang="ts">
	import { onMount } from 'svelte';
	import { selectedPage } from '../stores/pageSelectionStore';
	import Calendar from './components/calendar.svelte';

	let selectedPage_value: string;
	selectedPage.subscribe((value) => (selectedPage_value = value));

	onMount(() => {
		selectedPage.set('home');
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Crozetta's mind" />
</svelte:head>
<Calendar />

<style>
</style>
