# here some common methods
import requests
import json


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}
def assert_statuscode(get_statuscode,doc):
    assert get_statuscode == 200, doc + "get url status_code actually is %s" % (get_statuscode)
def assert_text(get_orderId,doc):
    text = get_orderId.text
    assert text != None,doc+"text is None"
def assert_orderId(rt,doc):
    assert rt["orderId"] != None, doc + " orderId is None"
def assert_orderstatus(text,doc):
    assert text["success"]==True,doc+"success value is %s"%(text["success"])

def get_orderId(url,doc):
    get_orderId = requests.get(url,headers=headers)
    get_statuscode = get_orderId.status_code
    assert_statuscode(get_statuscode, doc)
    assert_text(get_orderId, doc)
    rt = json.loads(get_orderId.text)
    assert_orderId(rt, doc)
    orderId = rt["orderId"]
    return orderId
def post_orderId(url,pizza_body,doc):
    post_orderid = requests.post(url,headers=headers, json=pizza_body)
    post_orderid_statuscode = post_orderid.status_code
    assert_statuscode(post_orderid_statuscode, doc)
    assert_text(post_orderid, doc)
    text = json.loads(post_orderid.text)
    assert_orderstatus(text, doc)