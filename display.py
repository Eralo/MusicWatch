import tkinter as tk

class Display:

    def __init__(self, player, retriever, offline_media, visualizer):
        self.player = player
        self.retriever = retriever
        self.offline_media = offline_media
        self.visualizer = visualizer

        self.root = tk.Tk()
        self.root.title("MusicWatch")
        self._setup_ui()

    def _setup_ui(self):
        self.label = tk.Label(self.root, text="MusicWatch GUI placeholder")
        self.label.pack()
        
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        self.load_button = tk.Button(self.root, text="Load media", command=self.load_media)
        self.load_button.pack()
        
        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.quit_button.pack()

    def load_media(self):
        link = self.entry.get()
        print(f"Entered : {link}")
        # Here add loading logic

    def run(self):
        self.root.mainloop()
