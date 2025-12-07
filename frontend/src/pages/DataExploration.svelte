<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Select from "$lib/components/ui/select/index.js";
  import ChartJSTrendline from 'chartjs-plugin-trendline';
  import type { Exploration } from "../types/types";
  import { API_URL } from "../const/const";
  import { Chart } from "chart.js/auto";
  import { Skeleton } from "$lib/components/ui/skeleton/index.js";
  import { currency_formatter, number_formatter } from "./reuse";
  import { onMount, onDestroy } from "svelte";

  let showLineOfBestFit = $state(false);
  let loading = $state(false);

  //Parameters
  let parameter_selection = $state("budget");

  let parameter_options: Record<string, string> = {
    "budget": "Budget",
    "release_month": "Release Month",
    "runtime": "Runtime",
    "popularity": "Popularity",
    "vote_count": "Vote Count",
    "vote_average": "Vote Average",
    "number_of_spoken_languages": "Number of Languages",
    "number_of_production_countries": "Number of Production Countries",
    "number_of_production_companies": "Number of Production Companies"
  }

  // Genre
  let genres: string[] = $state([]);
  let genres_selection = $derived(genres.join(', '));
  let genre_options = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", 
                      "Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction",
                      "Thriller", "TV Movie", "War", "Western"];

  let chartElem: HTMLCanvasElement;
  let chartInstance: Chart;
  let exploration = $state<Exploration | null>(null);

  const trendline = {
    colorMin: "red",
    lineStyle: "solid",
    width: 3,
    label: {
      display: false,
    }
  }

  const data = {
    datasets: [{
      label: 'Scatter Dataset',
      data: [],
      backgroundColor: '#0F93D4',
    }]
  };

  const commonConfig = {
    border: {
      color: "#FFFFFF"
    },
    ticks: {
      color: '#FFFFFF',
      callback: (value: number, _index: number, _ticks: any[]) => {
        return currency_formatter.format(value);
      }
    }
  }

  const config = {
    type: 'scatter',
    data: data,
    options: {
      aimation: false,
      responsive: true,
      maintainAspectRatio: false,
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
              return `${xLabel}: ${currency_formatter.format(xValue)}, ${yLabel}: ${currency_formatter.format(yValue)}`;
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
            text: 'Budget',
            color: '#FFFFFF',
            display: true
          },
          ...commonConfig
        },
        y: {
          title: {
            text: 'Revenue',
            color: '#FFFFFF',
            display: true
          },
          ...commonConfig
        }
      }
    }
  };

  onMount(async () => {
    Chart.register(ChartJSTrendline);
    chartElem = document.getElementById("scatter-chart") as HTMLCanvasElement;

    if (chartElem) {
      chartInstance = new Chart(chartElem, config as any)
    }

    exploration = await fetchExploration();
    (config.data.datasets[0] as any).data = $state.snapshot(exploration?.plot_dataset);
    chartInstance.update();
  })

  onDestroy(() => {
    chartElem?.remove();
  })

  async function updateChart() {
    exploration = await fetchExploration();
    (config.data.datasets[0] as any).data = $state.snapshot(exploration?.plot_dataset);
    chartInstance.update();
  }

  async function onParameterChange(x_param: string) {
    config.options.scales.x.title.text = parameter_options[x_param];
    updateChart();
  }

  async function fetchExploration(): Promise<Exploration> {
    loading = true;
    const url = new URL(`${API_URL}/exploration`);
    const searchParams = url.searchParams;
    if (parameter_selection) {
      searchParams.set("x_param", parameter_selection);
    }
    if (genres_selection) {
      searchParams.set("genres", genres_selection);
    }
    const exploration_res = await fetch(url)
    loading = false;
    return await exploration_res.json();
  }

  function onCheckShowLineOfBestFit() {
    if (showLineOfBestFit) {
      (config.data.datasets[0] as any).trendlineLinear = trendline;
    } else {
      delete (config.data.datasets[0] as any).trendlineLinear;
    }
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
      <Select.Root type="single" bind:value={parameter_selection} onValueChange={onParameterChange}>
          <Select.Trigger class="w-full">{parameter_options[parameter_selection]}</Select.Trigger>
          <Select.Content>
            {#each Object.entries(parameter_options) as [parameter_value, parameter_option]}
              <Select.Item value={parameter_value}>{parameter_option}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
    </div>
    <div class="flex flex-col flex-1 overflow-hidden">
      <p class="text-white mb-2">
        Filter by Genre
      </p>
      <Select.Root type="multiple" bind:value={genres} onValueChange={updateChart}>
          <Select.Trigger class="w-full">
            <div class="overflow-hidden text-ellipsis">{genres_selection ? genres_selection : "Select genres"}</div>
          </Select.Trigger>
          <Select.Content>
            {#each genre_options as genre_option}
              <Select.Item value={genre_option}>{genre_option}</Select.Item>
            {/each}
          </Select.Content>
        </Select.Root>
    </div>
    <div class="flex gap-2 mb-2 flex-1">
      <input type="checkbox" bind:checked={showLineOfBestFit} onchange={onCheckShowLineOfBestFit}/>
      <label class="text-white">Show Line of Best Fit</label>
    </div>
  </div>

  <div class="bg-dark-blue-3 gap-3 border border-blue-gray-2 rounded-xl flex p-9 mt-5 mb-5">
    <div class="min-h-100 w-full">
      <canvas id="scatter-chart"></canvas>
    </div>
  </div>

  <div class="flex justify-between gap-4 mb-5 flex-col md:flex-row">
    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Movies</Card.Title>
      </Card.Header>
      <Card.Content> 
        {#if loading}
          <Skeleton class="h-10 w-2/3 bg-light-gray"/>
        {:else}
          <p class="text-4xl font-extrabold text-white">{exploration?.total_number_of_movies ? number_formatter.format(exploration?.total_number_of_movies) : "-"}</p>
        {/if}
      </Card.Content>
    </Card.Root>  

    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Average Revenue</Card.Title>
      </Card.Header>
      <Card.Content>
        {#if loading}
          <Skeleton class="h-10 w-2/3 bg-light-gray"/>
        {:else}
          <p class="text-white text-4xl font-extrabold">{exploration?.average_revenue ? currency_formatter.format(exploration?.average_revenue) : "-"}</p>
        {/if}
      </Card.Content>
    </Card.Root>  

    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Average Budget</Card.Title>
      </Card.Header>
      <Card.Content>
        {#if loading}
          <Skeleton class="h-10 w-2/3 bg-light-gray"/>
        {:else}
          <p class="text-white text-4xl font-extrabold">{exploration?.average_budget ? currency_formatter.format(exploration?.average_budget) : "-"}</p>
        {/if}
      </Card.Content>
    </Card.Root>

    <Card.Root class="flex-1 bg-dark-blue-3 gap-4 border-blue-gray-2">
      <Card.Header>
        <Card.Title class="text-light-gray">Highest Revenue</Card.Title>
      </Card.Header>
      <Card.Content>
        {#if loading}
          <Skeleton class="h-10 w-2/3 bg-light-gray"/>
        {:else}
          <p class="text-white text-4xl font-extrabold">{exploration?.highest_revenue ? currency_formatter.format(exploration?.highest_revenue) : "-"}</p>
        {/if}
      </Card.Content>
    </Card.Root>
  </div>
</div>
