import customtkinter as ctk

# Set appearance and scaling
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # You can customize this

class MarsRoverUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mars Rover UI")
        self.geometry("1200x800")
        self.resizable(False, False)

        # Top Frame - Connection Button
        self.top_frame = ctk.CTkFrame(self, height=50)
        self.top_frame.pack(fill="x", side="top")

        self.connect_button = ctk.CTkButton(
            self.top_frame, text="Connect to ESP32", command=self.connect_to_esp32
        )
        self.connect_button.pack(pady=10)

        # Middle Frame - Controls + Camera Feed + Controls
        self.middle_frame = ctk.CTkFrame(self)
        self.middle_frame.pack(expand=True, fill="both")

        # Left Controls
        self.left_controls = ctk.CTkFrame(self.middle_frame, width=150)
        self.left_controls.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(self.left_controls, text="Left Controls").pack(pady=10)

        # Camera Feed Area
        self.camera_feed = ctk.CTkFrame(self.middle_frame, width=720, height=480)
        self.camera_feed.pack(side="left", expand=True, padx=10, pady=10)
        ctk.CTkLabel(self.camera_feed, text="Camera Feed").pack(expand=True)

        # Right Controls
        self.right_controls = ctk.CTkFrame(self.middle_frame, width=150)
        self.right_controls.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(self.right_controls, text="Right Controls").pack(pady=10)

        # Bottom Frame - Page Buttons
        self.bottom_frame = ctk.CTkFrame(self, height=50)
        self.bottom_frame.pack(fill="x", side="bottom")

        self.page1_button = ctk.CTkButton(self.bottom_frame, text="Page 1", command=self.go_to_page1)
        self.page1_button.pack(side="left", padx=10, pady=10)

        self.page2_button = ctk.CTkButton(self.bottom_frame, text="Page 2", command=self.go_to_page2)
        self.page2_button.pack(side="left", padx=10, pady=10)

    def connect_to_esp32(self):
        print("Attempting connection to ESP32...")
        # You’ll call your server.py stuff here

    def go_to_page1(self):
        print("Navigating to Page 1")

    def go_to_page2(self):
        print("Navigating to Page 2")

if __name__ == "__main__":
    app = MarsRoverUI()
    app.mainloop()

