<script lang="ts">
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
	const movies: string[] = [];
	let empty = false;
	function onMovieSelection() {
		console.error("Not implemented yet lol");
	}
</script>

<div class="flex flex-col w-7xl mx-auto pt-10">
	<div class="flex justify-between mb-3">
		<div>
			<h1 class="text-white text-3xl font-bold pb-2">Prediction Analysis</h1>
			<p class="text-gray-2 pb-7">Search for a movie to see its prediction explainability</p>
		</div>
'
		<Command.Root class="w-100">
			<Command.Input placeholder="Search for a movie title" keydown/>
			<Command.List>
				{#if empty}
					<Command.Empty>No results found.</Command.Empty>
				{/if}

				{#if movies.length}
					<Command.Group heading="Movie title">
						{#each movies as movie}
							<Command.Item onclick={onMovieSelection}>{movie}</Command.Item>
						{/each}
					</Command.Group>
				{/if}
			</Command.List>
		</Command.Root>
	</div>

	<div class="flex justify-between gap-4 mb-12">
		<Card.Root class="flex-1 bg-blue-gray gap-4 border-blue-gray-2">
			<Card.Header>
				<Card.Title class="text-white">Base Prediction</Card.Title>
			</Card.Header>
			<Card.Content>
				<p class="text-white text-4xl font-extrabold">$150M</p>
			</Card.Content>
			<Card.Footer>
				<p class="text-gray-2 text-sm">Industry average starting point</p>
			</Card.Footer>
		</Card.Root>	

		<Card.Root class="flex-1 bg-dark-blue-2 border border-light-blue gap-4">
			<Card.Header>
				<Card.Title class="text-white">Predictied Box Office Revenue</Card.Title>
			</Card.Header>
			<Card.Content>
				<p class="text-white text-4xl font-extrabold">$825M</p>
			</Card.Content>
			<Card.Footer>
				<p class="text-gray-2 text-sm">Final calculated prediction</p>
			</Card.Footer>
		</Card.Root>	
	</div>
	
	<div>
		<h1 class="text-white text-xl font-bold mb-5">Key Prediction Factors</h1>
	
		<table class="text-white w-full">
			<thead class="text-left">
				<tr class="border border-blue-gray-2 bg-dark-gray-2">
					<th class="px-4 py-3 w-4/10">Feature</th>
					<th class="px-4 py-3">Impact on Revenue</th>
					<th class="px-4 py-3">Adjusted Total</th>
				</tr>
			</thead>
			<tbody>
				<tr class="border border-blue-gray-2 bg-dark-gray-3 font-light">
					<td class="px-4 py-7 w-3/10">High Budget</td>
					<td class="px-4 py-7">
						<div class="bg-dark-green text-light-green rounded-3xl w-fit px-5 py-3 font-bold">
							<span class="mr-2">&#8593;</span> +$120M	
						</div>
					</td>
					<td class="px-4 py-7">$270M</td>
				</tr>
				<tr class="border border-blue-gray-2 bg-dark-gray-3 font-light">
					<td class="px-4 py-7 w-3/10">Genre: Sci fi</td>
					<td class="px-4 py-7">
						<div class="bg-dark-red text-light-red rounded-3xl w-fit px-5 py-3 font-bold">
							<span class="mr-2">&#8595;</span> -$20M	
						</div>
					</td>
					<td class="px-4 py-7">$20M</td>
				</tr>
			</tbody>
		</table>
	</div>
</div>


