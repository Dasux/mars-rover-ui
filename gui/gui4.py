import customtkinter as ctk
import sys
import threading
import socket
import signal
# sys.path.append('../backend')  # Adjust the path as necessary

from server2 import Server  # if the file is mymodule.py

# Set appearance and scaling
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # You can customize this

class MarsRoverUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mars Rover UI")
        self.geometry("1200x800")
        self.resizable(False, False)
        self.server = Server()

        # Start the server in a separate thread
        self.server_thread = threading.Thread(target=self.server.start_server, daemon=True)
        self.server_thread.start()

        # Handle SIGINT (Ctrl+C) in the main thread
        signal.signal(signal.SIGINT, self.handle_sigint)

        # Handle window close event
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        # Top Frame - Connection Button
        self.top_frame = ctk.CTkFrame(self, height=50)
        self.top_frame.pack(fill="x", side="top")

        self.connect_button = ctk.CTkButton(
            self.top_frame, text="Connect to ESP32", command=self.connect_to_esp32
        )
        self.connect_button.pack(pady=10)

        self.close_btn = ctk.CTkButton(
            self.top_frame, text="Close", command=self.close_server
        )
        self.close_btn.pack(pady=10)

        # Middle Frame - Controls + Camera Feed + Controls
        self.middle_frame = ctk.CTkFrame(self)
        self.middle_frame.pack(expand=True, fill="both")

        # Left Controls
        self.left_controls = ctk.CTkFrame(self.middle_frame, width=150)
        self.left_controls.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(self.left_controls, text="Left Controls").pack(pady=10)

        # Container for buttons in the left controls section
        self.left_button_container = ctk.CTkFrame(self.left_controls)
        self.left_button_container.pack(expand=True, fill="both", pady=10)

        self.left_button1 = ctk.CTkButton(self.left_button_container, text="Left Button 1", command=self.left_button1_action)
        self.left_button1.pack(expand=True, fill="both", pady=5)

        self.left_button2 = ctk.CTkButton(self.left_button_container, text="Left Button 2", command=self.left_button2_action)
        self.left_button2.pack(expand=True, fill="both", pady=5)

        # Camera Feed Area
        self.camera_feed = ctk.CTkFrame(self.middle_frame, width=720, height=480)
        self.camera_feed.pack(side="left", expand=True, padx=10, pady=10)
        ctk.CTkLabel(self.camera_feed, text="Camera Feed").pack(expand=True)

        # Right Controls
        self.right_controls = ctk.CTkFrame(self.middle_frame, width=150)
        self.right_controls.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(self.right_controls, text="Right Controls").pack(pady=10)

        # Define the container for buttons in the right controls section
        self.right_button_container = ctk.CTkFrame(self.right_controls)
        self.right_button_container.pack(expand=True, fill="both", pady=10)

        self.right_button1 = ctk.CTkButton(
            self.right_button_container, text="Right Button 1", command=self.right_button1_action
        )
        self.right_button1.pack(expand=True, fill="both", pady=5)

        self.right_button2 = ctk.CTkButton(
            self.right_button_container, text="Right Button 2", command=self.right_button2_action
        )
        self.right_button2.pack(expand=True, fill="both", pady=5)

        # Bottom Frame - Page Buttons
        self.bottom_frame = ctk.CTkFrame(self, height=50)
        self.bottom_frame.pack(fill="x", side="bottom")

        self.page1_button = ctk.CTkButton(self.bottom_frame, text="Page 1", command=self.go_to_page1)
        self.page1_button.pack(side="left", padx=10, pady=10)

        self.page2_button = ctk.CTkButton(self.bottom_frame, text="Page 2", command=self.go_to_page2)
        self.page2_button.pack(side="left", padx=10, pady=10)

    def connect_to_esp32(self):
        print("Attempting connection to ESP32...")

    def close_server(self):
        print("Closing server...")
        self.server.stop_server()

    def handle_sigint(self, signum, frame):
        """Handle SIGINT (Ctrl+C) signal."""
        print("SIGINT received. Stopping server...")
        self.on_exit()

    def on_exit(self):
        """Handle the exit event when the window is closed."""
        try:
            print("Closing application...")
            self.server.stop_server()  # Gracefully stop the server
        except Exception as e:
            print(f"Error while stopping server: {e}")
        finally:
            self.destroy()  # Close the application window
            sys.exit(0)  # Ensure the program exits completely

    def go_to_page1(self):
        print("Navigating to Page 1")

    def go_to_page2(self):
        print("Navigating to Page 2")

    def left_button1_action(self):
        print("Left Button 1 clicked")

    def left_button2_action(self):
        print("Left Button 2 clicked")

    def right_button1_action(self):
        print("Right Button 1 clicked")

    def right_button2_action(self):
        print("Right Button 2 clicked")

if __name__ == "__main__":
    app = MarsRoverUI()
    app.mainloop()

