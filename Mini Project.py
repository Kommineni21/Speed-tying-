import tkinter as tk
import random
import time

# Sample texts for typing test
sample_texts = [
    "Typing tests can improve your speed and accuracy.",
]

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.text_to_type = ""
        self.start_time = None
        self.score = 0

        # UI Components
        self.label_instructions = tk.Label(root, text="Click 'Start' to begin the test.", font=("Bell MT", 16))
        self.label_instructions.pack(pady=10)

        self.label_text = tk.Label(root, text="", font=("Candara",14), wraplength=400, justify="center")
        self.label_text.pack(pady=10)

        self.entry_text = tk.Entry(root, width=50, font=("Candara", 14)) 
        self.entry_text.pack(pady=10)
        self.entry_text.bind("<Return>", self.check_text)
        self.entry_text.config(state="disabled")

        self.label_score = tk.Label(root, text="Score: 0", font=("Candara",14))
        self.label_score.pack(pady=10)

        self.button_start = tk.Button(root, text="Start", command=self.start_test, font=("Candara", 14))
        self.button_start.pack(pady=10)

    def start_test(self):
        # Reset fields
        self.entry_text.delete(0, tk.END)
        self.entry_text.config(state="normal")
        self.label_instructions.config(text="Type the text below as fast as you can and press Enter.")
        self.text_to_type = random.choice(sample_texts)
        self.label_text.config(text=self.text_to_type)
        self.start_time = time.time()

    def check_text(self, event):
        typed_text = self.entry_text.get()
        self.entry_text.config(state="disabled")
        end_time = time.time()

        # Calculate time taken and score
        time_taken = end_time - self.start_time
        words = len(self.text_to_type.split())
        accuracy = sum(1 for a, b in zip(typed_text, self.text_to_type) if a == b) / max(len(self.text_to_type), 1)
        speed = words / (time_taken / 60)

        self.score =int(speed//10)

        self.label_instructions.config(
            text=f"Test completed! Time taken: {time_taken:.2f} seconds, Speed: {speed:.2f} WPM, Accuracy: {accuracy:.2%}"
        )
        self.label_score.config(text=f"Score: {self.score}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
