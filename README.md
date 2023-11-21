# Cleaner

Python script to help you clean your directory by rearranging the files in sub-directories as per the file kind

## How to use:

First clone the repository to your local machine:
`git clone git@github.com:sahiljhawar/directory-cleaner.git`

and install `watchdog` using  `pip install watchdog`

To see it in action, run the following command in the directory where you cloned the repository:

`python cleaner.py -p <absolute path to directory>`

if `-p` is not set then the program defaults to `~/Downloads`

## Example:

`python cleaner.py -p ~/Desktop`

This will rearrange all the files in the Desktop directory into sub-directories as per the file types defined in `extensions.py`

After executing the command, for the `watchdog` to get triggered perform some operation in the directory such as renaming a file, creating a new directory, etc.

## Features:

You can add more extensions/filetype by appending to the `extensions.py` file.

> [!WARNING]
> The scripts moves (cuts and pastes) the file. Make sure you have a backup of the files before running the script. However, you can change the script to copy the files instead of moving them.
