import re
import requests
from bs4 import BeautifulSoup

SNP_id = 'rs7241918'
base_addr = 'https://www.ncbi.nlm.nih.gov/snp/'
filter_loc = 'GRCh37'

def get_addr(id):
    return base_addr + SNP_id


def get_loc():
    target_addr = get_addr(SNP_id)
    r = requests.get(target_addr)

    soup = BeautifulSoup(r.text, 'html.parser')
    raw_data = soup.find('div', id='gene_plac_allele').find_all('td')

    n = 0
    filter_pattern = re.compile(filter_loc)

    while n < len(raw_data):
        key_tag = raw_data[n]
        value_tag = raw_data[n + 1]
        key_ = key_tag.string
        value_ = value_tag.string

        if filter_pattern.match(key_):
            loc_pattern = re.compile(r'\.\d+[A-Z]')
            middle = loc_pattern.search(value_).group(0)
            return re.search(r'\d+', middle).group(0)

        n += 2

print(get_loc())




