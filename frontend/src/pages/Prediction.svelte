<script lang="ts">
	import * as Card from "$lib/components/ui/card/index.js";
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
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 15000000" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 7.5" />
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
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="Action" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="English" />
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
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="November" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 3" />
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
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 146" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 5" />
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
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 50.5" />
			</Card.Content>
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 4" />
			</Card.Content>
			</div>
			<div class="flex pl-5">
			<Card.Content class= "flex-1">
				<Card.Title class="text-white">Vote Count</Card.Title>
			</Card.Content>
			</div>
			<div class="flex pl-5 mb-2 pb-3">
			<Card.Content class= "flex-1">
				<input class="bg-dark-blue-4 text-white px-3 py-2 w-100" placeholder="e.g. 5000" />
			</Card.Content>
			</div>
			<div class="mx-auto items-center">
				<Card.Content class= "flex-1">
					<button class="bg-light-blue-2 text-white px-3 py-2 w-45">
						&#10004; Predict Now
					</button>
				</Card.Content>
			</div>
	</Card.Root>
</div>


<style>
</style>
