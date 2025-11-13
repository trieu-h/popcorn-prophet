<script lang="ts">
	import * as Select from "$lib/components/ui/select/index.js";
	import TrendingUpNow from "@lucide/svelte/icons/trending-up-down";
  import { Button } from "$lib/components/ui/button/index.js";
  import { navigate } from "../router";

	// Genre
	let genres: string[] = $state([]);
	let genresSelection = $derived(genres.join(', '));
	let genreOptions = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", 
											"Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction",
											"Thriller", "TV Movie", "War", "Western"];

	// Release month
	let monthSelection: string = $state("");
	let monthOptions: Record<string, string> = { "1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", 
																								"7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December" };

	// Original language
	let languageSelection: string = $state("");
	let languageOptions: Record<string, string> = { "en": "English", "fr": "French", "ru": "Russian", "es": "Spanish", "ja": "Japanese", "hi": "Hindi", "others": "Others" };

	function predictNow() {
		navigate('/prediction/result');
	}
</script>

<div class="w-5xl mx-auto pt-10 flex flex-col items-center">
	<h1 class="text-white text-4xl font-bold pb-3">Predict Your Movie's Box Office Revenue</h1>
	<p class="text-gray-2 pb-7">Enter movie details to predict its success</p>
</div>

<div class="w-5xl mx-auto">
	<div class="bg-dark-blue-3 gap-3 border border-blue-gray-2 rounded-xl flex flex-col pt-3 mb-5">
		<div class="flex pl-5 pt-3">
			<div class= "flex-1">
				<p class="text-white">Budget</p>
			</div>
			<div class= "flex-1">
				<p class="text-white">Vote Average (1-10)</p>
			</div>
		</div>
		<div class="flex pl-5 mb-2">
			<div class= "flex-1 ">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 15000000" />
			</div>
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 7.5" />
			</div>
			</div>
			<div class="flex pl-5">
			<div class= "flex-1">
				<p class="text-white">Genre(s)</p>
			</div>
			<div class= "flex-1">
				<p class="text-white">Original Language</p>
			</div>
			</div>
			<div class="flex pl-5 mb-2">
			<div class= "flex-1">
				<Select.Root type="multiple" bind:value={genres}>
					<Select.Trigger class="w-100">{genresSelection}</Select.Trigger>
					<Select.Content>
						{#each genreOptions as genreOption}
							<Select.Item value={genreOption}>{genreOption}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
			</div>
			<div class= "flex-1">
				<Select.Root type="single" bind:value={languageSelection}>
					<Select.Trigger class="w-100">{languageOptions[languageSelection]}</Select.Trigger>
					<Select.Content>
						{#each Object.entries(languageOptions) as [languageValue, languageLabel]}
							<Select.Item value={languageValue}>{languageLabel}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
			</div>
			</div>
			<div class="flex pl-5">
			<div class= "flex-1">
				<p class="text-white">Release Month</p>
			</div>
			<div class= "flex-1">
				<p class="text-white">Number of Languages</p>
			</div>
			</div>
			<div class="flex pl-5 mb-2">
			<div class= "flex-1">
				<Select.Root type="single" bind:value={monthSelection}>
					<Select.Trigger class="w-100">{monthOptions[monthSelection]}</Select.Trigger>
					<Select.Content>
						{#each Object.entries(monthOptions) as [monthValue, monthLabel]}
							<Select.Item value={monthValue}>{monthLabel}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
			</div>
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 3" />
			</div>
			</div>
			<div class="flex pl-5">
			<div class= "flex-1">
				<p class="text-white">Runtime (in Minutes)</p>
			</div>
			<div class= "flex-1">
				<p class="text-white">Number of Production Companies</p>
			</div>
			</div>
			<div class="flex pl-5 mb-2">
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 146" />
			</div>
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 5" />
			</div>
			</div>
			<div class="flex pl-5">
			<div class= "flex-1">
				<p class="text-white">Popularity</p>
			</div>
			<div class= "flex-1">
				<p class="text-white">Number of Production Countries</p>
			</div>
			</div>
			<div class="flex pl-5 mb-2">
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 50.5" />
			</div>
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 4" />
			</div>
			</div>
			<div class="flex pl-5">
			<div class= "flex-1">
				<p class="text-white">Vote Count</p>
			</div>
			</div>
			<div class="flex pl-5 mb-2 pb-3">
			<div class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 5000" />
			</div>
			</div>
			<div class="mx-auto items-center">
				<div class= "flex-1 mb-5">
					<Button variant="blue" onclick={predictNow}>
						<TrendingUpNow/>
						Predict Now
					</Button>
				</div>
			</div>
		</div>
</div>


<style>
</style>
