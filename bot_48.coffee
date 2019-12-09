


c = console.log.bind console
fs = require 'fs'
members_csv = fs.readFileSync './member_data.csv', 'utf8'
request = require 'request'
redis = require 'redis'

client = redis.createClient()





batch_upload_members = ->
    request
        method: 'POST'
        uri: 'http://localhost:5000/batchuploadmembers'
        'content-type': 'application/json'
        json:
            members_csv: members_csv
        , (err, res, body) ->
            c 'batch_upload', body

#


read_members_by_account = ->
    request
        method: 'POST'
        uri: 'http://localhost:5000/readmembersbyaccount'
        'content-type': 'application/json'
        json:
            account_id: 16
        , (err, res, body) ->
            c 'Read members by account', body




create_member = ->
    request
        method: 'POST'
        uri: 'http://localhost:5000/createmember'
        'content-type': 'application/json'
        json:
            id : 999999
            first_name : "Amber"
            last_name : "Bronze"
            phone_number : 88888999999
            client_member_id : 2929283929
            account_id : 8585994
        , (err, res, body) ->
            c 'Create member', body




read_member = ->
    request
        method: 'POST'
        uri: 'http://localhost:5000/readmember'
        'content-type': 'application/json'
        # NOTE: According to this API, fields can be empty strings in the values but the properties must be present/keyed.
        json:
            # id : 999999
            id: ""
            # phone_number : 88888999999
            phone_number: ""
            client_member_id : 2929283929
        , (err, res, body) ->
            c 'Read member', body




flushall = ->
    client.flushall()


flushall()

setTimeout batch_upload_members, 1000


setTimeout read_members_by_account, 2000

setTimeout create_member, 3000


setTimeout read_member, 4000
