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
        
        self.hunger_label = tk.Label(stats_frame, text="Hunger: 50")
        self.hunger_label.grid(row=0, column=0, padx=10)
        
        self.happiness_label = tk.Label(stats_frame, text="Happiness: 50")
        self.happiness_label.grid(row=0, column=1, padx=10)
        
        self.cleanliness_label = tk.Label(stats_frame, text="Cleanliness: 50")
        self.cleanliness_label.grid(row=0, column=2, padx=10)
        
        self.health_label = tk.Label(stats_frame, text="Health: 50")
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
        # Implement feeding logic
        pass
    
    def play_with_pet(self):
        # Implement playing logic
        pass
    
    def clean_pet(self):
        # Implement cleaning logic
        pass
    
    def doctor_pet(self):
        # Implement doctor logic
        pass
    
    def load_game(self):
        # Implement load game logic
        pass
    
    def show_instructions(self):
        # Implement instructions display
        pass
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RaiseAGamerApp(root)
    root.mainloop()
