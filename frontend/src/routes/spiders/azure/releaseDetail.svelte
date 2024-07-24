<script lang="ts">
	import Accordion from './accordion.svelte';
	export let version: string;
	export let content: any;

	export let showModal: boolean; // boolean

	let dialog: HTMLDialogElement; // HTMLDialogElement

	$: if (dialog && showModal) dialog.showModal();

	function splitChangeLogLine(line: string) {
		let splitLines = line.split(':');
		if (splitLines.length > 2) {
			return [splitLines.slice(0, 2).join(':'), splitLines.slice(2).join(':')];
		} else {
			return splitLines;
		}
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div on:click|stopPropagation>
		<slot name="header" />
		<hr />
		<div class="relative z-10 w-60" aria-labelledby="modal-title" role="dialog" aria-modal="true">
			<div
				class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
				aria-hidden="true"
			></div>

			<div class="fixed inset-0 z-10 w-screen overflow-y-auto">
				<div
					class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
				>
					<!-- Here to set size of modal -->
					<div
						class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:p-6 w-4/5"
					>
						<div>
							<div
								class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-green-100"
							>
								<svg
									class="h-6 w-6 text-green-600"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									aria-hidden="true"
								>
									<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
								</svg>
							</div>
							<div class="mt-3 text-center sm:mt-5">
								<h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">
									{version}
								</h3>
								{#each Object.entries(content) as [key, value]}
									{#if key != '_release_date'}
										<Accordion>
											<div class="relative mb-3 hover:bg-gray-100" slot="head">
												<h6 class="mb-0">
													<button
														class="relative flex items-center w-full p-4 font-semibold text-left transition-all ease-in border-b border-solid cursor-pointer border-slate-100 text-slate-700 rounded-t-1 group text-dark-500"
														data-collapse-target="collapse-1"
													>
														<span>{key}</span>
														<i class="absolute right-0 pt-1 text-xs fa fa-plus group-open:opacity-0"
														></i>
														<i
															class="absolute right-0 pt-1 text-xs opacity-0 fa fa-minus group-open:opacity-100"
														></i>
													</button>
												</h6>
											</div>
											<div slot="details">
												<dl class="divide-y divide-gray-100">
													{#each value as v}
														<dl class="divide-y divide-gray-100">
															<div
																class="bg-gray-50 px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-3"
															>
																<dt class="text-sm leading-6 text-gray-900 font-bold">
																	{@html splitChangeLogLine(v)[0]}
																</dt>
																<dd
																	class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0"
																>
																	{@html splitChangeLogLine(v)[1]}
																</dd>
															</div>
														</dl>
													{/each}
												</dl>
											</div>
										</Accordion>
									{/if}
								{/each}
							</div>
						</div>
						<div class="mt-5 sm:mt-6">
							<button
								on:click={() => dialog.close()}
								type="button"
								class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
								>Close</button
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</dialog>
<!-- -->
