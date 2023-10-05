import whois

dominio = "netflix.com" #recebe o dominio 
resultado = whois.whois(dominio) #consultando o whois do dominio e armazena o resultado da consulta

if resultado.domain_name is None: #se o resultado de resultado.domain_name for igual a None, é porque o dominio nao foi encontrado

    print('Dominio nao encontrado')
else: 
    print(resultado)

