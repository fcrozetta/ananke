from datetime import datetime
from pathlib import Path
import scrapy


class AzurecliSpider(scrapy.Spider):
    name = "azurecli"
    allowed_domains = ["learn.microsoft.com"]
    start_urls = ["https://learn.microsoft.com/en-us/cli/azure/release-notes-azure-cli"]
    versions = []
    tags = [
        "App Service",
        "Container app",
        "Core",
        "Cosmos DB",
        "Network",
        "SQL",
        "Storage",
        "Key Vault",
        "Profile",
        "Security",
        "ARM",
        "Containerapp",
        "Monitor",
        "AD",
        "Upgrade",
    ]

    def _clean_tag(self, input: str, tag: str):
        return input.split(">")[1].split("<")[0]

    def convert_release_date(self,date:str) -> str:
        tmp_date = datetime.strptime(date, "%B-%d-%Y")
        return tmp_date.isoformat()

    def _to_dict(self, list_html: list[str], release_index=0) -> dict:
        result = []
        version = None
        resource = None
        for item in list_html:

            item_prefix = item[:3]
            if item_prefix == "<p>":
                """version"""
                version = self._clean_tag(item, "p")
                result = {"_release_date": self.convert_release_date(self.versions[release_index])}
            elif item_prefix == "<h3":
                resource = self._clean_tag(item, "h3")
            elif item_prefix == "<ul":
                changes = (
                    item.removeprefix("<ul>")
                    .removesuffix("</ul>")
                    .replace("\n", "")
                    .replace("<li>", "")
                    .split("</li>")
                )
                changes.pop()

                result[resource] = changes
        return (version,result)

    def _filter_tags(self, json_releases):
        filtered_list = []

    def _get_releases(self, response):
        return response.xpath("//h2[not(ancestor::nav)]/@id").getall()

    def _get_latest_release_notes(self, response, index=0):
        tmp = response.xpath(
            f"//h2[@id='{self.versions[index]}']/following-sibling::*[count(preceding-sibling::h2[1][@id='{self.versions[index]}'])=1 and count(following-sibling::h2[1][@id='{self.versions[index +1]}'])=1]"
        ).getall()
        return tmp

    def _get_last_x(self, response, number: int):
            result = {}
            for x in range(number):
                version,data = self._to_dict(self._get_latest_release_notes(response, x), x)
                result[version] = data
            return result

    def parse(self, response):
        self.versions = self._get_releases(response)
        # this require a -o parameter to have an output file
        return self._get_last_x(response, 5)
            
