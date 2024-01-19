import random

class TriviaGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self):
        # Selectează o întrebare aleatorie din listă
        question = random.choice(self.questions)
        print(question["text"])
        for idx, option in enumerate(question["options"]):
            print(f"{idx + 1}. {option}")

        # Obține răspunsul utilizatorului
        answer = int(input("Alegeți răspunsul (introduceți numărul): "))
        if question["options"][answer - 1] == question["correct_answer"]:
            self.score += 1
            print("Răspuns corect!")
        else:
            print("Răspuns incorect!")

    def play(self):
        num_questions = int(input("Câte întrebări doriți să răspundeți? "))
        for _ in range(num_questions):
            self.ask_question()
            print(f"Scorul actual: {self.score}")
        print("Joc terminat! Scorul final:", self.score)


# Exemplu de întrebări pentru joc
questions = [
    {
        "text": "Care este capitala Franței?",
        "options": ["Paris", "Londra", "Berlin", "Roma"],
        "correct_answer": "Paris"
    },
    {
        "text": "Cine a scris 'Romeo și Julieta'?",
        "options": ["William Shakespeare", "Jane Austen", "Leo Tolstoy", "Mark Twain"],
        "correct_answer": "William Shakespeare"
    },
    {
        "text": "Care este cel mai înalt munte din lume?",
        "options": ["K2", "Everest", "Kilimanjaro", "Mont Blanc"],
        "correct_answer": "Everest"
    },
    {
        "text": "Cine a pictat 'Mona Lisa'?",
        "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "text": "Care este cel mai lung râu din lume?",
        "options": ["Nil", "Amazon", "Yangtze", "Mississippi"],
        "correct_answer": "Nil"
    },
    {
        "text": "În ce an a început Primul Război Mondial?",
        "options": ["1914", "1918", "1939", "1945"],
        "correct_answer": "1914"
    },
    {
        "text": "Care este formula chimică a apei?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "correct_answer": "H2O"
    },
    {
        "text": "Cine a inventat becul electric?",
        "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein"],
        "correct_answer": "Thomas Edison"
    },
    {
        "text": "Care este cel mai mare ocean din lume?",
        "options": ["Oceanul Atlantic", "Oceanul Indian", "Oceanul Pacific", "Oceanul Arctic"],
        "correct_answer": "Oceanul Pacific"
    },
    {
        "text": "Cine a fost primul om care a pășit pe Lună?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
        "correct_answer": "Neil Armstrong"
    }
]


# Crearea și rularea jocului
trivia_game = TriviaGame(questions)
trivia_game.play()
