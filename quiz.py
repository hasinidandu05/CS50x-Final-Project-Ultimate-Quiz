#!/usr/bin/env python3
import random
import time
import json
from termcolor import colored
from datetime import datetime

# Comprehensive CS50 question bank (50+ questions)
QUESTIONS = {
    "C Programming": [
        {"question": "What command compiles C code in CS50 IDE?", "answer": "make", "difficulty": 1},
        {"question": "What is the CS50 library function for getting string input?", "answer": "get_string", "difficulty": 1},
        {"question": "What does #include do in C?", "answer": "header file inclusion", "difficulty": 2},
        {"question": "How do you print formatted output in C?", "answer": "printf", "difficulty": 1},
        {"question": "What is the correct way to compare strings in C?", "answer": "strcmp", "difficulty": 3},
        {"question": "What type of loop is 'for (int i = 0; i < n; i++)'?", "answer": "for loop", "difficulty": 1},
        {"question": "What does malloc() do in C?", "answer": "memory allocation", "difficulty": 3},
        {"question": "What is the size of an int in bytes typically?", "answer": "4", "difficulty": 2},
        {"question": "What does the -> operator do in C?", "answer": "access struct member via pointer", "difficulty": 3},
        {"question": "What is the null character in C strings?", "answer": "\\0", "difficulty": 2}
    ],
    "Python": [
        {"question": "How do you create a list in Python?", "answer": "square brackets []", "difficulty": 1},
        {"question": "What Python function converts a string to lowercase?", "answer": "lower()", "difficulty": 1},
        {"question": "What does 'if __name__ == \"__main__\":' do?", "answer": "runs code when executed directly", "difficulty": 3},
        {"question": "How do you open a file in Python?", "answer": "with open()", "difficulty": 2},
        {"question": "What is the main CS50 Python library function?", "answer": "get_string", "difficulty": 1},
        {"question": "What does list.append() do?", "answer": "adds item to end of list", "difficulty": 1},
        {"question": "How do you create a dictionary?", "answer": "curly braces {}", "difficulty": 1},
        {"question": "What does 'import sys' do?", "answer": "imports system module", "difficulty": 2},
        {"question": "What is the Python equivalent of C's struct?", "answer": "class", "difficulty": 3},
        {"question": "How do you handle exceptions in Python?", "answer": "try except", "difficulty": 2}
    ],
    "Algorithms": [
        {"question": "What search algorithm divides the problem in half each time?", "answer": "binary search", "difficulty": 2},
        {"question": "What is the time complexity of bubble sort?", "answer": "O(n^2)", "difficulty": 3},
        {"question": "What data structure uses FIFO ordering?", "answer": "queue", "difficulty": 2},
        {"question": "What algorithm uses a pivot element?", "answer": "quicksort", "difficulty": 3},
        {"question": "What is the most efficient sorting algorithm?", "answer": "merge sort", "difficulty": 3},
        {"question": "What data structure uses LIFO ordering?", "answer": "stack", "difficulty": 2},
        {"question": "What algorithm always takes the best immediate choice?", "answer": "greedy algorithm", "difficulty": 3},
        {"question": "What is the time complexity of linear search?", "answer": "O(n)", "difficulty": 2},
        {"question": "What is recursion?", "answer": "function calling itself", "difficulty": 2},
        {"question": "What algorithm did we use for credit card validation?", "answer": "luhn's algorithm", "difficulty": 3}
    ],
    "SQL": [
        {"question": "What SQL command retrieves data?", "answer": "SELECT", "difficulty": 1},
        {"question": "What clause filters GROUP BY results?", "answer": "HAVING", "difficulty": 3},
        {"question": "What joins two tables in SQL?", "answer": "JOIN", "difficulty": 2},
        {"question": "What SQLite command shows table structure?", "answer": "schema", "difficulty": 2},
        {"question": "What constraint ensures unique values?", "answer": "UNIQUE", "difficulty": 2},
        {"question": "What type of database does CS50 use?", "answer": "SQLite", "difficulty": 1},
        {"question": "What command modifies existing data?", "answer": "UPDATE", "difficulty": 1},
        {"question": "What command adds new data?", "answer": "INSERT", "difficulty": 1},
        {"question": "What command removes data?", "answer": "DELETE", "difficulty": 1},
        {"question": "What clause sorts results?", "answer": "ORDER BY", "difficulty": 1}
    ],
    "Web": [
        {"question": "What HTML tag creates a hyperlink?", "answer": "<a>", "difficulty": 1},
        {"question": "What CSS property changes text color?", "answer": "color", "difficulty": 1},
        {"question": "What JavaScript function runs after delay?", "answer": "setTimeout", "difficulty": 3},
        {"question": "What Flask decorator routes URLs?", "answer": "@app.route", "difficulty": 2},
        {"question": "What HTTP method submits form data?", "answer": "POST", "difficulty": 2},
        {"question": "What template language does Flask use?", "answer": "Jinja", "difficulty": 2},
        {"question": "What protocol serves web pages?", "answer": "HTTP", "difficulty": 1},
        {"question": "What tag imports JavaScript?", "answer": "<script>", "difficulty": 1},
        {"question": "What CSS framework does CS50 use?", "answer": "Bootstrap", "difficulty": 1},
        {"question": "What Python web framework does CS50 use?", "answer": "Flask", "difficulty": 1}
    ],
    "CS50 Trivia": [
        {"question": "Who teaches CS50?", "answer": "David Malan", "difficulty": 1},
        {"question": "What does David throw in lectures?", "answer": "paper", "difficulty": 1},
        {"question": "What color is CS50's logo?", "answer": "red", "difficulty": 1},
        {"question": "Where is CS50 filmed?", "answer": "Harvard", "difficulty": 1},
        {"question": "What week covers Python?", "answer": "6", "difficulty": 1},
        {"question": "What IDE does CS50 use?", "answer": "VS Code", "difficulty": 1},
        {"question": "What's the first problem set?", "answer": "Hello", "difficulty": 1},
        {"question": "What animal appears in CS50 puzzles?", "answer": "duck", "difficulty": 2},
        {"question": "What's the final project requirement?", "answer": "video", "difficulty": 1},
        {"question": "What's special about Week 0?", "answer": "Scratch", "difficulty": 1}
    ]
}

