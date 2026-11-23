# Coletor de clima de MT

O programa mostra o clima de 4 cidades do estado. Os dados vêm de uma API. 

## Como rodar

```
py -m venv .venv 
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.venv\Scripts\Activate.ps1
pip install httpx
py clima.py
```

## O que ele gera

- `clima.csv`: Um arquivo csv com o nome da cidade e sua temperatura.
- `clima.json`: Os mesmos dados do CSV, no formato JSON.

## Se a internet cair

Se não conseguir buscar uma cidade, o programa mostra: "Não consegui buscar Cuiabá" depois segue para a próxima cidade.
Se todas as cidades falharem, os arquivos não serão alterados.