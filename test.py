from model import Question
import json
from types import SimpleNamespace


def test():
    question = Question("инфа", "ответ")
    question.toJsonFile("Новый файл3")
    #newfile = open(cd+"/lol1.json")
    #data = json.load(newfile)
    #print(data.get("answer"))
    #newformat = dict()
    #newformat[data["question"]] = data["answer"]
    #q = "инфа"
    #print(newformat[q])
