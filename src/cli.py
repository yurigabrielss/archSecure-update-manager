import argparse
from .updater import run_yay_updates
from .parser import parse_updates

def main():
    parser = argparse.ArgumentParser(description="ArchSecure Update Manager")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("check", help="Check for available updates")
    sub.add_parser("upgrade", help="Upgrade packages (not implemented yet)")

    args = parser.parse_args()

    if args.command == "check":
        text = run_yay_updates()
        pkgs = parse_updates(text)
        print(pkgs)
    elif args.command == "upgrade":
        print("Upgrade não implementado ainda.")
    else:
        parser.print_help()
