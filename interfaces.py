from newspaper import Article
from newspaper import Config


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent


def parse_article(url):
    article = Article(url=url, config=config)
    article.download()
    article.parse()
    return article


""" 
[Author]. [Title of Source]. [Title of Container], [Other Contributors], [Version], [Number], [Publisher], [Publication Date], [Location]. [Access Date].
"""


def format_mla9(url):
    article = parse_article(url)

    def format_author(_authors):
        if len(_authors) == 1:
            return f"{author_lastname_firstname(_authors[0], ', ')}. "
        elif len(_authors) == 2:
            return f"{author_lastname_firstname(_authors[0], ', ')}, and {_authors[1]}. "
        elif len(_authors) > 2:
            return f"{author_lastname_firstname(_authors[0], ', ')}, et al. "
        else:
            return ""


    final_authors = format_author(article.authors)
    final = f"{final_authors}"
    return final


def author_lastname_firstname(author, sep):
    author_split = author.split()
    return f"{author_split[-1]}{sep if len(author_split) > 1 else ''}{sep.join(author_split[:-1])}"
