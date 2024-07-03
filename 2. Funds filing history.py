import requests
import json
import pandas as pd

CIK = ['0001678124', '0001803498', '0001842754', '0001736035', '0001061630', '0001735964']

df = pd.DataFrame()
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
for cik in CIK:
    resp = requests.get(f'https://data.sec.gov/submissions/CIK{cik}.json', headers=header)
    data = resp.json()['filings']['recent']
    temp_df = pd.DataFrame(data)
    temp_df['CIK'] = cik
    df = pd.concat([df, temp_df])

df = df[['CIK', 'accessionNumber', 'filingDate', 'reportDate', 'acceptanceDateTime', 'act', 'form', 'fileNumber', 'filmNumber', 'items', 'size', 'isXBRL', 'isInlineXBRL', 'primaryDocument', 'primaryDocDescription']]
df['reportDate'] = pd.to_datetime(df['reportDate'])
df['reportDate'] = df['reportDate'].dt.strftime('%m/%d/%Y')
df['filingDate'] = pd.to_datetime(df['filingDate'])
df['filingDate'] = df['filingDate'].dt.strftime('%m/%d/%Y')

df.to_excel('2. Funds filing history.xlsx', index=False)