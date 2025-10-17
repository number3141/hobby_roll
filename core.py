import random

class HobbyKit:
    def __init__(self):
        self.hobby: list[str] = list()

    def get_random_hobby(self) -> str:
        return random.choice(self.hobby)

    def add_hobby(self, new_hobby: str) -> None:
        if isinstance(new_hobby, str):
            self.hobby.append(new_hobby)

    def delete_hobby(self, del_hobby: str) -> None:
        if isinstance(del_hobby, str) and del_hobby in self.hobby:
            self.hobby.remove(del_hobby)

if __name__ == '__main__':
    test = HobbyKit()
    test.add_hobby('Попить чай')
    test.add_hobby('Почитать книгу')
