import re

patterns = [
    (r"\b(estou|to|tô|eu estou)\b (com )?(sem internet|sem acesso|com problemas no login|com erro \d{3,4}|com a tela travando)", r"ENTENDO QUE VOCÊ ESTÁ \g<2>\g<3>. ISSO PODE SER FRUSTRANTE. VOCÊ JÁ TENTOU REINICIAR O SISTEMA?"),

    (r".*(internet|rede|wi[-]?fi).*lenta.*", r"A CONEXÃO ESTÁ LENTA? ISSO TEM ACONTECIDO FREQUENTEMENTE?"),

    (r".*\b(\d{1,2}/\d{1,2}/\d{4})\b.*", 
     r"VOCÊ MENCIONOU A DATA \1. FOI NESSE DIA QUE O PROBLEMA COMEÇOU?"),

    (r".*(não aguento mais|desisto|irritado|raiva|não funciona).*", 
     r"EU ENTENDO SUA FRUSTRAÇÃO. VAMOS TENTAR RESOLVER ISSO JUNTOS."),

    (r".*\berro (\d{3,4})\b.*", 
     r"O ERRO \1 PODE ESTAR RELACIONADO A PERMISSÕES OU ACESSO. QUANDO ELE APARECE?"),

    (r".*\b((trav|falh|bug|reinici|atuali[zs]|lent))\w*\b.*", 
     r"PARECE QUE O SISTEMA ESTÁ COM ALGUM PROBLEMA DE \1... PODE ME CONTAR MAIS?"),


    (r".*\b(sim|com certeza|exatamente|claro)\b.*", r"OK, OBRIGADO PELA CONFIRMAÇÃO. TEM MAIS ALGUMA INFORMAÇÃO RELEVANTE?"), 
    
    (r".*\b(não|nem um pouco|nada)\b.*", r"ENTENDO. VAMOS TENTAR UMA ABORDAGEM DIFERENTE. VOCÊ PODE DESCREVER..."),
    
    (r".*\b(\d+)\s*(vezes|dias|horas|minutos)\b.*", 
     r"VOCÊ CITOU \1 \2. ISSO INDICA UMA OCORRÊNCIA FREQUENTE?"),

    (r"^.*$", "VOCÊ PODE ME EXPLICAR COM MAIS DETALHES O QUE ESTÁ ACONTECENDO?")
]

while True:
    comment = input("> ")
    response = comment.lower()
    for pat, sub in patterns:
        response, count = re.subn(pat, sub, response)
        if count > 0:
            break  
    print(response.upper())