<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import ArrowLeft from "@lucide/svelte/icons/arrow-left";
  import Play from "@lucide/svelte/icons/play";
  import { navigate } from "../router";
  import { onMount } from "svelte";
  import { form } from "./states.svelte";
  import { API_URL } from "../const/const";
  import type { Prediction } from "src/types/types";

  let projected_revenue = $state<number>();

  function backToInput() {
    const prediction_wrapper = document.querySelector("#prediction-wrapper") as HTMLDivElement;
    prediction_wrapper.style.viewTransitionName = "prediction-wrapper-back";
    navigate('/prediction', { viewTransition: true });
  }

  function runSimulation() {
    navigate('/prediction/result/simulation', { viewTransition: true });
  }

  const currency_formatter = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });

  onMount(async () => {
    const res = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    });

    const prediction_res: Prediction = await res.json();
    projected_revenue = prediction_res.predicted_revenue;
  })
</script>

<div class="flex flex-col max-w-7xl mx-auto pt-10 px-6" id="prediction-wrapper">
  <div class="flex justify-between mb-3">
    <div>
      <h1 class="text-white text-3xl font-bold pb-2">Prediction Result</h1>
      <p class="text-gray-2 pb-7">Based on the data you provided, here's our prediction</p>
    </div>
  </div>

  <div class="flex justify-between gap-4 mb-5 flex-col md:flex-row">
    <Card.Root class="flex-1 bg-blue-gray gap-4 border-blue-gray-2 min-w-0">
      <Card.Header>
        <Card.Title class="text-white">Projected Revenue</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-4xl font-extrabold text-light-blue">{projected_revenue ? currency_formatter.format(projected_revenue) : "-"}</p>
      </Card.Content>
    </Card.Root>  

    <Card.Root class="flex-1 bg-blue-gray gap-4 border-blue-gray-2 min-w-0">
      <Card.Header>
        <Card.Title class="text-white">Confidence</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-white text-4xl font-extrabold">85%</p>
      </Card.Content>
    </Card.Root>  

    <Card.Root class="flex-1 bg-blue-gray gap-4 border-blue-gray-2 min-w-0">
      <Card.Header>
        <Card.Title class="text-white">Verdict</Card.Title>
      </Card.Header>
      <Card.Content>
        <p class="text-white text-4xl font-extrabold">Potential Blockbuster</p>
      </Card.Content>
    </Card.Root>
  </div>

  <p class="text-gray-2 self-center mb-12">Confidence interval: $135M - $165M</p>
  
  <div class="bg-blue-gray border border-blue-gray-2 rounded-xl px-8 py-6 mb-10 ">
    <h1 class="text-white font-bold text-xl mb-5">How It Compares</h1>

    <div class="overflow-auto">
      <table class="text-white w-full">
        <thead class="text-left">
          <tr class="border-b border-blue-gray-2">
            <th class="px-4 py-3">Movie Title</th>
            <th class="px-4 py-3">Genre</th>
            <th class="px-4 py-3 text-right">Actual Box Office</th>
            <th class="px-4 py-3 text-right">Vote Average</th>
            <th class="px-4 py-3 text-right">Number of Votes</th>
            <th class="px-4 py-3 text-right">Budget</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-blue-gray-2">
            <td class="px-4 py-5">Movie 1</td>
            <td class="px-4 py-5">Sci-fi</td>
            <td class="px-4 py-5 text-right">$270M</td>
            <td class="px-4 py-5 text-right">7.8</td>
            <td class="px-4 py-5 text-right">3400</td>
            <td class="px-4 py-5 text-right">$45M</td>
          </tr>
          <tr class="border-b border-blue-gray-2">
            <td class="px-4 py-5">Movie 2</td>
            <td class="px-4 py-5">Adventure</td>
            <td class="px-4 py-5 text-right">$20M</td>
            <td class="px-4 py-5 text-right">7.8</td>
            <td class="px-4 py-5 text-right">3400</td>
            <td class="px-4 py-5 text-right">$45M</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="self-center flex gap-3">
    <Button variant="gray" onclick={backToInput}>
      <ArrowLeft/>
      Back to Input
    </Button>
    <Button variant="blue" onclick={runSimulation}>
      <Play/>
      Run Simulation
    </Button>
  </div>
</div>

<style>
  #prediction-wrapper {
    view-transition-name: prediction-wrapper;
  }
</style>
