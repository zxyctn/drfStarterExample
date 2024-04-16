import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
	let response;

	try {
		response = await fetch('http://127.0.0.1:8000/cars/');
	} catch (error) {
		console.error('Error fetching data: ', error);
		throw new Error(`Error fetching data: ${error}`);
	}

	const data = await response.json();

	if (response?.status !== 200) {
		console.error('Error fetching data: ', response.body);
		throw new Error(`Error fetching data: ${response.body}`);
	}

	console.log(data.results);

	return {
		data: data.results
	};
};
