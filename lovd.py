import pandas as pd

#genes
genes1=pd.read_html('https://databases.lovd.nl/shared/genes?page=1')[7]

#Individuals
individuals=pd.read_html('https://databases.lovd.nl/shared/individuals?page=2')[7]

#Disease
disease=pd.read_html('https://databases.lovd.nl/shared/diseases?page=2')[8]






#variants
t2=pd.read_html('https://databases.lovd.nl/shared/variants?page=2')[7]
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing the table
url = 'https://databases.lovd.nl/shared/variants?page=2'

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the table rows (tr) with class="data" in the HTML content
    rows = soup.find_all('tr', class_='data')
    
    # Initialize an empty list to store the data and id values from rows with class="data"
    data_list = []
    
    # Iterate through each table row and extract the data and id value from each cell (td)
    for row in rows:
        id_value = row.get('id', None)  # Get the value of the 'id' attribute or None if not present
        td_elements = row.find_all('td')
        row_data = [td.get_text() for td in td_elements]
        data_list.append([id_value] + row_data)  # Add the id_value to the beginning of the row_data list
    
    # Convert the list of lists to a pandas DataFrame
    df = pd.DataFrame(data_list)
    
    # Print the DataFrame
    print(df)
else:
    print("Failed to retrieve data. Status Code:", response.status_code)

Colnames=["PatientID","Effect","Chr","Classification method","Clinical classification","DNA change (genomic) (hg19)","DNA change (hg38)","Published as",
  "ISCN","DB-ID","Variant remarks","Reference","ClinVar ID","dbSNP ID","Origin","Segregation","Frequency","Re-site","VIP","Methylation",
  "Owner"]

df.columns=Colnames
