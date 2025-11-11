<script lang="ts">
  import * as Command from "$lib/components/ui/command/index.js";
	import { navigate } from "../router";
	const movies: string[] = ['movie 1', 'movie 2'];
	let empty = false;

	function onMovieSelection() {
		navigate('/analytics/result');
	}
</script>

<div class="w-3xl mx-auto pt-30 flex flex-col items-center">
	<h1 class="text-white text-5xl font-bold pb-5">Find an Existing Movie</h1>
	<p class="text-gray-2 pb-7">Search our database to view the prediction explainability dashboard for any movie</p>

	<Command.Root>
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

<style>
</style>
