# main.py

import os
from menu import start_menu, MENU_ITEMS
from installer import (
    update_system,
    install_hyprland,
    install_shell_utility,
    install_drivers,
    install_work_apps,
    install_game_apps,
    install_system_utils,
    copy_dotfiles
)
from logger import Logger

def run_installer():
    os.system("clear")

    # Ask for sudo password once at the beginning
    print("Please enter your sudo password (you will not be asked again for a while):")
    os.system("sudo -v")  # This will cache sudo credentials

    # Update system and install 'yay'
    update_system()

    while True:
        choice_index = start_menu()
        if choice_index is None:
            Logger.add_record("Menu interrupted by user.")
            break

        item = MENU_ITEMS[choice_index]

        if item.startswith("Install Hyprland environment"):
            install_hyprland()

        elif item.startswith("Install shell"):
            install_shell_utility()

        elif item.startswith("Install drivers"):
            print("\nChoose drivers: [nvidia / amd / intel]")
            driver_type = input("> ").strip().lower()
            install_drivers(driver_type)

        elif item.startswith("Install work applications"):
            install_work_apps()

        elif item.startswith("Install game applications"):
            install_game_apps()

        elif item.startswith("Install system utilities"):
            install_system_utils()

        elif item.startswith("Copy Dotfiles"):
            copy_dotfiles()

        elif item.startswith("Exit"):
            Logger.add_record("Exiting.")
            break

        # Wait for user input before returning to menu
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    run_installer()
