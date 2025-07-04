from bs4 import BeautifulSoup
import requests

def scrape_ft_pea():
    page_to_scrape = requests.get("https://www.pea.co.th/en/our-services/tariff/ft")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    span_elements = soup.find_all("span", attrs={"class": "text-primary"})
    ft_element = span_elements[0].text
    return ft_element

if __name__ == "__main__":
    scrape_ft_pea()