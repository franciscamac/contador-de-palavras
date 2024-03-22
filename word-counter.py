import re
import urllib.request
import back
import concurrent.futures

def process_url(url):
    response = urllib.request.urlopen(url) #abrindo a url
    html = response.read().decode('UTF-8') #decodificando para texto usando UTF-8
    text = back.removerHtml(html).lower() #Removendo tags HTML e colocando o texto para minúsculo
    wordlist = back.dividindoTexto(text) #Divide o texto em uma sequência não alfa-numérica
    wordlist = [word for word in wordlist if not word.isdigit()]  #Itera sobre cada palavra na lista "wordlist" e verifica se ela consiste apenas de dígitos usando o método 'isdigit()'
    wordlist = back.removerPalavraComum(wordlist, back.stopwords) #Remove palavras comuns e irrelevantes
    dictionary = back.dicionarioPalavras(wordlist) #Cria um dicionário de frequência das palavras
    sorteddict = back.ordemDecrescente(dictionary) #Faz a ordenação das palavras em ordem decrescente
    
    return sorteddict

def main():
    urls = []
    while True:
        url = input("Insira a URL (ou digite 'sair' para encerrar): ")
        if url.lower() == 'sair':
            break
        urls.append(url)

    if not urls:
        print("Nenhuma URL fornecida. Encerrando o programa.")
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Processa as URLs concorrentemente
        results = list(executor.map(process_url, urls))

    # Combina os resultados (se necessário)
    combined_result = []
    for result in results:
        combined_result.extend(result)

    # Imprime os resultados combinados
    for s in combined_result:
        print(str(s))

if __name__ == "__main__":
    main()
