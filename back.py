from collections import Counter

stopwords = [
    "de", "a", "s", "n", "o", "que", "e", "do", "da", "em", "um", "para", "é", "com", "não", "uma",
    "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele",
    "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos", "já",
    "está", "eu", "também", "só", "pelo", "pela", "até", "isso", "ela", "entre", "era",
    "depois", "sem", "mesmo", "aos", "ter", "seus", "quem", "nas", "me", "esse", "eles",
    "estão", "você", "tinha", "foram", "essa", "num", "nem", "suas", "meu", "às", "minha",
    "têm", "numa", "pelos", "elas", "havia", "seja", "qual", "será", "nós", "tenho", "lhe",
    "deles", "essas", "esses", "pelas", "este", "fosse", "dele", "tu", "te", "vocês", "vos",
    "lhes", "meus", "minhas", "teu", "tua", "teus", "tuas", "nosso", "nossa", "nossos", "nossas",
    "dela", "delas", "esta", "estes", "estas", "aquele", "aquela", "aqueles", "aquelas", "isto",
    "aquilo", "estou", "está", "estamos", "estão", "estive", "esteve", "estivemos", "estiveram",
    "estava", "estávamos", "estavam", "estivera", "estivéramos", "esteja", "estejamos", "estejam",
    "estivesse", "estivéssemos", "estivessem", "estiver", "estivermos", "estiverem", "hei", "há",
    "havemos", "hão", "houve", "houvemos", "houveram", "houvera", "houvéramos", "haja", "hajamos",
    "hajam", "houvesse", "houvéssemos", "houvessem", "houver", "houvermos", "houverem", "houverei",
    "houverá", "houveremos", "houverão", "houveria", "houveríamos", "houveriam", "sou", "somos",
    "são", "era", "éramos", "eram", "fui", "foi", "fomos", "foram", "fora", "fôramos", "seja",
    "sejamos", "sejam", "fosse", "fôssemos", "fossem", "for", "formos", "forem", "serei", "será",
    "seremos", "serão", "seria", "seríamos", "seriam", "tenho", "tem", "temos", "tém", "tinha",
    "tínhamos", "tinham", "tive", "teve", "tivemos", "tiveram", "tivera", "tivéramos", "tenha",
    "tenhamos", "tenham", "tivesse", "tivéssemos", "tivessem", "tiver", "tivermos", "tiverem",
    "terei", "terá", "teremos", "terão", "teria", "teríamos", "teriam"
]

def removerHtml(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0 #indicador de estado (0 = fora e 1 = dentro)
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text



def dividindoTexto(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Dada uma lista de palavras, retorna um dicionário de pares palavra-frequência.

def dicionarioPalavras(wordlist):
    return dict(Counter(wordlist))

# Ordena um dicionário de pares palavra-frequência em ordem decrescente de frequência.

def ordemDecrescente(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def removerPalavraComum(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]