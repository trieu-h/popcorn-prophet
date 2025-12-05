<script lang="ts">
  import ArrowUp from "@lucide/svelte/icons/arrow-up";
  import ArrowDown from "@lucide/svelte/icons/arrow-down";
	import * as Select from "$lib/components/ui/select/index.js";
	import Button from "$lib/components/ui/button/button.svelte";
	import RotateCCW from "@lucide/svelte/icons/rotate-ccw";
  import { navigate, route } from "../router";
  import { onMount } from "svelte";
  import { form } from "./states.svelte";
  import { API_URL } from "../const/const";
  import { currency_formatter } from "./reuse";

  let genre_options: Record<string, string> = {
    'A': 'Action',
    'B': 'Adventure',
    'C': 'Animation',
    'D': 'Comedy',
    'E': 'Crime',
    'F': 'Documentary',
    'G': 'Drama',
    'H': 'Family',
    'I': 'Fantasy',
    'J': 'History',
    'K': 'Horror',
    'L': 'Music',
    'M': 'Mystery',
    'N': 'Romance',
    'O': 'Science Fiction',
    'P': 'TV Movie',
    'Q': 'Thriller',
    'R': 'War',
    'S': 'Western',
  }

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
  let original_language: string = $state("");
  let genres: string[] = $state([]);
  let genresSelection = $derived(genres.map(g => genre_options[g]).join(', '));
  let predicted_revenue: number = $state()!;
  let initial_predicted_value: number;
  let updated_predicted_revenue: number | undefined = $state();
  let revenue_diff: number | null = $state(null);

  $effect(() => {
    if (!revenue_diff || !updated_predicted_revenue) {
      return;
    }
    let original_ratio;
    let simulated_ratio;
    if (revenue_diff < 0) {
      original_ratio = 1; 
      simulated_ratio = updated_predicted_revenue / initial_predicted_value;
    } else {
      simulated_ratio = 1;
      original_ratio = initial_predicted_value / updated_predicted_revenue;
    }
    const original = document.getElementById("original_height") as HTMLElement;
    original.style.height = `${Math.round(original_ratio * 100)}%`;
    const simulated = document.getElementById("simulated_height") as HTMLElement;
    simulated.style.height = `${Math.round(simulated_ratio * 100)}%`;
  });

  onMount(async () => {
    if (!Object.keys(form).length) {
      navigate('/prediction');
      return;
    }

    vote_count = form.vote_count;
    vote_average = form.vote_average;
    budget = form.budget;
    popularity = form.popularity;
    runtime = form.runtime;
    release_month = form.release_month.toString();
    original_language = form.original_language;
    genres = form.genres;
    number_of_production_countries = form.number_of_production_countries;
    number_of_production_companies = form.number_of_production_companies;
    number_of_spoken_languages = form.number_of_spoken_languages;
    predicted_revenue = (route.state as any).predicted_revenue as number;
    initial_predicted_value = predicted_revenue;
  });

  async function updatePrediction() {
    const body = {
      vote_count,
      vote_average,
      budget: Number(budget),
      popularity,
      runtime,
      release_month,
      original_language,
      genres: genres.join(""),
      number_of_production_countries,
      number_of_production_companies,
      number_of_spoken_languages,
      predicted_revenue,
    }

    const res = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    const new_prediction = await res.json();
    updated_predicted_revenue = new_prediction.predicted_revenue;
    predicted_revenue = updated_predicted_revenue!;
    revenue_diff = updated_predicted_revenue! - initial_predicted_value;
  }
</script>

