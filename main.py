import youtube
import youtube_dl
import sys

from player import Player
from retriever import Retriever
from offlineMedia import OfflineMedia
from display import Display
from visualizer import Visualizer
from CLImanager import CLIManager

### Simplifying functions
def is_running_in_terminal():
    """Detects TTY execution"""
    return sys.stdout.isatty()

def start_cli_mode():
    """Starts CLI interface"""
    CLIManager(player, retriever, offline_media, visualizer).cmdloop()

def start_tkinter_mode():
    """start TK GUI"""
    Display(player, retriever, offline_media, visualizer).run()
#########################



if __name__ == "__main__":

    player = Player()
    retriever = Retriever()
    offline_media = OfflineMedia()
    visualizer = Visualizer()
    
    # Check arguments
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == "--cli":
            start_cli_mode()
        elif mode == "--gui":
            start_tkinter_mode()
        else:
            print("Usage : python main.py [--cli | --gui]")
            sys.exit(5)
    else:
        #automatic running mode
        if is_running_in_terminal():
            start_cli_mode()
        else:
            start_tkinter_mode()
