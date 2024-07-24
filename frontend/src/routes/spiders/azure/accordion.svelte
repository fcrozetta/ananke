<script>
	export let open = true;
	import { slide } from 'svelte/transition';
	const handleClick = () => (open = !open);
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions a11y-no-static-element-interactions -->
<div class="accordion" on:click={handleClick}>
	<div class="header">
		<slot name="head"></slot>
	</div>
</div>
{#if open}
	<div class="details" transition:slide>
		<slot name="details"></slot>
	</div>
{/if}

<style>
</style>
