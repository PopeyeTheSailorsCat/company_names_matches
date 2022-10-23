import pycountry
import re
from transliterate import translit
# from langdetect import detect
# from ftlangdetect import detect


stopwords = ['Co.', 'Ltda', 'Ltd.', 'Ltd', 'Private', 'International', 'Pacific', 'Pvt.',
             'Corp.',
             'Inc.', 'Sdn Bhd', 'srl',
             'S.A.C.', 'Inc.', 'A.S.',
             'Imp. & Exp.', 'Exp.', 'S.A.', 'S A.', 'S.A', ' Lp',
             '/Gmbh', 'Gmbh', 'gmbh', 'gmbh', 'a/s.', 'a/s',
             'Sa De Cv', 'S.A. de C.V.', '\*\*\*',
             'Imp.', 'C.A.', 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ', 'ooo', 'ооо',
             'Llc', 'CO.', 'LTD.', 'PVT.', 'Asia', 'S.r.l', ' SPA', 'S.P.A.', 'S.P.A',
             'Industries', 'Industrial', 'Corporation', 'usa', 'Group of Companies', 'De Rl De Cv',
             'o.o.', ' z ', 'Sp.', 'E.E.T',
             'раша', 'руссия', 'русь', 'рус', 'снг', 'филиал компании', 'компани', 'срл', 'гмбх', 'раша',
             'лимитед',
             ]
stopwords = [st.replace('.', '\.') for st in stopwords]
countries = [cnt.name for cnt in pycountry.countries if cnt.name not in ['Colombia']]
end_stopwords = [' us', ' инк', ' лтд.', ' лтд', 'и к', ' sa', ' Lp']
start_stopwords = ['ЗАО', 'СП АО', 'АО', 'ОАО']
rus_alphabet = list('АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя')


def ru_detect(txt):
    if [i for i in txt if i in rus_alphabet]:
        return True
    else:
        return False


def preproc(txt, stopwords):
    txt = txt.replace('"', ' ')
    txt = txt.lower()

    # remove geo info
    txt = re.sub('\(.+?\)', ' ', txt)
    # remove codes
    txt = re.sub('\w\d{1,}', ' ', txt)

    # remove stopwords
    for stopw in stopwords:
        txt = re.sub(stopw.lower(), ' ', txt)
    for cnt in countries:
        txt = re.sub(cnt.lower(), ' ', txt)

    # Delete stopwrods from end of string
    for estopw in end_stopwords:
        if txt.endswith(estopw):
            txt = txt[:-len(estopw)]
    # Delete stopwrods from start of string
    for sstopw in start_stopwords:
        if txt.startswith(sstopw):
            txt = txt[len(sstopw):]

    if ru_detect(txt):
        txt = txt.replace('ь', '')
        txt = txt.replace('ъ', '')
        txt = translit(txt, 'ru', reversed=True)

    txt = txt.replace('-', ' ')
    txt = txt.replace('Ş', 's')
    txt = txt.replace(',', ' ')
    txt = txt.replace("'", ' ')
    txt = txt.replace(";", ' ')
    txt = txt.replace(":", ' ')
    txt = txt.replace("(", ' ')
    txt = txt.replace(")", ' ')
    txt = txt.replace(".", '')
    # replace consequent spaces
    txt = re.sub(' +', ' ', txt)
    txt = txt.strip()
    return txt


if __name__ == '__main__':
    a = 'Canada' in countries
    print(a)


