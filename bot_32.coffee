

c = console.log.bind console
c 93


request = require 'request'


request
    method: 'POST'
    uri: 'http://localhost:5000/mymodel/add'
    'content-type': 'application/json'
    json:
        x: 34
        y: 14
    , (err, res, body) ->
        c 'add', body



request
    method: 'POST'
    uri: 'http://localhost:5000/mymodel/subtract'
    'content-type': 'application/json'
    json:
        x: 34
        y: 14
    , (err, res, body) ->
        c 'subtract', body
