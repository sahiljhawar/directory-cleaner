import os
import shutil

from pathlib import Path

from watchdog.events import FileSystemEventHandler

from extensions import extension_paths


class EventHandler(FileSystemEventHandler):
    def __init__(self, watch_path: Path):
        self.watch_path = watch_path.resolve()

    def on_modified(self, event):
        redun = self.watch_path / "Redundant Files"
        for child in self.watch_path.iterdir():
            # skips directories and non-specified extensions
            if child.is_file() and child.suffix.lower() in extension_paths:
                destination_path = (
                    f"{str(self.watch_path)}/{extension_paths[child.suffix.lower()]}"
                )
                if os.path.basename(child) not in os.listdir(destination_path):
                    shutil.move(src=str(child), dst=str(destination_path))
                    print(f"{os.path.basename(child)} moved to {str(destination_path)}")
                else:
                    shutil.move(src=str(child), dst=str(redun))
                    print(f"{os.path.basename(child)} moved to {str(redun)}")
