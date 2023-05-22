import urllib, urllib.request, re
import pandas as pd
import numpy as np

def catCount(cat1, cat2) ->  int:
    url = 'http://export.arxiv.org/api/query?search_query=cat:math.'+ cat1 + '+AND+cat:math.' + cat2
    data = urllib.request.urlopen(url)
    regex = r'<opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1\.1/">(\d+)</opensearch:totalResults>'
    text = data.read().decode('utf-8')
    # Example usage
    match = re.search(regex, text)
    if match:
        number = match.group(1)
        return number


minicat = ['ac','ag','ap','at']
categories = ['ac','ag','ap','at','ca','co','ct','cv','dg','ds','fa','gm','gn','gr','gt','ho','it','kt','lo','mg','mp','na','nt','oa','oc','pr','qa','ra','rt','sg','sp','st']

def makeTable(cat):
    n = len(cat)
    table = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            table[i][j] = catCount(cat[i], cat[j])
            table[j][i] = table[i][j]
    return table

def export(cat, title):
    arr = np.asarray(makeTable(cat))
    filename = '/Users/AaronLi/MISC/Projects/' + title + '.csv'
    pd.DataFrame(data = arr, index = cat).to_csv(filename, header  = cat) 

export(categories, 'categories_new')