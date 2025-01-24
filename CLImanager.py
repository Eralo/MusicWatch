import cmd2


class CLIManager(cmd2.Cmd):
    intro = "Welcome to MusicWatch CLI. Please use 'help' or '?' t odisplay all available commands."
    prompt = "(MusicWatch) > "

    def __init__(self, player, retriever, offline_media, visualizer):
        super().__init__()
        
        self.player = player
        self.retriever = retriever
        self.offline_media = offline_media
        self.visualizer = visualizer

    def do_add(self, arg):
        """Add media to queue. Usage: add <media>"""
        if not arg.strip():
            self.poutput("Error: Please provide a media.")
            return
        media_info = self.retriever.retrieve_info(arg.strip())
        self.player.add_to_queue(media_info)
        self.poutput(f"Added to queue : {media_info['full_title']}")

    def do_play(self, arg):
        """Start playing all queued musics. Usage: play"""
        if self.player.queue:
            self.poutput("Playing  :")
            self.poutput(self.player.queue.pop(0))
        else:
            self.poutput("Queue is empty.")

    def do_download(self, arg):
        """Download media without playing it. Usage: download <media_link>"""
        if not arg.strip():
            self.poutput("Error: please provide a media.")
            return
        file_path = self.offline_media.check_and_download(arg.strip())
        self.poutput(f" Downloaded at : {file_path}")

    def do_exit(self, arg):
        """Quit program shell. Usage: exit"""
        return True

    def do_queue(self, arg):
        """Display the current queue. Usage: queue"""
        if self.player.queue:
            self.poutput("Queue :")
            for index, media in enumerate(self.player.queue, start=1):
                self.poutput(f"{index}. {media['full_title']} - {media['artist']}")
        else:
            self.poutput("Queue is empty.")
