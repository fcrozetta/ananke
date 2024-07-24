<script lang="ts">
	import { onMount } from 'svelte';
	import ReleaseDetail from './releaseDetail.svelte';
	import { selectedPage } from '../../../stores/pageSelectionStore';
	import { InternalAPI } from '../../../services/internalAPI';

	let api = new InternalAPI();
	let showModal = false;
	// let selectedPage_value: string;
	// selectedPage.subscribe((value) => (selectedPage_value = value));

	let modalVersion: string;
	let modalContent: any;
	onMount(() => {
		selectedPage.set('spiders - azure');
	});

	function convert_datetime(dt_string: string) {
		let dt = new Date(dt_string);
		return dt.toDateString();
	}

	function open_details(version: string, data: any) {
		modalVersion = version;
		modalContent = data;
		showModal = true;
	}
</script>

<svelte:head>
	<title>Spiders - Azure</title>
	<meta name="description" content="getting release notes form azure sdk" />
</svelte:head>

<div class="flow-root mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
	<ul role="list" class="-mb-8">
		{#await api.runSpider('azurecli')}
			<p>loading...</p>
		{:then data}
			<ul role="list" class="divide-y divide-gray-100">
				{#each Object.entries(data) as [version, contents]}
					<li class="flex items-center justify-between gap-x-6 py-5 px-2 hover:bg-gray-100">
						<div class="min-w-0">
							<div class="flex items-start gap-x-3">
								<p class="text-sm font-semibold leading-6 text-gray-900">{version}</p>
								<!-- <p
									class="mt-0.5 whitespace-nowrap rounded-md bg-red-50 px-1.5 py-0.5 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-600/20"
								>
									Use this to MARK versions with breaking changes
								</p> -->
							</div>
							<div class="mt-1 flex items-center gap-x-2 text-xs leading-5 text-gray-500">
								<p class="whitespace-nowrap">
									Released on <time datetime={contents['_release_date']}>
										{convert_datetime(contents['_release_date'])}
									</time>
								</p>
							</div>
						</div>
						<div class="flex flex-none items-center gap-x-4">
							<button
								on:click={() => {
									open_details(version, contents);
								}}
								class="hidden rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:block"
								>View release</button
							>
						</div>
					</li>
				{/each}
			</ul>
		{/await}
	</ul>
</div>

<!-- TODO: Prevent doing the check twice -->
{#if showModal}
	<ReleaseDetail bind:showModal version={modalVersion} content={modalContent}></ReleaseDetail>
{/if}

<style>
</style>
