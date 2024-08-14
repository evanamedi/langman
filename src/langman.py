#!/usr/bin/env python3.12

from manager import Manager
from data_handler import DataHandler
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: langman <command> [options]")
		return

	command = sys.argv[1]

	if command == "remove":
		print("Remove command not yet implemented.")
		return

	print(f"Command received: {command}")

if __name__ == "__main__":
	main()