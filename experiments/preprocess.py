import pycountry
import re

stopwords = ['Co.', 'Ltd.', 'Ltd', 'Private', 'International', 'Pacific', 'Pvt.',
             'Corp.',
             'Inc.', 'Sdn Bhd', 'Ltda',
             'S.A.C.', 'Inc.', 'A.S.',
             'Imp. & Exp.', 'Exp.', 'S.A.', 'S A.', 'S.A', 'Lp',
             '/Gmbh', 'Gmbh'
             'Sa De Cv', 'S.A. de C.V.'
             'Imp.', 'C.A.',
             'Llc', 'CO.', 'LTD.', 'PVT.', 'Asia']
stopwords = [st.replace('.', '\.') for st in stopwords]

countries = [cnt.name for cnt in pycountry.countries if cnt.name not in ['Colombia']]


def preproc(txt, stopwords):
    # remove stopwords
    # txt = txt.lower()
    for stopw in stopwords:
        txt = re.sub(stopw, ' ', txt)
    for cnt in countries:
        txt = re.sub(cnt, ' ', txt)

    txt = txt.replace(',', ' ')
    txt = txt.replace("'", ' ')
    txt = txt.replace(";", ' ')
    txt = txt.replace(":", ' ')
    txt = txt.replace('"', ' ')
    # remove geo info
    txt = re.sub('\(.+?\)', ' ', txt)
    # remove codes
    txt = re.sub('\w\d{1,}', ' ', txt)
    txt = txt.replace("(", ' ')
    txt = txt.replace(")", ' ')
    # replace consequent spaces
    txt = re.sub(' +', ' ', txt)
    txt = txt.strip()
    return txt