# [Rest of the code remains exactly the same as previous premium version]
# (The QuizGame class and all its methods stay identical)
class QuizGame:
    def __init__(self):
        self.score = 0
        self.leaderboard = []
        self.load_leaderboard()
        
    def load_leaderboard(self):
        try:
            with open("leaderboard.json", "r") as f:
                self.leaderboard = json.load(f)
        except FileNotFoundError:
            self.leaderboard = []
    
    def save_score(self, name):
        self.leaderboard.append({
            "name": name,
            "score": self.score,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        with open("leaderboard.json", "w") as f:
            json.dump(self.leaderboard, f, indent=2)
    
    def select_questions(self, num=10):
        all_questions = []
        for category in QUESTIONS.values():
            all_questions.extend(category)
        return random.sample(all_questions, min(num, len(all_questions)))
    
    def run(self):
        print(colored("\n=== CS50 MASTER QUIZ ===", "cyan", attrs=["bold"]))
        print(colored("Test your CS50 knowledge!\n", "yellow"))
        
        questions = self.select_questions()
        start_time = time.time()
        
        for i, q in enumerate(questions, 1):
            print(colored(f"\nQuestion {i}/{len(questions)} ({q['difficulty']*'★'})", "magenta"))
            print(colored(q["question"], "blue"))
            
            try:
                user_answer = input("> ").strip().lower()
                if user_answer in ("quit", "exit"):
                    print(colored("\nQuiz ended early!", "red"))
                    break
                    
                if user_answer == q["answer"].lower():
                    print(colored("✓ Correct! +1 point", "green"))
                    self.score += 1
                else:
                    print(colored(f"✗ Wrong! Answer: {q['answer']}", "red"))
                
                print(f"Current score: {self.score}/{i}")
                
            except KeyboardInterrupt:
                print(colored("\nQuiz cancelled!", "red"))
                return
        
        time_taken = round(time.time() - start_time, 1)
        percentage = round((self.score / len(questions)) * 100)
        
        # Display results
        print(colored("\n=== RESULTS ===", "cyan", attrs=["bold"]))
        print(colored(f"Final Score: {self.score}/{len(questions)}", "yellow"))
        print(colored(f"Percentage: {percentage}%", "yellow"))
        print(colored(f"Time Taken: {time_taken}s", "yellow"))
        
        # Performance feedback
        feedback = [
            (90, "Perfect! CS50 certified!", "green"),
            (70, "Great job! Almost there!", "green"),
            (50, "Good attempt! Keep learning!", "blue"),
            (0, "Review time! You got this!", "red")
        ]
        
        for threshold, message, color in feedback:
            if percentage >= threshold:
                print(colored(f"\n{message}", color, attrs=["bold"]))
                break
        
        # Leaderboard
        if input("\nSave to leaderboard? (y/n): ").lower() == "y":
            name = input("Enter your name: ").strip() or "Anonymous"
            self.save_score(name)
            
            print(colored("\n--- LEADERBOARD ---", "cyan"))
            sorted_scores = sorted(self.leaderboard, key=lambda x: (-x["score"], x["date"]))
            for entry in sorted_scores[:5]:
                print(f"{entry['name']}: {entry['score']} ({entry['date']})")

if __name__ == "__main__":
    quiz = QuizGame()
    quiz.run()