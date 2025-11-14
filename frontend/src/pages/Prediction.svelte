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

<div class="max-w-5xl mx-auto py-10 flex flex-col px-6">
  <h1 class="text-white text-4xl font-bold pb-3 text-center">Predict Your Movie's Box Office Revenue</h1>
  <p class="text-gray-2 pb-7 text-center">Enter movie details to predict its success</p>

  <div class="flex flex-col bg-dark-blue-3 border border-blue-gray-2 rounded-xl px-8 py-5 gap-8">
    <div class="flex gap-4"> 
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Budget</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 15000000" />
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Vote Average (1-10)</label>
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 7.5" />
      </div>
    </div>

    <div class="flex gap-4"> 
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Genre(s)</label> 
        <Select.Root type="multiple" bind:value={genres}>
          <Select.Trigger class="w-full">{genresSelection}</Select.Trigger>
          <Select.Content>
            {#each genreOptions as genreOption}
              <Select.Item value={genreOption}>{genreOption}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

       <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Language Selection</label>
          <Select.Root type="single" bind:value={languageSelection}>
            <Select.Trigger class="w-full">{languageOptions[languageSelection]}</Select.Trigger>
            <Select.Content>
              {#each Object.entries(languageOptions) as [languageValue, languageLabel]}
                <Select.Item value={languageValue}>{languageLabel}</Select.Item>
              {/each}
            </Select.Content>
          </Select.Root>
      </div>
    </div>

    <div class="flex gap-4"> 
     <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Release Month</label> 
        <Select.Root type="single" bind:value={monthSelection}>
          <Select.Trigger class="w-full">{monthOptions[monthSelection]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(monthOptions) as [monthValue, monthLabel]}
              <Select.Item value={monthValue}>{monthLabel}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Number of Languages</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 146" />
      </div>
    </div>

    <div class="flex gap-4">
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Runtime (mins)</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 50.5" />
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Number of Production Companies</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 5" />
      </div>
    </div>
    
    <div class="flex gap-4">
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Popularity</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 50.5" />
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Number of Production Countries</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 4" />
      </div>
    </div>

    <div class="flex gap-4">
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Vote Count</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 5000" />
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Vote Average (1-10)</label>
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2" placeholder="e.g. 7.5" />
      </div>
    </div>

    <Button variant="blue" onclick={predictNow} class="w-fit self-center">
      <TrendingUpNow/>
      Predict Now
    </Button>
  </div>
</div>
