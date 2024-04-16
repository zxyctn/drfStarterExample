<script lang="ts">
	import mercedes_benz from '$lib/images/mercedes_benz.png';
	import bmw from '$lib/images/bmw.png';
	import audi from '$lib/images/audi.png';

	export let row;

	const brand: 'Mercedes-Benz' | 'BMW' | 'Audi' = row.original.brand;

	const logos = {
		'Mercedes-Benz': mercedes_benz,
		BMW: bmw,
		Audi: audi
	};
</script>

<img src={logos[brand]} alt={brand} class="h-10" />
