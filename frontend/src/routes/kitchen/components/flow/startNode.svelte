<script lang="ts">
	import type { Writable } from 'svelte/store';
	import { Handle, Position, type NodeProps } from '@xyflow/svelte';

	type $$Props = NodeProps;
</script>

<div class="start">
	<div>
		<h1>Start</h1>
	</div>
	<Handle type="source" position={Position.Right} />
</div>

<style>
	.start {
		padding: 1rem;
		background: #eee;
		border-radius: 0.125rem;
		font-size: 0.7rem;
		color: green;
	}
</style>
