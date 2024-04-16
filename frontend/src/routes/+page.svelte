<script lang="ts">
	import { writable } from 'svelte/store';

	import Table from '$lib/components/Table.svelte';
	import type { PageData } from './$types';

	export let data: PageData;

	let tableData = data
		? writable<{ brand: 'Mercedes-Benz' | 'BMW' | 'Audi'; model: string; year: number }[]>(
				data.data as any
			)
		: null;
</script>

{#if tableData}
	<div class="h-screen w-screen p-10 flex justify-center items-center">
		<Table data={tableData} />
	</div>
{:else}
	<p>Failed to load data</p>
{/if}
