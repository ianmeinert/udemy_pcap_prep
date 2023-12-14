from random import choice
from typing import List


class Player:
    def __init__(self, name="") -> None:
        self.score = 0
        self.name = name

    def choose(self):
        return choice(["r", "p", "s"])


class HumanPlayer(Player):
    def __init__(self) -> None:
        super().__init__(name="You")

    def choose(self):
        while True:
            user_choice = input("Rock, paper, or scissors [r/p/s]?: ")

            if user_choice.isalpha() and user_choice in ["r", "p", "s"]:
                return user_choice.lower()


class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__(name="Computer")


class Game:
    _CHOICES = {"r": "Rock", "p": "Paper", "s": "Scissors"}

    def __init__(self, num_rounds) -> None:
        self.num_rounds = num_rounds
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()
        self.current_round = 0

    def settle_round(self, round_status):
        print(f"You {round_status} this round!\n")

        if round_status == "won":
            self.human.score += 1
        elif round_status == "lost":
            self.computer.score += 1
        elif round_status == "tied":
            self.human.score += 1
            self.computer.score += 1

    def play_round(self):
        human_choice = self._CHOICES[self.human.choose()]
        computer_choice = self._CHOICES[self.computer.choose()]

        results = f"{self.human.name}: {human_choice} | {self.computer.name}: {computer_choice}"
        print(results)

        match (human_choice, computer_choice):
            case ("Rock", "Scissors") | ("Paper", "Rock") | ("Scissors", "Paper"):
                return "won"
            case ("Rock", "Paper") | ("Paper", "Scissors") | ("Scissors", "Rock"):
                return "lost"
            case _:
                return "tied"

    def summarize_scores(self):
        if self.current_round == self.num_rounds:
            print(
                f"[Game summary] {self.human.name}: {self.human.score} | {self.computer.name}: {self.computer.score}"
            )

            if self.human.score > self.computer.score:
                print("You won.")
            elif self.human.score < self.computer.score:
                print("You lost.")
            elif self.human.score == self.computer.score:
                print("You tied.")

    def play(self):
        while self.current_round < self.num_rounds:
            results = self.play_round()

            self.settle_round(results)
            self.current_round += 1

        self.summarize_scores()


def start_game(num_rounds):
    game = Game(num_rounds=num_rounds)
    game.play()


def show_menu(title):
    print(title)

    while True:
        num_rounds = input("How many rounds would you like to play?: ")

        if num_rounds.isnumeric():
            start_game(int(num_rounds))
            break


title = "--- Rick Paper Scissors Game ---"
show_menu(title)
