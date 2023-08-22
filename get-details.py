import re
import requests
from bs4 import BeautifulSoup

def extract_website_info(url):
    # Fetching the HTML content of the website
    response = requests.get(url)
    html_content = response.content

    # Parsing HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Finding social links (Facebook, Twitter, LinkedIn)
    social_links = []
    social_patterns = [
        r'(?:https?:\/\/)?(?:www\.)?facebook\.com\/\S*',
        r'(?:https?:\/\/)?(?:www\.)?twitter\.com\/\S*',
        r'(?:https?:\/\/)?(?:www\.)?linkedin\.com\/\S*'
    ]
    for pattern in social_patterns:
        links = soup.find_all('a', href=re.compile(pattern, re.IGNORECASE))
        social_links.extend([link['href'] for link in links])

    # Finding email addresses from "mailto" links
    email_addresses = []
    mailto_links = soup.find_all(href=re.compile(r'^mailto:', re.IGNORECASE))
    for mailto_link in mailto_links:
        email_match = re.search(r'(?<=mailto:)[\w.-]+@[\w.-]+', mailto_link['href'])
        if email_match:
            email_addresses.append(email_match.group())

    # Finding phone numbers 
    phone_numbers = re.findall(r'\b\d{10,12}\b', str(soup))

    return social_links, email_addresses, phone_numbers

# Taking input
website_url = input("Enter a website URL: ")

social_links, email_addresses, phone_numbers = extract_website_info(website_url)

print("Social Links:")
for link in social_links:
    print(link)

print("\nEmail Addresses:")
for email in email_addresses:
    print(email)

print("\nPhone Numbers:")
for number in phone_numbers:
    print(number)

# The code for extracting phone number doesnot work with some websites

