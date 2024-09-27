<p align="center" style="margin: 40px 0">
    Acuracia.io
</p>

<div align="center">

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

</div>

# Acuracia.io - API

Cálculo de acuracia.

Software foi desenvolvido para o MVP da pós graduação de Engenharia de Software PUC-Rio, Disciplina: Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes (40530010063_20240_01)
Apresentação em: ...

> ⚠️ O frontend que consome essa API pode ser acessado em: [clicando aqui](https://github.com/elianoestevampuc/acuracia.io-frontend).

## Executando a API


### 1 - Clonar o repositório
Para clonar o projeto execute seguinte comando:

```
git clone https://github.com/elianoestevampuc/acuracia.io-backend.git
```

#

### 2 - Criando um ambiente virtual (opcional)

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
Você pode criar um  ambiente virtual a partir do seguinte comando:

```
python -m venv env
```

Após criar o ambiente virtual, você pode ativá-lo a partir do seguinte comando:

```
# Windows:
.\env\Scripts\activate.ps1

# Linux ou Mac:
source ./python_env/bin/activate
```

### 3 - Instalando as dependências

Para instalar as libs listadas no arquivo `requirements.txt`, execute o comando abaixo:

```
(env)$ pip install -r requirements.txt
```
### 4 - Executando a API
Para executar a API, basta executar o seguinte comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento, é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte, conforme abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000](http://localhost:5000) no navegador para verificar o status da API em execução.