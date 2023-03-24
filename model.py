import json


class Question:
    cd = "C:/Users/user/PycharmProjects/pythonProject1/questions"

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_json(self):
        return {
            'question': self.question,
            'answer': self.answer,
        }

    def toJsonFile(self, filename):
        file = open(Question.cd + "/" + filename + ".json", "w+")
        json.dump(self.to_json(), file)
        file.close()
