import re
import os
import json
import time
import requests
import datetime
from bs4 import BeautifulSoup
from argparse import ArgumentParser


def scrape(link, get_link=False):
	r = requests.post(link).content.decode('utf-8')
	r = re.sub("[\r\t\f\v\n]", "", r)
	r = re.sub("<[ /]*br[ /]*>", "\n", r)
	r = re.sub(" +", " ", r)
	r = re.sub("\u200b|\u3000", "", r)
	r = re.sub("<!--([\w\W]*?)-->", "", r)

	date = re.search("20\\d\\d\-[0-1]\\d\-[0-3]\\d", r).group(0)

	page = BeautifulSoup(r.encode("utf-8"), "html.parser")

	# "All information published on this website is authentic in Chinese. English is provided for reference only"
	title = page.find("div", {"class": "art-title"}).get_text()
	content = page.find("div", {"class": "art-con-bottonmLine"})

	zh_link = content.find("div").find("a")["href"] if get_link else None

	# date = content.find("section", {"class": "article-tool"}).find("div").find("p").get_text()

	# print(content.get_text())
	# paragraphs = [paragraph for p in content.find_all("p")[:-1] if (paragraph := p.get_text().strip()) != ""]

	paragraphs = []

	if text := content.find("p").find_all("p"):
		# text in p in p in div
		for p in text:
			paragraphs.extend(p.get_text().split("\n"))
	else:
		for p in content.find_all("p"):
			# text in div
			if not p.name:
				paragraphs.extend(p.split("\n"))
			# text in p in div
			elif p.name == "p":
				paragraphs.extend(p.get_text().split("\n"))

	paragraphs = [p.strip() for p in paragraphs if p.strip() != "(All information published on this website is authentic in Chinese. English is provided for reference only.)" and p.strip() != ""]

	return (paragraphs, title, date, zh_link)


def main():
	parser = ArgumentParser(prog="cli")
	parser.add_argument("-d", "--date", help="Starting date of press release (Inclusive)", nargs="?", default="2012-01-01")
	args = parser.parse_args()
	args_date = args.date.replace("-", "")

	if not os.path.exists("output"):
		os.makedirs("output")

	links = []
	page_count = 1
	while page_count <= 200:
		link = "http://english.mofcom.gov.cn/article/newsrelease/significantnews/" + ( f"?{page_count}" if page_count > 1 else "")
		# print(link)
		page = BeautifulSoup(requests.post(link).text, "html.parser")
		for news in page.find_all("a", {"href": re.compile("/article/newsrelease/significantnews")}):
			if numbers := re.search("\/\\d{6}\/(\\d{14})\.shtml", news.get("href")):
				if numbers.group(1)[:6] < args_date:
					break
				links.append(numbers.group(1))
		page_count += 1
		# TEMPORARY BREAK
		break

	for link in links:
		print(link)
		en_link = f"http://english.mofcom.gov.cn/article/newsrelease/significantnews/{link[:6]}/{link}.shtml"

		(en_paragraphs, en_title, date, zh_link) = scrape(en_link, True)
		(zh_paragraphs, zh_title, _, _) = scrape(zh_link)
		
		data = {
			"en_url": en_link,
			"zh_url": zh_link,
			"category": "Significant News",
			"en_title": en_title,
			"zh_title": zh_title,
			"release_date": date,
			"para_aligned_status": len(en_paragraphs) == len(zh_paragraphs),
			"contents": {
				"en": en_paragraphs,
				"zh": zh_paragraphs
			}
		}

		with open(f"output/{link}.json", "w") as json_file:
			json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
	main()
