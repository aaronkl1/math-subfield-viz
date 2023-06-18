"""
read_json.py

Requirements
------------
Please download the arXiv dataset here: https://www.kaggle.com/datasets/Cornell-University/arxiv
Once downloaded, unzip the file and move into same directory as this script

Returns
-------
This script will prune all arXiv articles from the downloaded dataset and
will generate a JSON file only containing the mathematical articles
"""

import json
from os.path import exists

# This will store a list of dictionaries
# each dictionary will be an article
# The article dictionary will have the following keys:
#   id: article identifier
#   submitter: author who submitted the article to arXiv
#   authors: authors of the article (comma separated)
#   title: title of the article
#   comments: comments/pdf information
#   journal-ref: the journal in which article is published
#   doi: identifier for the published article
#   report-no: identifier string of the report
#   categories: arXiv categories which best describes the topic of the article
#   license: license of the article
#   abstract: abstract of the article
#   versions: submitted versions of the article
#   update_date: when the article was last updated
#   authors_parsed: name of authors as list, i.e. [last name, first initial]
articles = []

# Don't regenerate math data if the file already exists
if exists('arxiv-metadata-math.json'):
    with open('arxiv-metadata-math.json') as file:
         articles = json.load(file)

    # ToDo: now that we have pruned the data we must get it in the desired
    # format for d3.js.

# prune down the arxiv data to generate math only articles
else:
    with open('arxiv-metadata-oai-snapshot.json') as file:
        for line in file:
            article = json.loads(line)
            if 'math' in article['categories'].lower():
                articles.append(article)

    with open('arxiv-metadata-math.json', 'w') as outfile:
        json.dump(articles, outfile)
