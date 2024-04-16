<script lang="ts">
	import { Render, Subscribe, createRender, createTable } from 'svelte-headless-table';
	import type { Writable } from 'svelte/store';

	import Logo from './Logo.svelte';

	export let data: Writable<
		{ brand: 'Mercedes-Benz' | 'BMW' | 'Audi'; model: string; year: number }[]
	>;

	const table = createTable(data);

	const columns = table.createColumns([
		table.display({
			header: '',
			cell: ({ row }) => createRender(Logo, { row })
		}),
		table.column({
			header: 'Brand',
			accessor: 'brand'
		}),
		table.column({
			header: 'Model',
			accessor: 'model'
		}),
		table.column({
			header: 'Year',
			accessor: 'year'
		})
	]);

	const { headerRows, rows, tableAttrs, tableBodyAttrs } = table.createViewModel(columns);
</script>

<table {...$tableAttrs} class="table table-auto table-compact w-max h-max">
	<thead>
		{#each $headerRows as headerRow (headerRow.id)}
			<Subscribe rowAttrs={headerRow.attrs()} let:rowAttrs>
				<tr {...rowAttrs}>
					{#each headerRow.cells as cell (cell.id)}
						<Subscribe attrs={cell.attrs()} let:attrs>
							<th {...attrs}>
								<Render of={cell.render()} />
							</th>
						</Subscribe>
					{/each}
				</tr>
			</Subscribe>
		{/each}
	</thead>
	<tbody {...$tableBodyAttrs}>
		{#each $rows as row (row.id)}
			<Subscribe rowAttrs={row.attrs()} let:rowAttrs>
				<tr {...rowAttrs}>
					{#each row.cells as cell (cell.id)}
						<Subscribe attrs={cell.attrs()} let:attrs>
							<td {...attrs} class="h-full">
								<div class="flex h-full items-center"><Render of={cell.render()} /></div>
							</td>
						</Subscribe>
					{/each}
				</tr>
			</Subscribe>
		{/each}
	</tbody>
</table>
