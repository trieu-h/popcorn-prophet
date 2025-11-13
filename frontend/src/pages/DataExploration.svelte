<script lang="ts">
	import * as Select from "$lib/components/ui/select/index.js";
	import * as Card from "$lib/components/ui/card/index.js";

	//Parameters
	let parameters: string[] = $state([]);
	let parameterSelection = $derived(parameters.join(', '));
	let parameterOptions = ["Budget", "Release Month", "Runtime", "Popularity", "Vote Count", "Vote Average", "Number of Languages", 
											"Number of Production Companies", "Number of Production Countries"];

	// Genre
	let genres: string[] = $state([]);
	let genresSelection = $derived(genres.join(', '));
	let genreOptions = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", 
											"Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction",
											"Thriller", "TV Movie", "War", "Western"];
</script>

<div class="flex flex-col w-7xl mx-auto pt-10">
	<div class="flex justify-between mb-5">
		<div>
			<h1 class="text-white text-3xl font-bold pb-2">Data Exploration</h1>
			<p class="text-gray-2">Explore the relationship between movie parameters and box office revenue</p>
		</div>
	</div>

	<div class="bg-dark-blue-3 gap-3 border border-blue-gray-2 rounded-xl flex px-5 py-5">
  		<div class="w-105 flex-none">
			<p class="text-white mb-2">
				Select Parameter
			</p>
			<Select.Root type="single" bind:value={parameterSelection}>
					<Select.Trigger class="w-100">{parameterSelection}</Select.Trigger>
					<Select.Content>
						{#each parameterOptions as parameterOption}
							<Select.Item value={parameterOption}>{parameterOption}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
		</div>
  		<div class="w-105 flex-none">
			<p class="text-white mb-2">
				Filter by Genre
			</p>
			<Select.Root type="multiple" bind:value={genres}>
					<Select.Trigger class="w-100">{genresSelection}</Select.Trigger>
					<Select.Content>
						{#each genreOptions as genreOption}
							<Select.Item value={genreOption}>{genreOption}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
		</div>
  		<div class="w-3 flex-none">
				<input class="mt-10" type="checkbox" checked={false} />
		</div>
		<div class="w-50 mt-8.5 flex-none">
				<p class=" text-white mb-7">
					Show Line of Best Fit
				</p>
		</div>
	</div>

	<div class="bg-dark-blue-3 gap-3 border border-blue-gray-2 rounded-xl flex px-5 py-5 mt-5 h-200 mb-5">

	</div>

	<div class="flex justify-between gap-4 mb-5">
		<Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
			<Card.Header>
				<Card.Title class="text-light-gray">Movies</Card.Title>
			</Card.Header>
			<Card.Content>
				<p class="text-4xl font-extrabold text-white">15</p>
			</Card.Content>
		</Card.Root>	

		<Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
			<Card.Header>
				<Card.Title class="text-light-gray">Average Revenue</Card.Title>
			</Card.Header>
			<Card.Content>
				<p class="text-white text-4xl font-extrabold">$1425M</p>
			</Card.Content>
		</Card.Root>	

		<Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
			<Card.Header>
				<Card.Title class="text-light-gray">Average Budget</Card.Title>
			</Card.Header>
			<Card.Content>
				<p class="text-white text-4xl font-extrabold">$167M</p>
			</Card.Content>
		</Card.Root>
		<Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
			<Card.Header>
				<Card.Title class="text-light-gray">Highest Revenue</Card.Title>
			</Card.Header>
			<Card.Content>
				<p class="text-white text-4xl font-extrabold">$2923M</p>
			</Card.Content>
		</Card.Root>
	</div>

</div>

<style>
</style>
