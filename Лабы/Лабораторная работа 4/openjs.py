import json
import time

start_time = time.time()

def json2xml(json_obj, tab=""):
    result_list = list()

    json_type = type(json_obj)

    if json_type is list:
        for s in json_obj:
            result_list.append(json2xml(s, tab))

        return "\n".join(result_list)

    if json_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (tab, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + tab))
            result_list.append("%s</%s>" % (tab, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (tab, json_obj)

f = open("JSON.txt", 'r', encoding = 'UTF-8')
s = f.read()
dec = json.loads(s)
print(json2xml(dec))
print("--- %s seconds ---" % (time.time() - start_time))