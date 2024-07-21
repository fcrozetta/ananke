import subprocess, os, json


class Spider:
    root_folder = "src/spiders/"

    def _clean_file(self, filename: str):
        if os.path.exists(filename):
            os.remove(filename)

    def list_spiders(self):
        filenames = [
            x.replace("_spider.py", "")
            for x in next(os.walk(self.root_folder), (None, None, []))[2]
        ]
        return filenames

    def retrieve_data(self, spider_name: str) -> dict:
        filename = f"{spider_name}.json"
        self._clean_file(filename)
        cmd = f"./.venv/bin/scrapy runspider src/spiders/{spider_name}_spider.py -o {filename}"
        process = subprocess.Popen(cmd.split())
        process.communicate()
        with open(filename, "r") as fp:
            return json.load(fp)
