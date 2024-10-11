import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing the tables
url = 'https://www.languagecourse.net/languages-worldwide'

# Fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables on the page
tables = soup.find_all('table')

# Loop through all tables found
for idx, table in enumerate(tables):
    # Extract headers (if they exist)
    headers = [th.text.strip() for th in table.find_all('th')]
    
    # Extract rows
    rows = []
    for tr in table.find_all('tr'):
        cells = [td.text.strip() for td in tr.find_all(['td', 'th'])]
        if cells:
            rows.append(cells)
    
    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers if headers else None)
    
    # Save each table to a separate CSV file
    csv_filename = f'table_{idx + 1}.csv'
    df.to_csv(csv_filename, index=False)
    
    print(f"Table {idx + 1} has been saved to '{csv_filename}'")
