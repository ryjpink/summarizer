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

You should get a response with a shortened text:
```
{
  "return_string": "muydv"
}
```

### Advanced usage

To control the amount of summarization, you can set the `skipLength` query parameter:

* Less summarized:
    ```
    $ curl -X POST http://127.0.0.1:5000/test?skipLength=2 --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
    {
      "return_string": "ayulfdie"
    }
    ```
* More summarized:
    ```
    $ curl -X POST http://127.0.0.1:5000/test?skipLength=4 --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
    {
      "return_string": "ylde"
    }
    ```

## Changelog

- Added optional `skipLength` parameter
- Initial version