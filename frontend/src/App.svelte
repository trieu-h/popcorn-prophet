<script lang="ts">
  import { Router } from 'sv-router';
  import { isActiveLink } from 'sv-router';
  import logo from './assets/logo.png'
  import './router.ts';

  const base = import.meta.env.PROD ? "popcorn-prophet" : undefined;
</script>

<main>
    <header class="text-white flex justify-between items-center max-md:items-start max-md:gap-3 border-b border-dark-gray p-5 max-md:flex-col">
      <div class="flex items-center gap-3">
        <img src={logo} class="w-10 h-10">
        <!-- <a class="hover:text-light-gray active:text-light-blue font-bold text-xl" href="/" use:isActiveLink={{ className: 'text-light-blue' }}>Popcorn Prophet</a> -->
        <a class="font-bold text-xl">Popcorn Prophet</a>
      </div>
      <ul class="flex gap-10 self-end">
        <li><a class="hover:text-light-gray active:text-light-blue" href="/data-exploration" use:isActiveLink={{ className: 'text-light-blue' }}>Data Exploration</a></li>
        <li><a class="hover:text-light-gray active:text-light-blue" href="/prediction" use:isActiveLink={{ className: 'text-light-blue', startsWith: true }}>Prediction</a></li>
        <li><a class="hover:text-light-gray active:text-light-blue" href="/analytics" use:isActiveLink={{ className: 'text-light-blue', startsWith: true }}>Analytics</a></li>
      </ul>
    </header>

    <Router base={base}></Router>
</main>

