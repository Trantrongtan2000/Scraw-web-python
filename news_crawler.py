import re

import validators
from newspaper import Article


def is_url(url):
    return validators.url(url)


def crawl(url):
    if not is_url(url):
        result = {
            'url': url,
            'error': 'Url không hợp lệ!',
            'success': False
        }

        return result
    article = Article(url)
    article.download()
    article.parse()
    result = {'title': article.title,'content': re.sub('\\n+', '</p><p>', '<p>' + article.text + '</p>')}
    return result


if __name__ == '__main__':
    res = crawl(
        'http://spiderum.com/bai-dang/Cach-de-dat-mui-cong-dong-game-nhu-dat-mui-bo-ph9')
    print(res)
    print(type(res))
