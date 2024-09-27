import pandas as pd

class Dado:

    def carregar(self, url: str, atributos: list):
        return pd.read_csv(url, names=atributos)
    
    def adicionar(self, url: str, dado: str):
        with open(url, 'r+') as fp:
            lines = fp.readlines()
            lines.insert(0, dado.decode() + "\n")
            fp.seek(0)
            fp.writelines(lines)       