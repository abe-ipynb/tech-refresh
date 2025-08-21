#!/usr/bin/env python3
# cli-tdl.py - A simple command-line todo list application

import sys
import os

DB_FILE = "db.txt"

def read_todos():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def write_todos(todos):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        for item in todos:
            f.write(item + "\n")

def add_todo(item):
    todos = read_todos()
    todos.append(item)
    write_todos(todos)
    print(f"Added: {item}")

def view_todos():
    todos = read_todos()
    if not todos:
        print("No todos found.")
    else:
        for idx, item in enumerate(todos, 1):
            print(f"{idx}. {item}")

def delete_todo(index_str):
    try:
        index = int(index_str)
    except ValueError:
        print("Please provide a valid number for delete.")
        return
    todos = read_todos()
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        write_todos(todos)
        print(f"Deleted: {removed}")
    else:
        print("No todo at that number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: add <item> | view | delete <number>")
        return
    action = sys.argv[1]
    if action == "add":
        if len(sys.argv) < 3:
            print("Please provide a todo item to add.")
        else:
            add_todo(" ".join(sys.argv[2:]))
    elif action == "view":
        view_todos()
    elif action == "delete":
        if len(sys.argv) < 3:
            print("Please provide the number of the todo to delete.")
        else:
            delete_todo(sys.argv[2])
    else:
        print("Unknown command. Use add, view, or delete.")

if __name__ == "__main__":
    main()
