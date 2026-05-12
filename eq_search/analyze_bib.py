import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import bibtexparser, os, json, re
from collections import Counter

bib_dir = r'C:\proyectos_personales\ML-Fisco\eq_search'
files = ['Scopus_B2.bib','Scopus_B3.bib','Scopus_B4.bib','principal.bib','Scopus_A.bib','Scopus_B1.bib']

all_entries = []
file_counts = {}

for f in files:
    fp = os.path.join(bib_dir, f)
    if not os.path.exists(fp):
        continue
    with open(fp, encoding='utf-8', errors='replace') as fh:
        try:
            db = bibtexparser.load(fh)
            file_counts[f] = len(db.entries)
            for e in db.entries:
                e['_source_file'] = f
                all_entries.append(e)
        except Exception as ex:
            print(f'Error {f}: {ex}')

print(f'Total entries: {len(all_entries)}')
for f, c in file_counts.items():
    print(f'  {f}: {c} entries')

# Deduplicate by title (normalized)
def norm(t):
    return re.sub(r'[^a-z0-9]', '', t.lower()) if t else ''

seen = {}
unique = []
dupes = 0
for e in all_entries:
    key = norm(e.get('title', ''))
    if key and key in seen:
        dupes += 1
    else:
        seen[key] = e
        unique.append(e)

print(f'Unique entries: {len(unique)}, Duplicates removed: {dupes}')
print()

# Route A classification
# 3 pillars: (1) Tax admin/fiscal, (2) ML/AI, (3) Due process/transparency/explainability
tax_kw = ['tax', 'fiscal', 'tributar', 'impuesto', 'evasion', 'evasión', 'compliance', 'audit',
           'dian', 'revenue', 'irs', 'hmrc', 'sat ', 'sii', 'receita']
ml_kw = ['machine learning', 'artificial intelligence', 'deep learning', 'neural network',
          'predictive', 'random forest', 'xgboost', 'classification', 'supervised',
          'unsupervised', 'data mining', 'algorithm', 'analytics', 'big data',
          'natural language', 'nlp', 'automated', 'automation']
dp_kw = ['due process', 'debido proceso', 'transparency', 'transparencia', 'explainab',
          'explicab', 'black box', 'caja negra', 'fairness', 'equidad', 'accountability',
          'bias', 'sesgo', 'right', 'derecho', 'constitutional', 'constitucional',
          'administrative law', 'derecho administrativo', 'gdpr', 'ai act', 'governance',
          'gobernanza', 'ethic', 'ética', 'procedural', 'procedimental', 'regulation',
          'regulación', 'motivación', 'motivation', 'interpretab']


def classify(entry):
    text = ' '.join([
        entry.get('title', ''),
        entry.get('abstract', ''),
        entry.get('keywords', ''),
        entry.get('author_keywords', '')
    ]).lower()
    has_tax = any(k in text for k in tax_kw)
    has_ml = any(k in text for k in ml_kw)
    has_dp = any(k in text for k in dp_kw)
    return has_tax, has_ml, has_dp


# Classify all
triple = []
double_tax_ml = []
double_tax_dp = []
double_ml_dp = []
single = []

for e in unique:
    t, m, d = classify(e)
    pillars = sum([t, m, d])
    if pillars == 3:
        triple.append(e)
    elif t and m:
        double_tax_ml.append(e)
    elif t and d:
        double_tax_dp.append(e)
    elif m and d:
        double_ml_dp.append(e)
    elif pillars >= 1:
        single.append(e)

print('=== CLASSIFICATION FOR ROUTE A ===')
print(f'3 pillars (Tax+ML+DueProcess): {len(triple)} entries')
print(f'Tax + ML (no due process): {len(double_tax_ml)} entries')
print(f'Tax + DueProcess (no ML): {len(double_tax_dp)} entries')
print(f'ML + DueProcess (no tax): {len(double_ml_dp)} entries')
print(f'Single pillar only: {len(single)} entries')
print()


def print_entry(i, e):
    yr = e.get('year', 'N/A')
    src = e.get('journal', e.get('booktitle', 'N/A'))[:60]
    title = e.get('title', 'N/A')[:140]
    sf = e['_source_file']
    print(f'{i}. [{yr}] {title}')
    print(f'   Source: {src} | File: {sf}')
    print()


print('=== TOP ENTRIES: ALL 3 PILLARS (Tax + ML + Due Process) ===')
for i, e in enumerate(triple, 1):
    print_entry(i, e)

print()
print('=== TAX + ML entries (top 30) ===')
for i, e in enumerate(double_tax_ml[:30], 1):
    print_entry(i, e)

print()
print('=== ML + DUE PROCESS entries (top 30) ===')
for i, e in enumerate(double_ml_dp[:30], 1):
    print_entry(i, e)

print()
print('=== TAX + DUE PROCESS entries (top 20) ===')
for i, e in enumerate(double_tax_dp[:20], 1):
    print_entry(i, e)

# Check specific authors mentioned in Recomendaciones
print()
print('=== CHECKING SPECIFIC AUTHORS FROM RECOMENDACIONES ===')
target_authors = ['Pasquale', 'Citron', 'Coglianese', 'Lehr', 'Zerilli', 'Hemberg', 'Rahimikia', 'Vellutini']
for author in target_authors:
    found = [e for e in unique if author.lower() in e.get('author', '').lower()]
    if found:
        for e in found:
            title = e.get('title', 'N/A')[:100]
            yr = e.get('year', 'N/A')
            sf = e['_source_file']
            print(f'  FOUND: {author} -> [{yr}] {title} (in {sf})')
    else:
        print(f'  NOT FOUND: {author}')

# Year distribution for relevant entries
print()
print('=== YEAR DISTRIBUTION (triple + double) ===')
relevant = triple + double_tax_ml + double_tax_dp + double_ml_dp
years = Counter(e.get('year', 'N/A') for e in relevant)
for yr in sorted(years.keys(), reverse=True)[:15]:
    print(f'  {yr}: {years[yr]} entries')
