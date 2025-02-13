# Example API Documentation

## Connecting to the API
Since we are running our API locally we will access the endpoint at ```http://127.0.0.1:5000``` (or the address the appears on your console).

## Welcome
- Method: GET
- Path: ```/```
- Query parameters: None

This is just a friendly welcome to the API.

## Sum
- Method: GET
- Path: ```/sum```
- Query parameters: two integers ```a``` and ```b```

This query returns the sum of the two numbers in json format.

## Factorial
- Method: GET
- Path: ```/factorial```
- Query parameters: An integer number ```n```

This query display a message with the result of n!. If no number is provided, it takes ```n = 10``` by default.
