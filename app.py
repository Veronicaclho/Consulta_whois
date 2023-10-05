import whois

dominio = "netflix.com"  
resultado = whois.whois(dominio) 

if resultado.domain_name is None: 

    print('Dominio nao encontrado')
else: 
    print(resultado)

