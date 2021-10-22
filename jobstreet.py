from bs4 import BeautifulSoup
import requests

job_name = "python programmer"
html_text = requests.get(f"https://www.jobstreet.co.id/id/job-search/{job_name}-jobs/").text
web_html = BeautifulSoup(html_text, "lxml")

kerjaan = web_html.find_all("div", attrs={'class':'sx2jih0','data-automation':'jobListing'})

job = web_html.find_all("div", class_="sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0")
company = web_html.find_all("span", class_="sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8")
location = web_html.find_all("span", class_="sx2jih0 zcydq82q zcydq810 iwjz4h0")
salary = web_html.find_all("span", class_="sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6")
published = web_html.find_all("span", class_="sx2jih0 zcydq82q _18qlyvc0 _18qlyvcx _18qlyvc1 _18qlyvc6")

for x in range(len(job)):
	result = "========================="
	result += f"\nJob = {job[0+x].text}"
	result += f"\nCompany Name = {company[21+x].text}"
	result += f"\nLocation = {location[3+x].text}"
	result += f"\nSalary = {salary[1+x].text if 'IDR' in salary[1+x].text else '-'}"
	result += f"\nPublished = {published[0+x].text}"
	print(result)
