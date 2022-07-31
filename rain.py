#!/usr/bin/env python3
from configs import API_URL, REPO_ADDR, REPO_NAME
import requests
import re
import os
import subprocess


def basher(**kwargs) -> None:
    """ set the the environment variable with passed arg.name to arg.value and then run the main.sh

    :param kwargs: key pair of environment variables
    :return: None
    """

    for i in kwargs:
        os.environ.setdefault(i, kwargs[i])

    subprocess.run('./main.sh')


def getIssueContext(response: dict) -> dict:
    """
    this function will get a dict which contain an issue and then return a context of its body, title and attachment_link.

    :param response:
    :return: dict
    """

    x = dict(title=None, body=None, attachment_link=None)

    x['title'] = response.get('title')
    x['body'] = response.get('body')

    if x['body']:
        if(match := re.findall('(https.*md)', x['body'])):
            x['attachment_link'] = match[0]

    return x


def downloadAttachment(url: str, name: str, dest: str) -> bool:
    """ download the attachment url ans save it under /tmp/{name}

    :param url: attachment url
    :param name: name to save file as
    :return: true if download and save file, false otherwise
    """

    data = requests.get(url)
    while data.status_code != 200:
        downloadAttachment(url)

    with open(f'./content/{dest}/{name}.md', 'wb') as fli:
        fli.write(data.content)
        return True

    return False


res = requests.get(API_URL)
while res.status_code != 200:
    res = requests.get(API_URL)


for issue in res.json():
    if issue.get('state') == 'open':
        if(labels := issue.get('labels')):
            for label in labels:
                if label.get('name') in ['tools', 'fundamentals']:
                    x = getIssueContext(issue)
                    if downloadAttachment(x.get('attachment_link'), x.get('title'), dest=label.get('name')):
                        print('found and downloaded')
