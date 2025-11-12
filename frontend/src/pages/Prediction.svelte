<script lang="ts">
	import * as Select from "$lib/components/ui/select/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
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
	<Card.Root class="bg-dark-blue-3 gap-3 border-blue-gray-2 flex flex-col">
		<div class="flex pl-5 pt-3">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Budget</Card.Title>
			</Card.Content>
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Vote Average (1-10)</Card.Title>
			</Card.Content>
		</div>
		<div class="flex pl-5 mb-2">
			<Card.Content class= "flex-1 ">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 15000000" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 7.5" />
			</Card.Content>
			</div>
			<div class="flex pl-5">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Genre(s)</Card.Title>
			</Card.Content>
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Original Language</Card.Title>
			</Card.Content>
			</div>
			<div class="flex pl-5 mb-2">
			<Card.Content class= "flex-1">
				<Select.Root type="multiple" bind:value={genres}>
					<Select.Trigger class="w-100">{genresSelection}</Select.Trigger>
					<Select.Content>
						{#each genreOptions as genreOption}
							<Select.Item value={genreOption}>{genreOption}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
			</Card.Content>
			<Card.Content class= "flex-1">
				<Select.Root type="single" bind:value={languageSelection}>
					<Select.Trigger class="w-100">{languageOptions[languageSelection]}</Select.Trigger>
					<Select.Content>
						{#each Object.entries(languageOptions) as [languageValue, languageLabel]}
							<Select.Item value={languageValue}>{languageLabel}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
			</Card.Content>
			</div>
			<div class="flex pl-5">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Release Month</Card.Title>
			</Card.Content>
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Number of Languages</Card.Title>
			</Card.Content>
			</div>
			<div class="flex pl-5 mb-2">
			<Card.Content class= "flex-1">
				<Select.Root type="single" bind:value={monthSelection}>
					<Select.Trigger class="w-100">{monthOptions[monthSelection]}</Select.Trigger>
					<Select.Content>
						{#each Object.entries(monthOptions) as [monthValue, monthLabel]}
							<Select.Item value={monthValue}>{monthLabel}</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 3" />
			</Card.Content>
			</div>
			<div class="flex pl-5">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Runtime (in Minutes)</Card.Title>
			</Card.Content>
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Number of Production Companies</Card.Title>
			</Card.Content>
			</div>
			<div class="flex pl-5 mb-2">
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 146" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 5" />
			</Card.Content>
			</div>
			<div class="flex pl-5">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Popularity</Card.Title>
			</Card.Content>
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Number of Production Countries</Card.Title>
			</Card.Content>
			</div>
			<div class="flex pl-5 mb-2">
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 50.5" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 4" />
			</Card.Content>
			</div>
			<div class="flex pl-5">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Vote Count</Card.Title>
			</Card.Content>
			</div>
			<div class="flex pl-5 mb-2 pb-3">
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2" placeholder="e.g. 5000" />
			</Card.Content>
			</div>
			<div class="mx-auto items-center">
				<Card.Content class= "flex-1">
					<Button variant="blue" onclick={predictNow}>
						<TrendingUpNow/>
						Predict Now
					</Button>
				</Card.Content>
			</div>
	</Card.Root>
</div>


<style>
</style>
