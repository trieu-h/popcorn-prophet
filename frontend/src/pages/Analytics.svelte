<script lang="ts">
  import type { Movie } from "src/types/types";
  import { Command, CommandInput } from "$lib/components/ui/command";
  import { Card, CardContent, CardHeader, CardTitle } from "$lib/components/ui/card"
  import { Skeleton } from "$lib/components/ui/skeleton/index.js";
  import { navigate } from "../router";

  const poster_prefix = "https://image.tmdb.org/t/p/original/";
  let movies: Movie[] = $state([]);
  let search_string = $state("");
  let is_loading = $state(false);
  let last_movie_id_state: number | null = null;

  let timeout: number | null = null;
  const cooldown = 1000;

  function on_movie_selection() {
    navigate('/analytics/result');
  }

  async function on_input_change() {
    if (search_string.trim() === '') {
      is_loading = false;
      movies = [];
      last_movie_id_state = null;
      return;
    }

    is_loading = true;
    if (timeout) clearTimeout(timeout);
      
    timeout = setTimeout(async () => {
      await get_movies(search_string);
      is_loading = false;
    }, cooldown);
  }

  async function get_movies(title: string, last_movie_id?: number) {
    let url = `http://localhost:8000/movies?title=${title.trim()}`;
    if (last_movie_id) {
      url = url + `&last_id=${last_movie_id}`
    }
    const res = await fetch(url);
    const movies_json = await res.json();
    movies = last_movie_id ? [...movies, ...movies_json] : movies_json;
    last_movie_id_state = movies.length ? movies[movies.length - 1].id : null;
  }

  window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight) {
      get_movies(search_string.trim(), last_movie_id_state!);
    }
  })
</script>

<div class="max-w-4xl mx-auto pt-10 flex flex-col px-6">
  <h1 class="text-white text-4xl font-bold pb-3 text-center">Find an Existing Movie</h1>
  <p class="text-gray-2 pb-7 text-center">Search our database to view the prediction explainability dashboard for any movie</p>

  <Command class="mb-7">
    <CommandInput placeholder="Search for a movie title" oninput={on_input_change} bind:value={search_string}/>
  </Command>

  {#if is_loading}
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
      {#each { length: 4 }}
        <Card class="gap-3 opacity-50">
          <CardHeader>
            <CardTitle>
              <Skeleton class="h-10 w-full bg-black"/>
            </CardTitle>
          </CardHeader>
          <CardContent>
           <Skeleton class="h-60 md:h-50 w-full bg-black"/>
          </CardContent>
        </Card>
      {/each}
    </div>
  {:else}
    {#if movies.length === 0 && search_string.trim().length !== 0}
      <p class="text-white text-3xl">No movies found (&gt;_&lt;)</p>
    {:else}
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        {#each movies as movie}
          <Card class="gap-3" onclick={on_movie_selection}>
            <CardHeader>
              <CardTitle class="overflow-hidden text-ellipsis whitespace-nowrap">{movie.original_title}</CardTitle>
            </CardHeader>
            <CardContent class="text-center">
              {#if movie.poster_path}
                <img src={poster_prefix + movie.poster_path} alt="">
              {:else}
                <p>No poster available</p>
                <p>(⋟﹏⋞)</p>
              {/if}
            </CardContent>
          </Card>
        {/each}
      </div>
    {/if}
  {/if}
</div>
