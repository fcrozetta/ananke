<script lang="ts">
	import { onMount } from 'svelte';
	import { selectedPage } from '../../../stores/pageSelectionStore';
	import { InternalAPI } from '../../../services/internalAPI';

	let api = new InternalAPI();

	let selectedPage_value: string;
	selectedPage.subscribe((value) => (selectedPage_value = value));

	onMount(() => {
		selectedPage.set('spiders - azure');
	});
</script>

<svelte:head>
	<title>Spiders - Azure</title>
	<meta name="description" content="getting release notes form azure sdk" />
</svelte:head>

<div class="flow-root">
	<ul role="list" class="-mb-8">
		{#await api.runSpider('azurecli')}
			<p>loading...</p>
		{:then data}
			{#each Object.entries(data) as [version, contents]}
				<h2>{version} - {contents['_release_date']}</h2>
				{#each Object.entries(contents) as [key, value]}
					{#if key != '_release_date'}
						<h3>{key}</h3>
						<ul>
							{#each value as v}
								<!-- Rendering the list as HTML to use the <code> tags in the lists -->
								<li>{@html v}</li>
							{/each}
						</ul>
					{/if}
				{/each}
			{/each}
		{/await}
		<li>
			<div class="relative pb-8">
				<span class="absolute left-4 top-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true" />

				<div class="relative flex space-x-3">
					<div>
						<span
							class="flex h-8 w-8 items-center justify-center rounded-full bg-green-500 ring-8 ring-white"
						>
							<svg
								class="h-5 w-5 text-white"
								viewBox="0 0 20 20"
								fill="currentColor"
								aria-hidden="true"
							>
								<path
									fill-rule="evenodd"
									d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z"
									clip-rule="evenodd"
								/>
							</svg>
						</span>
					</div>
					<div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
						<div>
							<p class="text-sm text-gray-500">
								Applied to <a href="#" class="font-medium text-gray-900">Front End Developer</a>
							</p>
						</div>
						<div class="whitespace-nowrap text-right text-sm text-gray-500">
							<time datetime="2020-09-20">Sep 20</time>
						</div>
					</div>
				</div>
			</div>
		</li>

		<li>
			<div class="relative pb-8">
				<div class="relative flex space-x-3">
					<div>
						<span
							class="flex h-8 w-8 items-center justify-center rounded-full bg-gray-400 ring-8 ring-white"
						>
							<svg
								class="h-5 w-5 text-white"
								viewBox="0 0 20 20"
								fill="currentColor"
								aria-hidden="true"
							>
								<path
									fill-rule="evenodd"
									d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z"
									clip-rule="evenodd"
								/>
							</svg>
						</span>
					</div>
					<div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
						<div>
							<p class="text-sm text-gray-500">
								Completed interview with <a href="#" class="font-medium text-gray-900"
									>Katherine Snyder</a
								>
							</p>
						</div>
						<div class="whitespace-nowrap text-right text-sm text-gray-500">
							<time datetime="2020-10-04">Oct 4</time>
						</div>
					</div>
				</div>
			</div>
		</li>
	</ul>
</div>

<style>
</style>
