thonimport requests
from bs4 import BeautifulSoup
import json
import csv
import os

def scrape_instagram_data(usernames):
    data = []
    for username in usernames:
        url = f"https://www.instagram.com/{username}/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            script = soup.find('script', text=lambda t: t and 'window._sharedData' in t).string
            json_data = script.split('=')[-1].strip().rstrip(';')
            data_json = json.loads(json_data)

            user_data = data_json['entry_data']['ProfilePage'][0]['graphql']['user']
            user_info = {
                "username": username,
                "followers_count": user_data['edge_followed_by']['count'],
                "following_count": user_data['edge_follow']['count'],
                "profile_url": f"https://www.instagram.com/{username}/",
                "bio": user_data['biography'],
                "posts_count": user_data['edge_owner_to_timeline_media']['count']
            }
            data.append(user_info)
        else:
            print(f"Failed to retrieve data for {username}")
    return data

def save_to_json(data, filename='output.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename='output.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def save_to_xml(data, filename='output.xml'):
    import dicttoxml
    xml_data = dicttoxml.dicttoxml(data)
    with open(filename, 'wb') as xml_file:
        xml_file.write(xml_data)

if __name__ == "__main__":
    usernames = ['example_user1', 'example_user2']
    scraped_data = scrape_instagram_data(usernames)
    
    save_to_json(scraped_data)
    save_to_csv(scraped_data)
    save_to_xml(scraped_data)