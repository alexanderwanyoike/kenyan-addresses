import json
import requests
from bs4 import BeautifulSoup
import math

URL = "https://www.businesslist.co.ke/location/%s/%d"
TOWNS = ['Nairobi', 'Mombasa', 'Kisumu', 'Kiambu', 'Kisii', 'Kakamega', 'Nakuru', 'Thika', 'Nyeri', 'Naivasha',
         'Eldoret', 'Embu', 'Kitui', 'Meru', 'Homa-Bay']


def parse_to_address(item, town):
    address_line1 = item.find('h4')
    address_line2 = item.find('div', {"class": "address"})
    return {
        "addressLine1": address_line1.text,
        "addressLine2": address_line2.text,
        "town": town,
    }


def get_address(total_address, towns=None):
    if towns is None:
        towns = TOWNS

    address_per_town = math.floor(total_address / len(towns))
    addresses = []
    for town in towns:
        town_lower = town.lower()
        total_companies = 0
        page_number = 1
        company_elms = []
        while len(company_elms) < address_per_town:
            town_url = URL % (town_lower, page_number)
            print(town_url)
            page = requests.get(town_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            for item in soup.select('div[id*="cmap_"]'):
                if len(company_elms) > address_per_town:
                    break
                company_elms.append(item)
            page_number = page_number + 1

        for company_elm in company_elms:
            addresses.append(parse_to_address(company_elm, town))

        # for i in range(1, address_per_town):
    return addresses


if __name__ == "__main__":
    addresses = get_address(200)
    print(len(addresses))
    with open('output.json', 'w') as fp:
        json.dump(addresses, fp)
