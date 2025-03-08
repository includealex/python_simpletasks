from bs4 import BeautifulSoup
import re

DATE_REGEXP = r"\d{,2} (?:[яЯ]нваря|[фФ]евраля|[мМ]арта|[аА]преля|[мМ]ая|[иИ]ю[лн]я|[аА]вгуста|[сС]ентября|[оО]ктября|[нН]оября|[дД]екабря) \d{4}"
NOT_WIKI_REGEXP="^((?!wiki/).)*$"

input_filename = "armenia.html"

with open(input_filename, "r") as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

images = soup.find_all("img")
print(f"На странице {len(images)} изображений.")

table_rows = soup.find_all("th", attrs={"class": "plainlist"})
print(f"В таблице с описанием государства {len(table_rows)} рядов.")

text_format = soup.get_text()
text_words_num = len(text_format.split())
print(f"В тексте {text_words_num} слов.")

dates = (re.findall(re.compile(DATE_REGEXP), text_format))
print(f"В тексте статьи {len(dates)} дат.")

n_total_links = len(soup.find_all("a"))
n_self_links = len(soup.find_all("a", attrs={"class": "mw-selflink selflink"}))
n_external_links = len(soup.find_all("a", attrs={"href": re.compile(NOT_WIKI_REGEXP)}))
n_other_links = n_total_links - n_self_links - n_external_links

print(f"Ссылок в статье: {n_total_links}, из них:\n"
      f"- {n_external_links} ведущих не на Википедию,\n"
      f"- {n_self_links} ведущих на саму себя,\n"
      f"- {n_other_links} других."
      )
