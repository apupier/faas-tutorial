import json


def main(args):
    body = json.loads(args["body"])
    text = body.get("text", "NODATA")
    replyQ = body.get("replyQ", "DLQ")
    print("Got Message : %s, \n Reply Queue: %s \n" %
          (text, replyQ))
    r = {}
    r["result"] = text.split(",")
    r["replyQ"] = replyQ
    return r
