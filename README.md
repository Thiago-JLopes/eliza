# Chatbot Eliza - Suporte Técnico

Este projeto é uma versão personalizada do chatbot Eliza, focada no **domínio de suporte técnico**. O objetivo é identificar automaticamente situações comuns enfrentadas por usuários de sistemas computacionais, como lentidão, erros, falhas de rede, e reagir com empatia e sugestões apropriadas.

## 💡 Domínio de Aplicação

O chatbot Eliza foi adaptado para atuar como um atendente virtual de **suporte técnico de TI**. Ele entende expressões comuns relacionadas a problemas com sistemas, como falhas, lentidão, erros, bugs, entre outros, e responde de forma acolhedora e guiada, utilizando expressões regulares para identificar padrões nas mensagens dos usuários.

## ✅ Funcionalidades com Expressões Regulares

- Identificação de **datas** (ex: "12/05/2024")
- Reconhecimento de **numerais com unidades** (ex: "3 vezes", "2 dias")
- Detecção de **radicais de palavras** como `trav`, `bug`, `falh`, `reinici`, etc.
- Uso de palavras **pré-definidas** (ex: "não aguento mais", "sim", "não", etc.) para gerar respostas empáticas e direcionadas

## 💬 Exemplo de Diálogo

```plaintext
> estou com erro 403
ENTENDO QUE VOCÊ ESTÁ COM ERRO 403. ISSO PODE SER FRUSTRANTE. VOCÊ JÁ TENTOU REINICIAR O SISTEMA?

> internet lenta
A CONEXÃO ESTÁ LENTA? ISSO TEM ACONTECIDO FREQUENTEMENTE?

> 12/05/2024 foi quando parou
VOCÊ MENCIONOU A DATA 12/05/2024. FOI NESSE DIA QUE O PROBLEMA COMEÇOU?

>sim
OK, OBRIGADO PELA CONFIRMAÇÃO. TEM MAIS ALGUMA INFORMAÇÃO RELEVANTE?

> não aguento mais
EU ENTENDO SUA FRUSTRAÇÃO. VAMOS TENTAR RESOLVER ISSO JUNTOS.

> travou de novo
PARECE QUE O SISTEMA ESTÁ COM ALGUM PROBLEMA DE TRAV... PODE ME CONTAR MAIS?

> 3 vezes hoje
VOCÊ CITOU 3 VEZES. ISSO INDICA UMA OCORRÊNCIA FREQUENTE?

> o sistema está com bug
PARECE QUE O SISTEMA ESTÁ COM ALGUM PROBLEMA DE BUG... PODE ME CONTAR MAIS?
