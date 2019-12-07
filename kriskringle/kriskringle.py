from string import ascii_uppercase
from random import choice


class Result:
    def __init__(self):
        self.unique_id = ''.join(choice(ascii_uppercase) for i in range(8))
        self.giver = None
        self.receiver = None


class ResultCollection:
    def __init__(self):
        self.results = []
        self.seed = ''.join(choice(ascii_uppercase) for i in range(10))
        pass

    def add(self, result):
        self.results.append(result)

    def get_result(self, unique_id):
        for result in self.results:
            if result.unique_id == unique_id:
                return result

    def is_valid(self):
        for result in self.results:
            if result.giver == result.receiver:
                return False

        return True

def create_collection(names):
    while True:
        collection = ResultCollection()
        used_receivers = []

        for name in names:
            result = Result()
            available_receivers = list(filter(lambda x: x not in used_receivers + [name], names))

            result.giver = name

            # Easy workaround for when the last person in the list has got themselves
            try:
                result.receiver = choice(available_receivers)
            except:
                continue

            used_receivers.append(result.receiver)
            collection.add(result)

        break

    return collection
