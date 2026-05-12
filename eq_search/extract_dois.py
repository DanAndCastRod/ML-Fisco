import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import bibtexparser, os, re

bib_dir = r'C:\proyectos_personales\ML-Fisco\eq_search'
files = ['Scopus_B2.bib','Scopus_B3.bib','Scopus_B4.bib','principal.bib','Scopus_A.bib','Scopus_B1.bib']

all_entries = []
for f in files:
    fp = os.path.join(bib_dir, f)
    if not os.path.exists(fp):
        continue
    with open(fp, encoding='utf-8', errors='replace') as fh:
        try:
            db = bibtexparser.load(fh)
            for e in db.entries:
                e['_source_file'] = f
                all_entries.append(e)
        except Exception as ex:
            pass

# Deduplicate
def norm(t):
    return re.sub(r'[^a-z0-9]', '', t.lower()) if t else ''

seen = {}
unique = []
for e in all_entries:
    key = norm(e.get('title', ''))
    if key and key not in seen:
        seen[key] = e
        unique.append(e)

# Search terms for priority entries - using partial title matches
priority_searches = {
    "ALTA": [
        ("Coglianese & Lehr (2017)", "regulating by robot"),
        ("Towards XAI in Tax Law (2022)", "towards explainable artificial intelligence xai in tax law"),
        ("AI, Rule of Law, Taxation (2024)", "artificial intelligence the rule of law and public administration the case of taxation"),
        ("AI Governance and Taxpayers' Rights (2025)", "ai governance and taxpayers rights in a digital age"),
        ("Balancing innovation and integrity (2025)", "balancing innovation and integrity ai in tax administration"),
        ("Fighting Tax Fraud through AI (2020)", "fighting tax fraud through artificial intelligence"),
        ("Requirements for Tax XAI (2022)", "requirements for tax xai under constitutional"),
        ("Tax compliance and privacy rights (2019)", "tax compliance and privacy rights in profiling"),
    ],
    "MEDIA": [
        ("Behind the One-Way Mirror (2022)", "behind the one way mirror"),
        ("Exploring explainable AI in tax (2025)", "exploring explainable ai in the tax domain"),
        ("Ethics in AI Use for Tax Admin (2025)", "ethics in ai use for tax administration"),
        ("Use of AI by Tax Authorities (2025)", "the use of artificial intelligence by tax authorities for tax auditing"),
        ("AI and Tax Administration (2021)", "artificial intelligence and tax administration strategy applications"),
        ("IA, Sesgos y No Discriminación (2022)", "inteligencia artificial sesgos y no discrimin"),
        ("Regulation algorithms Colombian (2024)", "regulation of algorithms and ai systems for judicial decision making"),
        ("Explainable AI for government (2024)", "explainable ai for government does the type of explanation"),
    ],
    "BAJA": [
        ("Zerilli et al. (2019)", "transparency in algorithmic and human decision making"),
        ("XAI Supporting Public Admin Tax Audit (2021)", "explainable artificial intelligence xai supporting public administration"),
        ("Proactive detection tax fraud XAI (2025)", "proactive detection of tax fraud using explainable"),
        ("Automated decision-making public admin (2021)", "automated decision making in public administration"),
    ]
}

for priority, searches in priority_searches.items():
    print(f"\n{'='*70}")
    print(f"  PRIORIDAD {priority}")
    print(f"{'='*70}")
    for label, search_term in searches:
        search_norm = norm(search_term)
        found = False
        for e in unique:
            title_norm = norm(e.get('title', ''))
            if search_norm in title_norm:
                doi = e.get('doi', '').strip()
                title = e.get('title', 'N/A')[:120]
                year = e.get('year', 'N/A')
                author = e.get('author', 'N/A')
                # Get first author surname
                first_author = author.split(',')[0].strip() if author != 'N/A' else 'N/A'
                journal = e.get('journal', e.get('booktitle', 'N/A'))[:80]
                url = e.get('url', '').strip()
                
                print(f"\n  {label}")
                print(f"  Título: {title}")
                print(f"  Autor(es): {first_author} et al." if ',' in author or ' and ' in author.lower() else f"  Autor: {first_author}")
                print(f"  Año: {year}")
                print(f"  Fuente: {journal}")
                if doi:
                    print(f"  DOI: {doi}")
                    print(f"  URL: https://doi.org/{doi}")
                else:
                    print(f"  DOI: ❌ No disponible en el registro BibTeX")
                    if url:
                        print(f"  URL alternativa: {url}")
                    else:
                        print(f"  URL: No disponible")
                found = True
                break
        if not found:
            print(f"\n  {label}")
            print(f"  ⚠️ NO ENCONTRADO en la bibliografía descargada")
