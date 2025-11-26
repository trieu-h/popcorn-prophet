<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
  import TrendingUpNow from "@lucide/svelte/icons/trending-up-down";
  import { Button } from "$lib/components/ui/button/index.js";
  import { navigate } from "../router";
  import { form } from "./states.svelte";

  let genre_options = [
    "Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", 
    "Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction",
    "Thriller", "TV Movie", "War", "Western"
  ];

  let month_options: Record<string, string> = { 
      "1": "January", 
      "2": "February", 
      "3": "March", 
      "4": "April", 
      "5": "May", 
      "6": "June", 
      "7": "July",
      "8": "August", 
      "9": "September", 
      "10": "October", 
      "11": "November", 
      "12": "December" 
  };

  let original_language_options: Record<string, string> = { 
    "en": "English",
    "fr": "French",
    "ru": "Russian",
    "es": "Spanish", 
    "ja": "Japanese", 
    "hi": "Hindi",
    "others": "Others" 
  };

  let vote_count = $state();
  let vote_average = $state();
  let budget = $state();
  let number_of_production_countries = $state();
  let popularity = $state();
  let number_of_production_companies = $state();
  let runtime = $state();
  let number_of_spoken_languages = $state();
  let release_month: string = $state("");
  let genres: string[] = $state([]);
  let original_language: string = $state("");
  let genresSelection = $derived(genres.join(', '));

  async function predict(e: SubmitEvent) {
    e.preventDefault();

    form.vote_count = Number(vote_count); 
    form.vote_average = Number(vote_average); 
    form.budget = Number(budget); 
    form.number_of_production_countries = Number(number_of_production_countries);
    form.number_of_production_companies = Number(number_of_production_companies); 
    form.number_of_spoken_languages = Number(number_of_spoken_languages); 
    form.popularity = Number(popularity); 
    form.runtime = Number(runtime); 
    form.release_month = Number(release_month); 
    form.original_language = original_language;
    form.genres = "";

    navigate('/prediction/result', { viewTransition: true });
  }
</script>

<div class="max-w-5xl mx-auto py-10 flex flex-col px-6" id="prediction-wrapper">
  <h1 class="text-white text-4xl font-bold pb-3 text-center">Predict Your Movie's Box Office Revenue</h1>
  <p class="text-gray-2 pb-7 text-center">Enter movie details to predict its success</p>

  <form class="flex flex-col bg-dark-blue-3 border border-blue-gray-2 rounded-xl px-8 py-5 gap-8">
    <div class="flex gap-4"> 
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Budget</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 15000000" bind:value={budget}/>
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Vote Average (1-10)</label>
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 7.5" bind:value={vote_average}/>
      </div>
    </div>

    <div class="flex gap-4"> 
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Genre(s)</label> 
        <Select.Root type="multiple" bind:value={genres}>
          <Select.Trigger class="w-full">{genresSelection}</Select.Trigger>
          <Select.Content>
            {#each genre_options as genre_option}
              <Select.Item value={genre_option}>{genre_option}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

       <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Original Language</label>
          <Select.Root type="single" bind:value={original_language}>
            <Select.Trigger class="w-full">{original_language_options[original_language]}</Select.Trigger>
            <Select.Content>
              {#each Object.entries(original_language_options) as [language_value, language_label]}
                <Select.Item value={language_value}>{language_label}</Select.Item>
              {/each}
            </Select.Content>
          </Select.Root>
      </div>
    </div>

    <div class="flex gap-4"> 
     <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Release Month</label> 
        <Select.Root type="single" bind:value={release_month}>
          <Select.Trigger class="w-full">{month_options[release_month]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(month_options) as [month_value, month_label]}
              <Select.Item value={month_value}>{month_label}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Number of Languages</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 2" bind:value={number_of_spoken_languages}/>
      </div>
    </div>

    <div class="flex gap-4">
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Runtime (mins)</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 50.5" bind:value={runtime}/>
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Number of Production Companies</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 5" bind:value={number_of_production_companies}/>
      </div>
    </div>
    
    <div class="flex gap-4">
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Popularity</label> 
          <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 50.5" bind:value={popularity}/>
      </div>

      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Number of Production Countries</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 4" bind:value={number_of_production_countries}/>
      </div>
    </div>

    <div class="flex gap-4">
      <div class="flex-1 flex flex-col gap-2">
        <label class="text-white">Vote Count</label> 
        <input class="bg-dark-blue-4 text-white h-9 px-3 py-2 rounded-md border border-blue-gray-2 w-full" placeholder="e.g. 5000" bind:value={vote_count} />
      </div>
      <div class="flex-1 flex flex-col gap-2"></div>
    </div>

    <Button variant="blue" onclick={predict} class="w-fit self-center" type="submit">
      <TrendingUpNow/>
      Predict Now
    </Button>
  </form>
</div>

<style>
  @keyframes slide-out-to-left {
    from {
      right: 0%;
      opacity: 1;
    }
    to {
      right: 100%;
      opacity: 0;
    }
  }
  @keyframes slide-out-to-right {
    from {
      left: 0%;
      opacity: 1;
    }
    to {
      left: 100%;
      opacity: 0;
    }
  }
  #prediction-wrapper {
    view-transition-name: prediction-wrapper;
  }
  ::view-transition-group(prediction-wrapper) {
    animation-duration: 300ms;
  }
  ::view-transition-old(prediction-wrapper) {
    animation-name: slide-out-to-left;
  }
  ::view-transition-old(prediction-wrapper-back) {
    animation-name: slide-out-to-right;
  }
</style>
