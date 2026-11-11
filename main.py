# ==============================================================================
# PROJECT    : Royal To-Do CLI (Python Task Manager)
# AUTHOR     : Zakaria
# GITHUB     : github.com/j0jj
# Instagram  : @jddb
# DATE       : 2026
# DESCRIPTION: A lightweight CLI task manager using Python & JSON persistence.
# ==============================================================================

import json # Library for handling data persistence in JSON format
import os # Library for interacting with the operating system (e.g., file paths)

FIlE_PATH = "tasks.json" # Path to the JSON file where tasks will be stored

# --- ANSI COLOR CODES FOR TERMINAL DESIGN ---
GOLD = "\033[93m"
RESET = "\033[0m"
def clear_screen():
    """Clears the terminal screen for a fresh interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_msg(text, msg_type="info"):
    """Unified print function with bracket-only coloring, keeping symbols and text uncolored."""
    if msg_type == "success":
        print(f"{GOLD}[{RESET}✓{GOLD}]{RESET} {text}") # Output : Success message with a checkmark
    elif msg_type == "error":
        print(f"{GOLD}[{RESET}✗{GOLD}]{RESET} Error: {text}") # Output : Error message with a cross
    elif msg_type == "warning":
        print(f"{GOLD}[{RESET}!{GOLD}]{RESET} {text}") # Output : Warning message with an exclamation mark
    elif msg_type == "header":
        print(f"\n{GOLD}===================================={RESET}")
        print(f"{GOLD}        {RESET}{text}{GOLD}         {RESET}")
        print(f"{GOLD}===================================={RESET}")
    else:
        print(text) # Output : Default message without any special formatting
def load_tasks():
    """Reads tasks from tasks.json if it exists and informs the user."""
    if os.path.exists(FIlE_PATH):
        with open(FIlE_PATH, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            print_msg(f"Loaded {len(tasks)} tasks from '{FIlE_PATH}'", "success")
            return tasks
    print_msg(f"No existing '{FIlE_PATH}' found. Starting fresh.", "warning")
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FIlE_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4) # Output : Saves the list of tasks to the JSON file with indentation for readability
    print_msg(f"Changes saved successfully to '{FIlE_PATH}'", "success")

def main():
    """Main function to run the task manager."""
    clear_screen()
    tasks = load_tasks() # Fetch saved data upon script execution
    print_msg("ROYAL TO-DO CLI - INITIALIZING", "header")
    tasks = load_tasks()
    input(f"\n{GOLD}➔{RESET} Press Enter to start...")
    while True:
        clear_screen() # Clear the terminal screen for a fresh interface

        # --- UI DISPLAY ---
        print_msg("Royal To-Do CLI", "header")
        print(f" {GOLD}[{RESET}1{GOLD}]{RESET} View Tasks")
        print(f" {GOLD}[{RESET}2{GOLD}]{RESET} Add Task")
        print(f" {GOLD}[{RESET}3{GOLD}]{RESET} Delete Task")
        print(f" {GOLD}[{RESET}4{GOLD}]{RESET} Exit")

        choice = input(f"\n ➔ Select Option (1-4) > ").strip()

        if choice == "1":
            clear_screen() # Clear the screen before displaying tasks
            if not tasks:
                print_msg("No tasks found in storage.", "warning") # Output : Informative message for empty list
            else:
                print(f"\n--- TASK LIST ---")
                for index, task in enumerate(tasks, 1):
                    status = f"{GOLD}[{RESET}✓{GOLD}]{RESET}" if task["completed"] else f"{GOLD}[{RESET} {GOLD}]{RESET}"
                    print(f" {index}. {status} {task['title']}")
            input(f"\n{GOLD}➔{RESET} Press Enter to return to menu...")
        elif choice == "2":
            clear_screen() # Clear the screen before adding a new task
            title = input(f"\n ➔ Enter task title > ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print_msg("Task added successfully!", "success")
            else:
                print_msg("Title cannot be empty.", "error")
            input(f"\n{GOLD}➔{RESET} Press Enter to return to menu...")
        elif choice == "3":
            clear_screen() # Clear the screen before displaying tasks for deletion
            if not tasks:
                print_msg("No tasks available to delete.", "warning")
                input(f"\n{GOLD}➔{RESET} Press Enter to return to menu...")
            else:
                print(f"\n--- CURRENT TASKS ---")
                for index, task in enumerate(tasks, 1):
                    print(f" {index}. {task['title']}")
                try:
                    task_num = int(input(f"\n ➔ Enter task number to delete > "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print_msg(f"Deleted: '{removed['title']}'", "success")
                    else:
                        print_msg("Invalid task number.", "error")
                except ValueError:
                    print_msg("Please enter a valid number.", "error")
                input(f"\n{GOLD}➔{RESET} Press Enter to return to menu...")
        elif choice == "4":
            clear_screen() # Clear the screen before displaying the exit message
            print_msg("Session closed successfully - Made by Zakariya", "header")
            input(f"\n{GOLD}➔{RESET} Press Enter to exit...")
            break
        else:
            print_msg("Invalid option. Please select a number between 1 and 4.", "error")
            input(f"\n{GOLD}➔{RESET} Press Enter to continue...")

if __name__ == "__main__":
    main() # Start the task manager application