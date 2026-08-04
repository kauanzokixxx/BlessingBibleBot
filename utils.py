import json


def carregar_json(nome):
    with open(nome, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
