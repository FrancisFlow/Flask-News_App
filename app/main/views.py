from flask import render_template, request, redirect, url_for
from ..requests import get_sources, get_article
from ..models import Source,Articles
from . import main

@main.route('/', methods = ['GET', 'POST'])
def index():
    """
    view root page function
    """

    #getting sources
    tech_sources = get_sources('technology')
    title = 'News Flow'
    return render_template('index.html', title = title, technology=tech_sources)


@main.route('/source/<id>', ['GET', 'POST'])
def articles(id):
    """
    function to return articles
    """
    articles = get_article(id)
    title = f'Headline {id}'
    return render_template('article.html', title = title, articles = articles)