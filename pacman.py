# pacman.py

import os
from logger import Logger, LoggerStatus

def install_packages(package_names: list):
    for package in package_names:
        # Check if package is already installed
        check_installed = os.system(f"pacman -Q {package} > /dev/null 2>&1")
        if check_installed == 0:
            Logger.add_record(f"Package already installed: {package}")
            continue

        # Check in official repos
        pacman_check = os.system(f"pacman -Si {package} > /dev/null 2>&1")
        if pacman_check == 0:
            pacman_install = os.system(f"sudo pacman -S --noconfirm {package}")
            if pacman_install == 0:
                Logger.add_record(f"Installed via pacman: {package}")
            else:
                Logger.add_record(
                    f"Failed to install via pacman: {package}",
                    status=LoggerStatus.ERROR
                )
            continue

        # Check in AUR
        yay_check = os.system(f"yay -Si {package} > /dev/null 2>&1")
        if yay_check == 0:
            yay_install = os.system(f"yay -S --noconfirm {package}")
            if yay_install == 0:
                Logger.add_record(f"Installed via AUR: {package}")
            else:
                Logger.add_record(
                    f"Failed to install via AUR: {package}",
                    status=LoggerStatus.ERROR
                )
            continue

        # If not found anywhere
        Logger.add_record(f"Package not found in pacman or AUR: {package}", status=LoggerStatus.ERROR)
