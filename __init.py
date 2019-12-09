

import sys
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

from functools import reduce
import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)


from requests.exceptions import HTTPError

app = Flask(__name__)
json = FlaskJSON(app)

# This is not a REST API, strictly speaking.  I'm not shooting for idiomatic purity.

schema = "id,first_name,last_name,phone_number,client_member_id,account_id"


@app.route('/batchuploadmembers', methods=['POST'])
def batch_upload():
    data = request.get_json(force=True)
    members_csv = data["members_csv"].splitlines()
    def iter0(acc, member):
        record = member.split(",")
        record_1 = {
            "id": record[0],
            "first_name": record[1],
            "last_name": record[2],
            "phone_number": record[3],
            "client_member_id": record[4],
            "account_id": record[5]
        }
        acc[record_1["id"]] = record_1
        return acc
    ready_collection = reduce(iter0, members_csv, {})
    # print(ready_collection)
    with r.pipeline() as pipe:
        for record_id, record2 in ready_collection.items():
            # print('record2', record2)
            pipe.hmset("member:" + str(record_id), record2)
            pipe.sadd("account:" + record2["account_id"], record_id)
            pipe.set("phone_link:" + record2["phone_number"], record_id)
            pipe.set("client_member_id_link:" + record2["client_member_id"], record_id)
        pipe.execute()
    return "OK"








@app.route('/readmembersbyaccount', methods=['POST'])
def members_by_account():
    data = request.get_json(force=True)
    try:
        account_id = data['account_id']
        print("account_id", account_id)
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    member_ids = r.smembers("account:" + str(account_id))
    def iter3(acc, id):
        acc[id] = r.hgetall("member:" + id)
        return acc
    arq = reduce(iter3, member_ids, {})

    return arq








@app.route('/readmember', methods=['POST'])
def read_member():
    data = request.get_json(force=True)
    # Need to do a bunch of tries, because we only need one of the three to read.
    try:
        phone_number = data['phone_number']
        client_member_id = data['client_member_id']
        id = data['id']
    except (KeyError, TypeError, ValueError):
        raise(JsonError(description='Invalid value.'))


    cand = r.hgetall(id)
    if isinstance(cand, dict) and len(cand) > 0:
        return cand
    phone_link = r.get("phone_link:" + str(phone_number))
    print("phone_link", phone_link)
    if phone_link != None:
        cand = r.hgetall("member:" + str(phone_link))
    else:
        cand = None
    if isinstance(cand, dict) and len(cand) > 0:
        return cand
    client_member_id_link = r.get("client_member_id_link:" + str(client_member_id))
    print("client_member_id_link", client_member_id_link)
    if client_member_id_link != None:
        cand = r.hgetall("member:" + str(client_member_id_link))
    else:
        cand = None
    if isinstance(cand, dict) and len(cand) > 0:
        return cand

    return "Not found."







@app.route('/createmember', methods=['POST'])
def create_member():
    data = request.get_json(force=True)
    try:
        id = data["id"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        phone_number = data["phone_number"]
        client_member_id = data["client_member_id"]
        account_id = data["account_id"]

    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')

    val = {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "client_member_id": client_member_id,
            "account_id": account_id
    }
    # print("val", val, "id", id)
    with r.pipeline() as pipe:
        pipe.hmset("member:" + str(id), val)
        pipe.sadd("account:" + str(account_id), id)
        pipe.set("phone_link:" + str(phone_number), id)
        pipe.set("client_member_id_link:" + str(client_member_id), id)
        pipe.execute()
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
