import os

from muraho.core.menu import confirm
from muraho.core.repo import GitHubRepo


class XsstrikeRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="s0md3v/XSStrike",
            install={"pip": "requirements.txt"},
            description="Advanced XSS Detection Suite",
        )

    def run(self):
        os.chdir(self.full_path)
        user_url = input("\nEnter a url to scan: ").strip()
        args = []
        if confirm("Do you want to crawl?"):
            args.append("--crawl")
        if confirm("Do you want to find hidden parameters?"):
            args.append("--p")
        args_str = " ".join(args)
        return os.system(f"python3 xsstrike.py -u {user_url} {args_str}")


xsstrike = XsstrikeRepo()
