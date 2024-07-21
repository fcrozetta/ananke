export class InternalAPI {
	private url: string;

	constructor() {
		this.url = 'http://0.0.0.0:8000';
	}

	async listSpiders() {
		return await this.getData('/spiders')
			.then((res) => {
				return res.json();
			})
			.catch((err) => console.error(err));
	}

	async runSpider(spiderName: string) {
		return await this.getData('/spiders/' + spiderName)
			.then((res) => {
				let result = res.json();
				console.log(result);

				return result;
			})
			.catch((err) => {
				console.error(err);
			});
	}

	private async getData(endpoint: string): Promise<Response> {
		return await fetch(this.url + endpoint);
	}

	private async postData(endpoint: string, data: any): Promise<Response> {
		const options = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(data)
		};
		return await fetch(this.url + endpoint, options);
	}
}
