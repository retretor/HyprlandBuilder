# installer.py

import os
from pacman import install_packages
from logger import Logger, LoggerStatus

# Packages for Hyprland environment
HYPRLAND_PACKAGES = [
    "hyprland",
    "waybar",
    "hyprpaper",
    "hyprlock",
    "hyprshot",
    "rofi-wayland",
    "ags-hyprpanel-git",
    "swww",
    "kitty",
    "fastfetch",
    "awesome-terminal-fonts",
    "otf-font-awesome",
    "ttf-font-awesome",
    "ttf-jetbrains-mono",
    "ttf-jetbrains-mono-nerd",
    "xdg-desktop-portal-hyprland-git",
    "wl-clipboard",
    "grim",
    "slurp",
    "mako"
]

# Packages for shell and utilities
SHELL_UTILITY_PACKAGES = [
    "fish",
    "starship",
    "git",
    "wget",
    "curl",
    "unzip",
    "zip",
    "p7zip",
    "htop",
    "rsync",
    "neovim",
    "lazygit",
    "thunar"
]

# Drivers
NVIDIA_PACKAGES = [
    "nvidia", "nvidia-utils", "nvidia-settings"
]
AMD_PACKAGES = [
    "xf86-video-amdgpu"
]
INTEL_PACKAGES = [
    "xf86-video-intel"
]

# Work apps
WORK_APPS = [
    "firefox",
    "telegram-desktop",
    "discord",
    "libreoffice-still"
]

# Game apps
GAME_APPS = [
    "steam",
]

# System utils
SYSTEM_UTILS = [
    "networkmanager",
    "network-manager-applet",
    "pipewire",
    "pipewire-alsa",
    "pipewire-pulse",
    "wireplumber",
    "bluez",
    "bluez-utils",
    "alsa-utils",
    "pavucontrol",
    "iw",
    "wpa_supplicant",
    "dialog",
    "openbsd-netcat",
    "dnsutils",
    "bash-completion",
    "polkit-gnome"
]

def update_system():
    os.system("clear")
    Logger.add_record("Updating system...")
    # Full system update
    os.system("sudo pacman -Syu --noconfirm")
    Logger.add_record("System updated successfully.")

    Logger.add_record("Installing 'yay' for AUR support...")
    os.system("sudo pacman -S --needed base-devel git --noconfirm")
    if not os.path.exists("yay"):
        os.system("git clone https://aur.archlinux.org/yay.git")
    os.system("cd yay && makepkg -si --noconfirm")
    Logger.add_record("yay installed successfully.")

def install_hyprland():
    os.system("clear")
    Logger.add_record("Installing Hyprland environment...")
    install_packages(HYPRLAND_PACKAGES)
    Logger.add_record("Hyprland environment installation done.")

def install_shell_utility():
    os.system("clear")
    Logger.add_record("Installing shell (Fish) and utilities...")
    install_packages(SHELL_UTILITY_PACKAGES)
    Logger.add_record("Shell and utilities installed.")

def install_drivers(driver_type: str):
    os.system("clear")
    Logger.add_record(f"Installing drivers for: {driver_type}")

    if driver_type == "nvidia":
        install_packages(NVIDIA_PACKAGES)
    elif driver_type == "amd":
        install_packages(AMD_PACKAGES)
    elif driver_type == "intel":
        install_packages(INTEL_PACKAGES)
    else:
        Logger.add_record(f"Unknown driver type: {driver_type}", status=LoggerStatus.ERROR)
        return

    Logger.add_record(f"Drivers for {driver_type} installed.")

def install_work_apps():
    os.system("clear")
    Logger.add_record("Installing work applications...")
    install_packages(WORK_APPS)
    Logger.add_record("Work applications installed.")

def install_game_apps():
    os.system("clear")
    Logger.add_record("Installing game applications...")
    install_packages(GAME_APPS)
    Logger.add_record("Game applications installed.")

def install_system_utils():
    os.system("clear")
    Logger.add_record("Installing system utilities (sound, Wi-Fi, Bluetooth, etc.)...")
    install_packages(SYSTEM_UTILS)
    Logger.add_record("System utilities installed.")

def copy_dotfiles():
    os.system("clear")
    Logger.add_record("Copying Dotfiles...")

    home = os.path.expanduser("~")
    dotfiles_dir = os.path.join(os.getcwd(), "Dotfiles")

    # Example: copy Dotfiles/.config/* to ~/.config/
    # You can adjust logic as needed
    rsync_cmd = f'rsync -av --exclude ".git" "{dotfiles_dir}/" "{home}/.config/"'
    os.system(rsync_cmd)

    Logger.add_record("Dotfiles copied. Please verify your configs.")
