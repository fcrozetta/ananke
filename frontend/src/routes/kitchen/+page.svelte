<script lang="ts">
	import { writable } from 'svelte/store';
	import { SvelteFlow, Controls, Background, BackgroundVariant, MiniMap } from '@xyflow/svelte';
	import ColorPickerNode from './components/flow/colorPickerNode.svelte';
	import StartNode from './components/flow/startNode.svelte';

	// 👇 this is important! You need to import the styles for Svelte Flow to work
	import '@xyflow/svelte/dist/style.css';

	const nodeTypes = {
		colorPicker: ColorPickerNode,
		start: StartNode
	};

	// We are using writables for the nodes and edges to sync them easily. When a user drags a node for example, Svelte Flow updates its position.
	const nodes = writable([
		{
			id: '0',
			type: 'start',
			position: { x: -200, y: 0 }
		},
		{
			id: '1',
			type: 'input',
			data: { label: 'Input Node' },
			position: { x: 0, y: 0 }
		},
		{
			id: '2',
			type: 'default',
			data: { label: 'Node' },
			position: { x: 0, y: 150 }
		},
		{
			id: '3',
			type: 'colorPicker',
			data: { color: writable('#ff4000') },
			position: { x: 160, y: 0 }
		}
	]);

	// same for edges
	const edges = writable([
		{
			id: '1-2',
			type: 'default',
			source: '1',
			target: '2',
			label: 'Edge Text'
		}
	]);

	let nodes_value;
	nodes.subscribe((value) => (nodes_value = value));

	function exportFlow() {
		let flow = {
			nodes: JSON.stringify(nodes_value)
		};
		// console.log(nodes_value);
		console.log(flow);
	}
	const snapGrid = [25, 25];
</script>

<!--
👇 By default, the Svelte Flow container has a height of 100%.
This means that the parent container needs a height to render the flow.

I am using 45 rem cause it looks OK in both laptop and external display
-->
<div style:height="45rem">
	<button type="button" class="w-full bg-green-500 text-yellow-100" on:click={exportFlow}
		>Export Flow</button
	>
	<SvelteFlow
		{nodeTypes}
		{nodes}
		{edges}
		{snapGrid}
		fitView
		on:nodeclick={(event) => console.log('on node click', event.detail.node)}
	>
		<Controls />
		<Background variant={BackgroundVariant.Dots} />
		<MiniMap />
	</SvelteFlow>
</div>
