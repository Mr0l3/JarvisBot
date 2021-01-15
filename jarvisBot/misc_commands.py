#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from commands import send_message
from bs4 import BeautifulSoup


def replace_tags(string: str, tags: tuple, replace_with: str) -> str:
    for tag in tags:
        string = string.replace(tag, replace_with)

    return string


def c_lyrics(update, context) -> None:
    # /lyrics [query]
    search_term = ' '.join(context.args).strip()

    if len(search_term) > 1:
        search_result = search_lyrics_url(search_term)
        lyrics_url = search_result[0].strip()

        song_title = search_result[1].strip().replace(' - LETRAS.MUS.BR', '')
        song_title = replace_tags(song_title, ('<b>', '</b>', '<b/>'), '')
        song_title = f'<b>{song_title}</b>\n\n'

        if lyrics_url:
            r = requests.get(lyrics_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            lyrics_div = soup.find('div', class_='cnt-letra p402_premium')

            lyrics = ''
            for verse_raw in lyrics_div:

                # Remove tags
                verse_raw = str(verse_raw)
                if(verse_raw[0] == ' '):
                    verse_raw = verse_raw[1:]

                verse_raw = verse_raw.replace('<p>', '')
                verse_raw = verse_raw.replace('</p>', '\n\n')
                verse_raw = replace_tags(verse_raw, ('<br>', '<br/>', '</br>'), '\n')
                verse_raw = verse_raw.replace('-', '\-')

                # Remove extra line breaks
                verse_raw = verse_raw.replace('\n\n\n', '\n\n')
                lyrics += verse_raw

            msg = song_title + lyrics

        else:
            msg = 'Couldn\'t find the requested lyrics'
    else:
        msg = 'Usage: /lyrics search-term\nExample: /lyrics orgia de traveco'

    send_message(update, context, msg, parse_HTML=True)


def search_lyrics_url(search_term: str) -> list:
    url = f'https://cse.google.com/cse/element/v1?rsz=4&num=4&hl=pt-PT&source=gcsc&gss=.br&cselibv=921554e23151c152&cx=partner-pub-9911820215479768:4038644078&q={search_term}&safe=off&cse_tok=AJvRUv0hKGJlVIZpenOLGpkcyxU7:1610670352756&exp=csqr,cc&callback=a'
    r = requests.get(url)

    if r.status_code == 200:
        # Convert the message to a json, then decode it
        results = json.loads(r.text[10:len(r.text) - 2])['results']
        for result in results:
            # Search for lyrics that aren't translated to portuguese
            if '(TRADUÇÃO)' in result['title']:
                continue
            else:
                return [result['url'], result['title']]
    else:
        return []