<div class="flex flex-col mx-auto pt-10 px-6 max-w-7xl" id="prediction-wrapper">
  <div class="flex justify-between mb-7">
	  <div>
		  <h1 class="text-white text-3xl font-bold pb-2">Box Office Scenario Simulator</h1>
		  <p class="text-gray-2">Adjust a variable on the left to see its impact on the prediction</p>
	  </div>
  </div>

  <div class="flex flex-col md:flex-row justify-between gap-6 mb-5">
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
        <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={budget} onblur={updatePrediction}/>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Genre(s)</label>
        <Select.Root type="multiple" bind:value={genres} onValueChange={updatePrediction}>
          <Select.Trigger class="w-full">{genresSelection}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(genre_options) as [genre_value, genre_label]}
              <Select.Item value={genre_value}>{genre_label}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Release Month</label>
        <Select.Root type="single" bind:value={release_month} onValueChange={updatePrediction}>
          <Select.Trigger class="w-full">{month_options[release_month]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(month_options) as [month_value, month_label]}
              <Select.Item value={month_value}>{month_label}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Runtime (minutes)</label>
        <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={runtime} onblur={updatePrediction}/>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Popularity</label>
        <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={popularity} onblur={updatePrediction}/>
      </div>

      <div class="flex gap-4 mb-6">
        <div class="flex-1">
          <label class="text-white">Vote Count</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={vote_count} onblur={updatePrediction}/>
        </div>
        <div class="flex-1">
          <label class="text-white">Vote Average</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={vote_average} onblur={updatePrediction}/>
        </div>
      </div>

      <div class="flex flex-col gap-2 mb-6">
        <label class="text-white">Original Language</label>
        <Select.Root type="single" bind:value={original_language} onValueChange={updatePrediction}>
          <Select.Trigger class="w-full">{original_language_options[original_language]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(original_language_options) as [language_value, language_label]}
              <Select.Item value={language_value}>{language_label}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
      </div>

      <div class="flex gap-4">
        <div class="flex-1 flex flex-col gap-2">
          <label class="text-white"># Languages</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={number_of_spoken_languages} onblur={updatePrediction}/>
        </div>
        <div class="flex-1 flex flex-col gap-2">
          <label class="text-white"># Prod. Comp.</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={number_of_production_companies} onblur={updatePrediction}/>
        </div>
        <div class="flex-1 flex flex-col gap-2">
          <label class="text-white"># Prod. Count.</label>
          <input class="bg-dark-blue-4 text-white px-3 py-2 w-full rounded-md border border-blue-gray-2" bind:value={number_of_production_countries} onblur={updatePrediction}/>
        </div>
      </div>
    </div>

    <div class="flex-13/20 flex flex-col">
      <div class="bg-dark-blue-3 border border-blue-gray-2 rounded-xl p-7 mb-7">
        <p class="text-gray-2 mb-3">Predicted Worldwide Box Office</p>
        <div class="flex gap-2">
          <p class="text-white font-extrabold text-4xl">{currency_formatter.format(predicted_revenue)}</p>
          {#if revenue_diff}
            <div class="flex gap-1 {revenue_diff > 0 ? "text-light-green" : "text-light-red"} font-extrabold self-end pb-1" >
                {#if revenue_diff > 0}
                  <ArrowUp/>
                {:else}
                  <ArrowDown/>
                {/if}
                <span>{currency_formatter.format(revenue_diff)}</span>
            </div>
          {/if}
        </div>
      </div>
      <div class="bg-dark-blue-3 border border-blue-gray-2 rounded-xl flex flex-col flex-1 p-7">
        <p class="text-white font-bold mb-3">Original vs. Simulated Revenue</p>
        {#if !updated_predicted_revenue}
          <p class="text-white">Please update any parameters in the left panel to observe the changes</p>
        {:else}
          <div class="flex text-white h-full">
            <div class="flex flex-col flex-1 bg-blue items-center h-full">
              <div class="flex-1 flex flex-col">
                <div class="w-20 bg-blue-gray-2 mt-auto rounded-t-lg" id="original_height">
                </div>
              </div>
              <span class="text-light-gray mb-2">Original</span>
              <span>{currency_formatter.format(initial_predicted_value)}</span>
            </div>
            <div class="flex flex-col flex-1 items-center h-full">
              <div class="flex-1">
                <div class="w-20 bg-light-blue rounded-t-lg" id="simulated_height">
                </div>
              </div>
              <span class="mb-2">Simulated</span>
              <span>{currency_formatter.format(updated_predicted_revenue)}</span>
            </div>
          </div>
        {/if}
      </div>
    </div>
  </div>
</div>
