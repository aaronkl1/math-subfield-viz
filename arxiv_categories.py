import urllib, urllib.request, re
import pandas as pd
import numpy as np

def catCount(cat1, cat2) -> int:
    url = 'http://export.arxiv.org/api/query?search_query=cat:math.'+ cat1 + '+AND+cat:math.' + cat2
    data = urllib.request.urlopen(url)
    regex = r'<opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1\.1/">(\d+)</opensearch:totalResults>'
    text = data.read().decode('utf-8')
    # Example usage
    match = re.search(regex, text)
    if match:
        number = match.group(1)
        # Must convert to type int, number variable above is of type string
        return int(number)
    # Function expects return value of type int
    return 0


minicat = ['ac','ag','ap','at']
categories = ['ac','ag','ap','at','ca','co','ct','cv','dg','ds','fa','gm','gn','gr','gt','ho','it','kt','lo','mg','mp','na','nt','oa','oc','pr','qa','ra','rt','sg','sp','st']
cat_names = ["Commutative Algebra", "Algebraic Geometry", "Analysis of PDEs", "Algebraic Topology", "Classical Analysis and ODEs", "Combinatorics", "Category Theory", "Complex Variables", "Differential Geometry", "Dynamical Systems", "Functional Analysis", "General Mathematics", "General Topology", "Group Theory", "Geometric Topology", "History and Overview", "Information Theory", "K-Theory and Homology", "Logic", "Metric Geometry", "Mathematical Physics", "Numerical Analysis", "Number Theory", "Operator Algebras", "Optimization and Control", "Probability", "Quantum Algebra", "Rings and Algebras", "Representation Theory", "Symplectic Geometry", "Spectral Theory", "Statistics Theory"]


def makeTable(cat):
    n = len(cat)
    table = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            table[i][j] = catCount(cat[i], cat[j])
            table[j][i] = table[i][j]
    return table

def export(cat, names, title):
    arr = np.asarray(makeTable(cat))
    filename = '/Users/AaronLi/MISC/Projects/' + title + '.csv'
    pd.DataFrame(data = arr, index = names).to_csv(filename, header  = names) 

export(categories, cat_names, 'categories_new')
