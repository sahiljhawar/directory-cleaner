from pathlib import Path
from time import sleep
import argparse

from watchdog.observers import Observer

from EventHandler import EventHandler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Monitor a directory and move files to another directory."
    )
    parser.add_argument(
        "-p",
        "--path",
        default="~/Downloads",
        type=str,
        help="The directory to monitor.",
    )
    args = parser.parse_args()

    watch_path = Path(args.path).expanduser().absolute()
    event_handler = EventHandler(watch_path=watch_path)

    print(f"Monitoring {Path(watch_path).absolute()}...")

    observer = Observer()
    observer.schedule(event_handler, f"{watch_path}", recursive=True)
    observer.start()

    try:
        while True:
            sleep(0.01)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
