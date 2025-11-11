import { createRouter } from 'sv-router';
import Analytics from "./pages/Analytics.svelte";
import AnalyticsResult from "./pages/AnalyticsResult.svelte";
import DataExploration from "./pages/DataExploration.svelte";
import Prediction from "./pages/Prediction.svelte";
import Introduction from "./pages/Introduction.svelte";

export const { p, navigate, isActive, route } = createRouter({
	'/analytics': Analytics,
	'/analytics/result': AnalyticsResult,
	'/data-exploration': DataExploration,
	'/prediction': Prediction,
	'/': Introduction
});
