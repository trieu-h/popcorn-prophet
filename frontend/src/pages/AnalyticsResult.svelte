<script lang="ts">
  import { onDestroy, onMount } from "svelte";
  import { route, navigate } from "../router";
  import ArrowLeft from "@lucide/svelte/icons/arrow-left";
  import * as Card from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { Movie } from "src/types/types";
  import { POSTER_PREFIX } from "../const/const";

  let movie = $state<Movie>();
  let backdrop_dom_node: HTMLDivElement | null = null;

  function back_to_search_page() {
    navigate("/analytics", { state: 'navigateFromResult', viewTransition: true });
  }

  onMount(async () => {
    const res = await fetch(`http://localhost:8000/movies/${route.params.movie_id}`)
    movie = await res.json();

    const main = document.body.querySelector('div#app main');
    backdrop_dom_node = document.createElement('div');
    backdrop_dom_node.style = `position: absolute; width: 100%; height: 300px; z-index: -1`;
    const imgElem: HTMLImageElement = document.createElement('img');
    imgElem.src = `${POSTER_PREFIX}${movie?.backdrop_path}`;
    imgElem.style = `height: 100%; width: 100%; object-fit: cover; opacity: 0; transition: opacity .75s cubic-bezier(.165,.84,.44,1)`;
    if (imgElem.complete) {
      imgElem.style.opacity = "0.2";
    } else {
      imgElem.addEventListener('load', () => {
        imgElem.style.opacity = "0.2";
      });
    }
    backdrop_dom_node.insertAdjacentElement('afterbegin', imgElem);
    main?.insertAdjacentElement('afterbegin', backdrop_dom_node);
  })

  onDestroy(() => {
    backdrop_dom_node?.remove();
  })

  const number_formatter = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });

  const extract_release_year = (date: string) => date?.split("-")[0];

  const reformat_date = (date: string | null) => {
    if (!date) return '';
    const [y, m, d] = date.split("-");
    return `${m}/${d}/${y}`;
  }

  const reformat_time = (time: number | null) => {
    if (!time) return '';
    const h = Math.floor(time / 60);
    const m = time % 60;
    let str = '';
    if (h > 0) str += `${h}h `;
    if (m > 0) str += `${m}m`;
    return str;
  }
</script>

<div class="flex flex-col max-w-7xl mx-auto pt-10 px-6">
  <div class="flex justify-between mb-3">
    <Button variant="ghost" onclick={back_to_search_page} class="text-white">
      <ArrowLeft/>
      Back to Search page
    </Button>
  </div>

  <h1 class="text-white text-center text-3xl font-bold pb-2 mb-3">Prediction Analysis</h1>

  <div class="flex mb-6 gap-3 bg-blue-gray border border-blue-gray-2 p-6 rounded-xl">
    <div class="h-60 w-40">
      <img src={POSTER_PREFIX + movie?.poster_path} class="object-contain" id="poster" alt="movie poster">
    </div>
    <div class="flex-7 text-white flex flex-col gap-3">
        <h1 class="text-2xl font-bold">{movie?.original_title} <span class="text-gray-2">({extract_release_year(movie?.release_date as string)})</span></h1>
        <div class="flex text-sm">
          <span>{reformat_date(movie?.release_date as string)} ({movie?.original_language.toUpperCase()})</span>
          <span class="pl-6 relative before:content-['•'] before:absolute before:left-2">{movie?.genres}</span>
          <span class="pl-6 relative before:content-['•'] before:absolute before:left-2">{reformat_time(movie?.runtime as number)}</span>
        </div>
        <h3 class="text-xl font-bold">Overview</h3>
        <p>{movie?.overview}</p>
    </div>
  </div>

  <div class="flex flex-col md:flex-row justify-between gap-4 mb-12">
    <Card.Root class="flex-1 bg-blue-gray gap-4 border-blue-gray-2 min-w-0">
      <Card.Header>
        <Card.Title class="text-white">Actual Box Office Revenue</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-white text-4xl font-extrabold">{number_formatter.format(movie?.revenue as number)}</p>
      </Card.Content>
      <Card.Footer>
        <p class="text-gray-2 text-sm">Actual revenue at the time of the release</p>
      </Card.Footer>
    </Card.Root>  

    <Card.Root class="flex-1 bg-dark-blue-2 border border-light-blue gap-4 min-w-0">
      <Card.Header>
        <Card.Title class="text-white">Predicted Box Office Revenue</Card.Title>
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

<style>
  #poster {
    view-transition-name: poster;
  }
</style>

