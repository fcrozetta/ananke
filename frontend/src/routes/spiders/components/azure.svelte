<script lang="ts">
	import { InternalAPI } from '../../../services/internalAPI';
	let spiders: Array<string> = [];
	let api = new InternalAPI();

	function runSpider() {
		return api.runSpider('azurecli');
	}
</script>

<details>
	<summary>Azure Spider</summary>
	<label class="switch">
		<input type="checkbox">
		<span class="slider round"></span>
	</label>
	Breaking changes only
	{#await api.runSpider('azurecli')}
			<p>loading...</p>
		{:then data}
			{#each Object.entries(data) as [version, contents]}
				<h2>{version} - {contents['_release_date']}</h2>
				{#each Object.entries(contents) as [key, value]}
					{#if key != '_release_date'}
						<h3>{key}</h3>
						<ul>
							{#each value as v}
								<!-- Rendering the list as HTML to use the <code> tags in the lists -->
								<li>{@html v}</li>
							{/each}
						</ul>
					{/if}
				{/each}
			{/each}
		{:catch error}
			<p style="color: red">{error.message}</p>
		{/await}
</details>
	


<style>
	details {
  border: 1px solid #aaa;
  border-radius: 4px;
  padding: 0.5em 0.5em 0;
}

summary {
  font-weight: bold;
  margin: -0.5em -0.5em 0;
  padding: 0.5em;
}

details[open] {
  padding: 0.5em;
}

details[open] summary {
  border-bottom: 1px solid #aaa;
  margin-bottom: 0.5em;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}
/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
