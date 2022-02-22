import bs4
import requests


# Convert to class ?
tags_list = ["html", "header", "body"]
tag_dict = {}


def pull_web_page(url: str, tag_from_list: str) -> list:
    """
    Pull and return the web page tags and content
    :param tag_from_list:
    :param url:
    :return:
    """
    response = requests.get("http://www."+url)
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
