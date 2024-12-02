<script lang="ts">
	import '../app.css';
	import { selectedPage } from '../stores/pageSelectionStore';

	let selectedPage_value: string;
	selectedPage.subscribe((value) => (selectedPage_value = value));
</script>

<html lang="en" class="h-full">
	<body class="h-full">
		<div class="min-h-full">
			<nav class="border-b border-gray-200 bg-white">
				<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
					<div class="flex h-16 justify-between">
						<div class="flex">
							<div class="flex flex-shrink-0 items-center">
								<img
									class="hidden h-20 w-auto lg:block"
									src="/src/lib/images/wizard.png"
									alt="Fer Crozetta"
								/>
							</div>
							<div class="hidden sm:-my-px sm:ml-6 sm:flex sm:space-x-8">
								<!-- Current: "border-indigo-500 text-gray-900", Default: "border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700" -->
								<a
									href="/"
									class="inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium"
									class:border-indigo-500={selectedPage_value == 'home'}
									class:border-transparent={selectedPage_value != 'home'}
									class:text-gray-500={selectedPage_value != 'home'}
									class:text-gray-900={selectedPage_value == 'home'}
									class:hover:border-gray-300={selectedPage_value != 'home'}
									class:hover:text-gray-700={selectedPage_value != 'home'}
									aria-current="page">Dashboard</a
								>
								<a
									href="/spiders"
									class="inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium"
									class:border-indigo-500={selectedPage_value == 'spiders'}
									class:border-transparent={selectedPage_value != 'spiders'}
									class:text-gray-500={selectedPage_value != 'spiders'}
									class:text-gray-900={selectedPage_value == 'spiders'}
									class:hover:border-gray-300={selectedPage_value != 'spiders'}
									class:hover:text-gray-700={selectedPage_value != 'spiders'}
									aria-current="page"
									>Spiders
								</a>
								<a
									href="/kitchen"
									class="inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium"
									class:border-indigo-500={selectedPage_value == 'kitchen'}
									class:border-transparent={selectedPage_value != 'kitchen'}
									class:text-gray-500={selectedPage_value != 'kitchen'}
									class:text-gray-900={selectedPage_value == 'kitchen'}
									class:hover:border-gray-300={selectedPage_value != 'kitchen'}
									class:hover:text-gray-700={selectedPage_value != 'kitchen'}
									aria-current="page"
									>Kitchen
								</a>
								<a
									href="/scheduler"
									class="inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium"
									class:border-indigo-500={selectedPage_value == 'scheduler'}
									class:border-transparent={selectedPage_value != 'scheduler'}
									class:text-gray-500={selectedPage_value != 'scheduler'}
									class:text-gray-900={selectedPage_value == 'scheduler'}
									class:hover:border-gray-300={selectedPage_value != 'scheduler'}
									class:hover:text-gray-700={selectedPage_value != 'scheduler'}
									aria-current="page"
									>scheduler
								</a>
								<a
									href="/moirai"
									class="inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium"
									class:border-indigo-500={selectedPage_value == 'moirai'}
									class:border-transparent={selectedPage_value != 'moirai'}
									class:text-gray-500={selectedPage_value != 'moirai'}
									class:text-gray-900={selectedPage_value == 'moirai'}
									class:hover:border-gray-300={selectedPage_value != 'moirai'}
									class:hover:text-gray-700={selectedPage_value != 'moirai'}
									aria-current="page"
									>Moirai
								</a>
							</div>
						</div>
					</div>
				</div>
			</nav>

			<div class="py-10">
				<header>
					<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
						<h1 class="text-3xl font-bold leading-tight tracking-tight text-gray-900">
							{selectedPage_value}
						</h1>
					</div>
				</header>
				<main>
					<div class="px-4 py-8 lg:px-8 h-full w-full">
						<slot />
					</div>
				</main>
			</div>
		</div>
	</body>
</html>

<style>
</style>
