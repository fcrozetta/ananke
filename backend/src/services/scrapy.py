import subprocess, os, json


class Spider:
    root_folder = "src/spiders/"
    scrapy_path = os.getenv("SCRAPY_PATH", "/app/backend/.venv/bin/scrapy")

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
        print("starting retrieving data")
        filename = f"{spider_name}.json"
        self._clean_file(filename)
        cmd = f"{self.scrapy_path} runspider src/spiders/{spider_name}_spider.py -o {filename}"
        process = subprocess.Popen(cmd.split())
        process.communicate()
        with open(filename, "r") as fp:
            return json.load(fp)
