import re
import bs4
import requests
from urllib.parse import urlparse


# Convert to class ?
tags_list = ["html", "header", "body"]
tag_dict = {}


def is_valid_url(url_from_ui: str) -> bool:
    regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return True if regex.search(url_from_ui) else False


def is_url_getable(url_from_ui: str):
    """
    Try to get 200 HTTP code from the valid URL
    :param url_from_ui:
    :return:
    """
    if is_valid_url(url_from_ui):
        try:
            requests.get(url_from_ui)
        except requests.exceptions.ConnectionError as conerr:
            return conerr
    return True


def get_domain(original_url: str) -> str:
    """
    Parse original URL and return domain
    :param original_url:
    :return:
    """
    urlparse("scheme://netloc/path;parameters?query#fragment")
    parsed_url = urlparse(original_url)

    domain = parsed_url.hostname.split('.')[1]

    return domain


def pull_web_page(url: str, tag_from_list: str) -> list:
    """
    Pull and return the web page tags and content
    :param tag_from_list:
    :param url:
    :return:
    """
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all(tag_from_list)

    q_l = list(quotes)
    return q_l


def dict_create(url_from_ui: str) -> dict:
    """
    Create dict from data from internet
    :param url_from_ui:
    :return:
    """
    # count_t = 0
    for t_f_l in tags_list:
        count_t = len(pull_web_page(url_from_ui, t_f_l))

        tag_dict.update({t_f_l: count_t})
        tag_dict[t_f_l] = count_t

    return tag_dict


# print(dict_create("google.com"))

if __name__ == '__main__':
    pass
