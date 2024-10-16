#Stephanie Ray
#10/13/2024
#GUI based game to interact with avatar
#M08 Final

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RaiseAGamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Raise a Gamer")
        self.root.geometry("600x400")

        self.main_menu()

    def main_menu(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Raise a Gamer", font=("Arial", 24))
        title.pack(pady=20)

        new_game_btn = tk.Button(self.root, text="New Game", command=self.pet_selection)
        new_game_btn.pack(pady=10)

        load_game_btn = tk.Button(self.root, text="Load Game", command=self.load_game)
        load_game_btn.pack(pady=10)

        instructions_btn = tk.Button(self.root, text="Instructions", command=self.show_instructions)
        instructions_btn.pack(pady=10)

    def pet_selection(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Select Your Pet", font=("Arial", 18))
        title.pack(pady=20)

        pet_options = ["Dog", "Cat", "Dragon"]
        self.selected_pet = tk.StringVar(value=pet_options[0])

        for pet in pet_options:
            rb = tk.Radiobutton(self.root, text=pet, variable=self.selected_pet, value=pet)
            rb.pack(anchor=tk.W)

        name_label = tk.Label(self.root, text="Name Your Pet:")
        name_label.pack(pady=10)

        self.pet_name_entry = tk.Entry(self.root)
        self.pet_name_entry.pack(pady=10)

        start_game_btn = tk.Button(self.root, text="Start Game", command=self.start_game)
        start_game_btn.pack(pady=20)

    def start_game(self):
        self.pet_name = self.pet_name_entry.get()
        self.pet_type = self.selected_pet.get()

        if not self.pet_name:
            messagebox.showwarning("Input Error", "Please enter a name for your pet.")
            return

        self.main_game_screen()

    def main_game_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text=f"{self.pet_name} the {self.pet_type}", font=("Arial", 18))
        title.pack(pady=20)

        self.pet_image = ImageTk.PhotoImage(Image.open(f"{self.pet_type.lower()}.png"))
        pet_image_label = tk.Label(self.root, image=self.pet_image)
        pet_image_label.pack(pady=10)

        stats_frame = tk.Frame(self.root)
        stats_frame.pack(pady=10)

        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 50
        self.health = 50

        self.hunger_label = tk.Label(stats_frame, text=f"Hunger: {self.hunger}")
        self.hunger_label.grid(row=0, column=0, padx=10)

        self.happiness_label = tk.Label(stats_frame, text=f"Happiness: {self.happiness}")
        self.happiness_label.grid(row=0, column=1, padx=10)

        self.cleanliness_label = tk.Label(stats_frame, text=f"Cleanliness: {self.cleanliness}")
        self.cleanliness_label.grid(row=0, column=2, padx=10)

        self.health_label = tk.Label(stats_frame, text=f"Health: {self.health}")
        self.health_label.grid(row=0, column=3, padx=10)

        actions_frame = tk.Frame(self.root)
        actions_frame.pack(pady=10)

        feed_btn = tk.Button(actions_frame, text="Feed", command=self.feed_pet)
        feed_btn.grid(row=0, column=0, padx=10)

        play_btn = tk.Button(actions_frame, text="Play", command=self.play_with_pet)
        play_btn.grid(row=0, column=1, padx=10)

        clean_btn = tk.Button(actions_frame, text="Clean", command=self.clean_pet)
        clean_btn.grid(row=0, column=2, padx=10)

        doctor_btn = tk.Button(actions_frame, text="Doctor", command=self.doctor_pet)
        doctor_btn.grid(row=0, column=3, padx=10)

    def feed_pet(self):
        self.hunger = min(self.hunger + 10, 100)
        self.hunger_label.config(text=f"Hunger: {self.hunger}")
        messagebox.showinfo("Feed", f"You fed {self.pet_name}. Hunger is now {self.hunger}.")

    def play_with_pet(self):
        self.happiness = min(self.happiness + 10, 100)
        self.happiness_label.config(text=f"Happiness: {self.happiness}")
        messagebox.showinfo("Play", f"You played with {self.pet_name}. Happiness is now {self.happiness}.")

    def clean_pet(self):
        self.cleanliness = min(self.cleanliness + 10, 100)
        self.cleanliness_label.config(text=f"Cleanliness: {self.cleanliness}")
        messagebox.showinfo("Clean", f"You cleaned {self.pet_name}. Cleanliness is now {self.cleanliness}.")

    def doctor_pet(self):
        self.health = min(self.health + 10, 100)
        self.health_label.config(text=f"Health: {self.health}")
        messagebox.showinfo("Doctor", f"You took {self.pet_name} to the doctor. Health is now {self.health}.")

    def load_game(self):
        messagebox.showinfo("Load Game", "Load game functionality not implemented yet.")

    def show_instructions(self):
        instructions = (
            "Welcome to Raise a Gamer!\n\n"
            "1. Select a pet and give it a name.\n"
            "2. Take care of your pet by feeding, playing, cleaning, and taking it to the doctor.\n"
            "3. Monitor your pet's stats to ensure it stays happy and healthy.\n"
            "4. Enjoy raising your virtual pet!"
        )
        messagebox.showinfo("Instructions", instructions)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RaiseAGamerApp(root)
    root.mainloop()
