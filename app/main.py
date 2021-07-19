import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(link, headers):
    url = "https://api-ssl.bitly.com/v4/shorten"
    payloads = {"long_url": link}
    response = requests.post(url, json=payloads, headers=headers)
    response.raise_for_status()
    abbreviated_link = response.json()
    return abbreviated_link["link"]


def count_clicks(link, headers):
    payloads = {"units": -1}
    split_link = urlparse(link)
    complete_url = f'https://api-ssl.bitly.com/v4/bitlinks/{"".join(split_link._replace(scheme=""))}/clicks/summary'
    response = requests.get(complete_url, params=payloads, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()
    return clicks_count["total_clicks"]


def has_abbreviated_link(link, headers):
    split_link = urlparse(link)
    complete_url = f'https://api-ssl.bitly.com/v4/bitlinks/{"".join(split_link._replace(scheme=""))}'
    response = requests.get(complete_url, headers=headers)
    return response.ok


if __name__ == "__main__":
    project_folder = os.path.expanduser(
        "~/Desktop/Projects/bitlinks_consider_clicks/app"
    )
    load_dotenv(os.path.join(project_folder, ".env"))
    token = {"Authorization": os.getenv("BITLY_API_KEY")}
    parser = argparse.ArgumentParser(
        description="Сокращает ссылки и показывает количество кликов по сокращенной ссылке"
    )
    parser.add_argument("link", help="Ваша ссылка")
    args = parser.parse_args()

    try:
        if has_abbreviated_link(args.link, token):
            print(f"Количество кликов по ссылке: {count_clicks(args.link, token)}")
        else:
            print(shorten_link(args.link, token))
    except requests.exceptions.HTTPError:
        print("Вы ввели некорректную ссылку!")
