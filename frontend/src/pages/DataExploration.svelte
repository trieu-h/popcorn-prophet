<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import { Chart } from "chart.js/auto";
  import { onMount, onDestroy } from "svelte";

  //Parameters
  let parameterSelection = $state("Budget");
  let parameterOptions = ["Budget", "Release Month", "Runtime", "Popularity", "Vote Count", "Vote Average", "Number of Languages", 
                      "Number of Production Companies", "Number of Production Countries"];

  // Genre
  let genres: string[] = $state([]);
  let genresSelection = $derived(genres.join(', '));
  let genreOptions = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", 
                      "Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction",
                      "Thriller", "TV Movie", "War", "Western"];

  let chartElem: HTMLCanvasElement;
  let chartInstance: Chart;

  const data = {
    datasets: [{
      label: 'Scatter Dataset',
      data: [{
        x: -10,
        y: 0
      }, {
        x: 0,
        y: 10
      }, {
        x: 10,
        y: 5
      }, {
        x: 0.5,
        y: 5.5
      }],
      backgroundColor: '#0F93D4'
    }],
  };

  const commonConfig = {
    border: {
      color: "#FFFFFF"
    },
    ticks: {
      color: '#FFFFFF'
    }
  }

  const config = {
    type: 'scatter',
    data: data,
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          callbacks: {
            label: function(context: any) {
              const xLabel = config.options.scales.x.title.text;
              const yLabel = config.options.scales.y.title.text;
              const xValue = context.parsed.x;
              const yValue = context.parsed.y;
              return `${xLabel}: ${xValue}, ${yLabel}: ${yValue}`;
            }
          }
        }
      },
      elements: {
        point: {
          radius: 5,
          hoverRadius: 8
        }
      },
      scales: {
        x: {
          type: 'linear',
          position: 'bottom',
          title: {
            text: 'Budget (Millions $)',
            color: '#FFFFFF',
            display: true
          },
          ...commonConfig
        },
        y: {
          title: {
            text: 'Revenue (Millions $)',
            color: '#FFFFFF',
            display: true
          },
          ...commonConfig
        }
      }
    }
  };

  onMount(() => {
    chartElem = document.getElementById("scatter-chart") as HTMLCanvasElement;

    if (chartElem) {
      chartInstance = new Chart(chartElem, config as any)
    }
  })

  onDestroy(() => {
    if (chartElem) {
      chartElem.remove();
    }
  })

  function onParameterChange(parameter: string) {
    config.options.scales.x.title.text = parameter;
    chartInstance.update();
  }
</script>

<div class="flex flex-col max-w-7xl mx-auto pt-10 px-6">
  <div class="mb-5">
    <h1 class="text-white text-3xl font-bold pb-2">Data Exploration</h1>
    <p class="text-gray-2">Explore the relationship between movie parameters and box office revenue</p>
  </div>

  <div class="bg-dark-blue-3 gap-3 border border-blue-gray-2 rounded-xl flex p-5 items-end">
    <div class="flex flex-col flex-1">
      <p class="text-white mb-2">
        Select Parameter
      </p>
      <Select.Root type="single" bind:value={parameterSelection} onValueChange={onParameterChange}>
          <Select.Trigger class="w-full">{parameterSelection}</Select.Trigger>
          <Select.Content>
            {#each parameterOptions as parameterOption}
              <Select.Item value={parameterOption}>{parameterOption}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
    </div>
    <div class="flex flex-col flex-1">
      <p class="text-white mb-2">
        Filter by Genre
      </p>
      <Select.Root type="multiple" bind:value={genres}>
          <Select.Trigger class="w-full">{genresSelection}</Select.Trigger>
          <Select.Content>
            {#each genreOptions as genreOption}
              <Select.Item value={genreOption}>{genreOption}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
    </div>
    <div class="flex gap-2 mb-2 flex-1">
      <input type="checkbox" checked={false} />
      <label class="text-white">Show Line of Best Fit</label>
    </div>
  </div>

  <div class="bg-dark-blue-3 gap-3 border border-blue-gray-2 rounded-xl flex p-9 mt-5 mb-5">
    <canvas id="scatter-chart"></canvas>
  </div>

  <div class="flex justify-between gap-4 mb-5">
    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Movies</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-4xl font-extrabold text-white">15</p>
      </Card.Content>
    </Card.Root>  

    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Average Revenue</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-white text-4xl font-extrabold">$1425M</p>
      </Card.Content>
    </Card.Root>  

    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Average Budget</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-white text-4xl font-extrabold">$167M</p>
      </Card.Content>
    </Card.Root>
    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Highest Revenue</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-white text-4xl font-extrabold">$2923M</p>
      </Card.Content>
    </Card.Root>
  </div>

</div>

<style>
</style>
