# import cohere co = cohere.Client('RRNSG7Umz9eHzpvppJJu3TZW9wVuW2AljKOsJQ9M')
import requests
from bs4 import BeautifulSoup
import json
import helpers


def get_html(url):
    response = requests.get(url)
    return response.content


def get_author_messy(meta_tags):
    author = None
    for tag in meta_tags:
        if 'name' in tag.attrs and tag.attrs['name'].lower() == 'author':
            author = tag.attrs['content']
            break

    return author


def get_publication_date_messy(meta_tags):
    pub_date = None
    for tag in meta_tags:
        if 'name' in tag.attrs and tag.attrs['name'].lower() in ['pubdate', 'date', 'dcterms.created']:
            pub_date = tag.attrs['content']
            break

    return pub_date


def get_metadata_schema_org(soup):
    structured_data = soup.find('script', type='application/ld+json')
    author = None
    publication_date = None
    title = None
    website_name = None
    if structured_data:
        data = json.loads(structured_data.string)
        author = data.get('author', {})
        if author:
            author = author['name']
        publication_date = data.get('datePublished')
        title = data.get('headline')
        publisher_info = data.get('publisher')
        if publisher_info:
            website_name = publisher_info.get('name')

    return {'author': author, 'publication_date': publication_date, 'title': title, 'website_name': website_name}


def get_metadata(url):
    html_content = get_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    # meta_tags = soup.find_all('meta')

    data = get_metadata_schema_org(soup)
    data['url'] = url

    if helpers.is_iso_string(data['publication_date']):
        data['publication_date'] = helpers.iso_to_dmy(data['publication_date'])

    # author = get_author_messy(meta_tags)
    # publication_date = get_publication_date_messy(meta_tags)

    return data
