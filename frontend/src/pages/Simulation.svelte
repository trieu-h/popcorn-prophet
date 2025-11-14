<script lang="ts">
  import ArrowUp from "@lucide/svelte/icons/arrow-up";
	import RotateCCW from "@lucide/svelte/icons/rotate-ccw";
	import Button from "$lib/components/ui/button/button.svelte";
	import * as Select from "$lib/components/ui/select/index.js";

	let genres: string[] = $state([]);
	let genresSelection = $derived(genres.join(', '));
	let genreOptions = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", 
											"Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction",
											"Thriller", "TV Movie", "War", "Western"];

	let monthSelection: string = $state("");
	let monthOptions: Record<string, string> = { "1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", 
																								"7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December" };

	let languageSelection: string = $state("");
	let languageOptions: Record<string, string> = { "en": "English", "fr": "French", "ru": "Russian", "es": "Spanish", "ja": "Japanese", "hi": "Hindi", "others": "Others" };
</script>

<div class="flex flex-col w-7xl mx-auto pt-10 px-6">
  <div class="flex justify-between mb-7">
	  <div>
		  <h1 class="text-white text-3xl font-bold pb-2">Box Office Scenario Simulator</h1>
		  <p class="text-gray-2">Adjust a variable on the left to see its impact on the prediction</p>
	  </div>
  </div>

  <div class="flex justify-between gap-4 mb-5">
    <div class="bg-dark-blue-3 border border-blue-gray-2 rounded-xl flex flex-col flex-7/20 p-5">
      <div class="flex justify-between items-center mb-5">
        <h1 class="text-2xl text-white font-bold">Adjust Variables</h1>
        <Button class="text-gray-2" variant="ghost">
          <RotateCCW/>
          Reset All
        </Button>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Budget ($)</label>
        <input class="bg-dark-blue-4 text-white px-3 py-2 w-100 rounded-md border border-blue-gray-2"/>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Genre(s)</label>
        <Select.Root type="multiple" bind:value={genres}>
          <Select.Trigger class="w-100">{genresSelection}</Select.Trigger>
          <Select.Content>
            {#each genreOptions as genreOption}
              <Select.Item value={genreOption}>{genreOption}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Release Month</label>
        <Select.Root type="single" bind:value={monthSelection}>
          <Select.Trigger class="w-100">{monthOptions[monthSelection]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(monthOptions) as [monthValue, monthLabel]}
              <Select.Item value={monthValue}>{monthLabel}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Runtime (minutes)</label>
        <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Popularity</label>
        <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
      </div>

      <div class="flex gap-4 mb-6">
        <div class="flex-1">
          <label class="text-white">Vote Count</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
        </div>
        <div class="flex-1">
          <label class="text-white">Vote Average</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
        </div>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Original Language</label>
        <Select.Root type="single" bind:value={languageSelection}>
          <Select.Trigger class="w-100">{languageOptions[languageSelection]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(languageOptions) as [languageValue, languageLabel]}
              <Select.Item value={languageValue}>{languageLabel}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex gap-4">
        <div class="flex-1 flex flex-col gap-2">
          <label class="text-white"># Languages</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
        </div>
        <div class="flex-1 flex flex-col gap-2">
          <label class="text-white"># Prod. Comp.</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
        </div>
        <div class="flex-1 flex flex-col gap-2">
          <label class="text-white"># Prod. Count.</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" />
        </div>
      </div>
    </div>

    <div class="flex-13/20 px-5 py-3">
      <p class="text-white font-bold pl-2 mb-5">Predicted Outcome</p>
      <div class="bg-dark-blue-3 border border-blue-gray-2 rounded-xl p-7 mb-7">
        <p class="text-gray-2 mb-3">Predicted Worldwide Box Office</p>
        <div class="flex gap-2">
          <p class="text-white font-extrabold text-4xl">$854.4M</p>
          <div class="flex gap-1 text-light-green font-extrabold self-end pb-1">
            <ArrowUp/>
            <span>+42.1M</span>
          </div>	
        </div>
      </div>
      <div class="bg-dark-blue-3 border border-blue-gray-2 rounded-xl flex flex-col flex-7/20 p-7">
        <p class="text-white font-bold mb-3">Original vs. Simulated Revenue</p>
        <div class="flex text-white h-100">
          <div class="flex flex-col flex-1 bg-blue items-center h-full">
            <div class="flex-1 flex flex-col">
              <div class="w-20 bg-blue-gray-2 h-3/4 mt-auto rounded-t-lg">
              </div>
            </div>
            <span class="text-light-gray mb-2">Original</span>
            <span>$811M</span>
          </div>
          <div class="flex flex-col flex-1 items-center h-full">
            <div class="flex-1">
              <div class="w-20 bg-light-blue h-full rounded-t-lg">
              </div>
            </div>
            <span class="mb-2">Simulated</span>
            <span>$911M</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
