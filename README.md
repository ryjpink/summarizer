# "String Cutting" Text Summarizer

A simple REST service which summarizes text by cutting out letters

## Installation

Install third-party modules with pip:

```
$ pip install -r requirements.txt
```

## Run local service for development
```
$ python ./service.py
```

In flask, the default port is `5000`.

## Call the API

Use your favourite command-line tool to POST a request:

```
$ curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```

## Changelog

- Initial version