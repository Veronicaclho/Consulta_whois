import whois
from tabulate import tabulate

def consulta():
    domains = []
    
    with open('dominios.txt', 'r') as file:
        domains = [line.strip() for line in file.readlines()]

    results = []
    for domain in domains:
        try:
            whois_info = whois.whois(domain)
            if isinstance(whois_info, dict):
                registrar = whois_info.get('registrar', 'N/A')
                creation_date = whois_info.get('creation_date', 'N/A')
                expiration_date = whois_info.get('expiration_date', 'N/A')
                results.append([domain, registrar, creation_date, expiration_date])
        except Exception as e:
            print(f"Erro ao obter informações WHOIS para {domain}: {str(e)}")

     
    headers = ['Domínio', 'Registrador', 'Data de Criação', 'Data de Expiração']

    
    tabela = tabulate(results, headers, tablefmt='plain')

    
    print(tabela)

if __name__ == "__main__":
    consulta()
