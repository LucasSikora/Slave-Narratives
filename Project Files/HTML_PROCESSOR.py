import pandas as pd
from bs4 import BeautifulSoup
import re

# Load the HTML content from a file
with open('C:\\Users\Lucas\PycharmProjects\pythonProject6\HTML_Narratives\Alabama.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the modified informants_header
informants_header = soup.find('h2', string='INFORMANTS')

# Find all the <a> (anchor) tags within <li> elements under the modified informants_header
links = informants_header.find_next('ul').find_all('li')

# Create a list to store data
data = []

# Iterate over the original links and find corresponding divs
for link in links:
    # Extract the ID and remove the first character (assuming the ID is a string)
    id_value = link.find('a')['href'][1:]

    # Find the div with the corresponding ID
    div = soup.find('div', id=id_value)

    # Check if div is found
    if div:
        # Extract 'pfirst' text
        pfirst_text = div.find('p', class_='pfirst')
        pfirst = pfirst_text.get_text(strip=True) if pfirst_text and pfirst_text.get_text().isupper() else ""

        # Remove 'pfirst' element from the div
        if pfirst_text:
            pfirst_text.decompose()

        # Get the remaining text, handling backslashes
        remaining_text = re.sub(r'\\', '', div.get_text(separator='\n', strip=True))

        # Find all image elements within the div
        images = div.find_all('img')
        image_src_list = [image['src'] for image in images] if images else []

        # Find the blockquote within the div
        blockquote = div.find('blockquote')

        # Extract text from blockquote
        blockquote_text = blockquote.get_text(separator='\n', strip=True) if blockquote else ""

        # Initialize caption variables
        caption_text = None

        # Check if there are images in the div
        if images:
            # Find the caption div within the div
            caption_div = div.find('div', class_='caption italics')

            # Extract text from the caption div or use an empty string if not found
            caption_text = caption_div.get_text(strip=True) if caption_div else ""

            # If caption is not found in the current div, check for the overall div
            if not caption_text:
                overall_caption_div = div.find_previous('div', class_='caption italics')
                caption_text = overall_caption_div.get_text(strip=True) if overall_caption_div else ""

        # Add data to the list
        data.append({
            'ID': id_value.replace("-", " ").title(),
            'Pfirst': pfirst,
            'Remaining Text': remaining_text,
            'Blockquote Text': blockquote_text,
            'Photographs': image_src_list,
            'Photograph_Location': caption_text
        })

# Create a DataFrame
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
output_csv_path = 'C:\\Users\Lucas\PycharmProjects\pythonProject6\Alabama_Raw.csv'  # Replace with the desired output path
df.to_csv(output_csv_path, index=False)

print(f"CSV file saved to {output_csv_path}")