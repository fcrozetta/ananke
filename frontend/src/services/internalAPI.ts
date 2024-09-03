export class InternalAPI {
	private url: string;

	constructor() {
		this.url = 'http://0.0.0.0:8000';
	}

	//! SPIDERS
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

	// ! Scheduler
	async getCronJobs() {
		return await this.getData('/cron/mock')
			.then((res) => {
				let result = res.json();
				return result;
			})
			.catch((err) => {
				console.error(err);
			});
	}

	async addCronTask() {
		return await this.postData('/cron', {})
			.then((res) => {
				let result = res.json();
				return result;
			})
			.catch((err) => {
				console.error(err);
			});
	}

	// ! internal calls
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
