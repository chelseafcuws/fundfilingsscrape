import requests
import json
import pandas as pd

CIK = '0001655888'

header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
resp = requests.get(f'https://data.sec.gov/submissions/CIK{CIK}.json', headers=header)
data = resp.json()['filings']['recent']

df = pd.DataFrame(data)
df['CIK'] = CIK
df = df[['CIK', 'accessionNumber', 'filingDate', 'reportDate', 'acceptanceDateTime', 'act', 'form', 'fileNumber', 'filmNumber', 'items', 'size', 'isXBRL', 'isInlineXBRL', 'primaryDocument', 'primaryDocDescription']]

df.to_excel('1. Funds filing history.xlsx', index=False)