<script lang="ts">
  import { Router } from 'sv-router';
  import { isActiveLink } from 'sv-router';
  import logo from './assets/logo.png'
  import './router.ts';

  const base = import.meta.env.PROD ? "popcorn-prophet" : undefined;
</script>

<main>
    <header class="text-white flex justify-between items-center border-b border-dark-gray p-5">
      <div class="flex items-center gap-3">
        <img src={logo} class="w-10 h-10">
        <a class="hover:text-light-gray active:text-light-blue font-bold text-xl" href="/" use:isActiveLink={{ className: 'text-light-blue' }}>Popcorn Prophet</a>
      </div>
      <div>
        <ul class="flex gap-10">
          <li><a class="hover:text-light-gray active:text-light-blue" href="/data-exploration" use:isActiveLink={{ className: 'text-light-blue' }}>Data Exploration</a></li>
          <li><a class="hover:text-light-gray active:text-light-blue" href="/prediction" use:isActiveLink={{ className: 'text-light-blue', startsWith: true }}>Prediction</a></li>
          <li><a class="hover:text-light-gray active:text-light-blue" href="/analytics" use:isActiveLink={{ className: 'text-light-blue', startsWith: true }}>Analytics</a></li>
        </ul>
      </div>
    </header>

    <Router base={base}></Router>
</main>

