# Análise de Sentimento de Texto

Este projeto é uma aplicação web simples que utiliza um modelo de Machine Learning para realizar análises de sentimento de texto em português.

## Como funciona

A aplicação consiste em uma interface web que permite ao usuário inserir um texto em um campo de texto e, ao clicar em um botão, a aplicação irá analisar o sentimento do texto e retornar se ele é positivo, negativo ou neutro.

## Como foi construído

Este projeto foi construído utilizando a biblioteca Flask para a parte de back-end e HTML/CSS/JS para a interface web.

O modelo de Machine Learning foi treinado com dados de treinamento em português (base.csv) usando o algoritmo de Naive Bayes e a biblioteca scikit-learn. O modelo foi treinado no arquivo `treino.py` e salvo em arquivos .pkl para ser usado posteriormente na aplicação.

## Como executar

1. Clone este repositório em sua máquina local:

    ```sh
    git clone https://github.com/faustinopsy/flask.git
    ```

2. Navegue até a pasta do projeto:

    ```sh
    cd flask
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

5. Inicie a aplicação:

    ```sh
    python app.py
    ```

6. Abra seu navegador e acesse a aplicação no endereço [http://localhost:5000](http://localhost:5000).

## Autor

Nome do Autor
- [Github](https://github.com/faustinopsy)
- [LinkedIn](https://www.linkedin.com/in/faustinopsy)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
