# installer.py
import os
from pacman import install_packages
from logger import Logger, LoggerStatus

# --- Пакеты для Hyprland и окружения ---
HYPRLAND_PACKAGES = [
    # Hyprland
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

    # Шрифты и иконки
    "awesome-terminal-fonts",
    "otf-font-awesome",
    "ttf-font-awesome",
    "ttf-jetbrains-mono",
    "ttf-jetbrains-mono-nerd",

    "xdg-desktop-portal-hyprland-git",
    "wl-clipboard",
    "grim",  # скриншоты
    "slurp",  # выбор области
    "mako",  # уведомления
]

# --- Пакеты для shell и утилит ---
SHELL_UTILITY_PACKAGES = [
    "fish",  # оставим оба, на выбор
    "starship",  # приятная подсветка для shell
    "git",
    "wget",
    "curl",
    "unzip",
    "zip",
    "p7zip",
    "htop",
    "rsync",
    "neovim",  # или nano/vim - на ваш выбор
    "lazygit",
    "thunar"
]

# --- Драйверы ---
NVIDIA_PACKAGES = [
    "nvidia", "nvidia-utils", "nvidia-settings"  # для новых карт
]
AMD_PACKAGES = [
    "xf86-video-amdgpu"  # свободный драйвер
]
INTEL_PACKAGES = [
    "xf86-video-intel"  # иногда люди ставят, иногда нет
]

# --- Программы для работы ---
WORK_APPS = [
    "firefox",
    "telegram-desktop",
    "discord",
    "libreoffice-still"
]

# --- Программы для игр ---
GAME_APPS = [
    "steam",
]

# --- Системные утилиты (звук, wifi, bluetooth...) ---
SYSTEM_UTILS = [
    "networkmanager",
    "network-manager-applet",
    "pipewire",
    "pipewire-alsa",
    "pipewire-pulse",
    "wireplumber",
    "bluez",  # Bluetooth
    "bluez-utils",
    "alsa-utils",
    "pavucontrol",  # GUI для звука
    "iw", "wpa_supplicant",  # Wi-Fi
    "dialog",
    "openbsd-netcat",
    "dnsutils",
    "bash-completion",
    "polkit-gnome"
]


def update_system():
    Logger.add_record("[+] Updating Pacman DataBase")
    os.system("sudo pacman -Syu --noconfirm")
    Logger.add_record("[+] System updated.")

    Logger.add_record("[+] Installing yay")
    os.system("sudo pacman -S --needed base-devel git --noconfirm")
    os.system("git clone https://aur.archlinux.org/yay.git")
    os.system("cd yay && makepkg -si --noconfirm")
    Logger.add_record("[+] Done")


def install_hyprland():
    install_packages(HYPRLAND_PACKAGES)


def install_shell_utility():
    install_packages(SHELL_UTILITY_PACKAGES)


def install_drivers(driver_type: str):
    if driver_type == "nvidia":
        install_packages(NVIDIA_PACKAGES)
    elif driver_type == "amd":
        install_packages(AMD_PACKAGES)
    elif driver_type == "intel":
        install_packages(INTEL_PACKAGES)
    else:
        Logger.add_record(f"Неизвестный драйвер: {driver_type}", status=LoggerStatus.ERROR)


def install_work_apps():
    install_packages(WORK_APPS)


def install_game_apps():
    install_packages(GAME_APPS)


def install_system_utils():
    install_packages(SYSTEM_UTILS)


def copy_dotfiles():
    """
    Допустим, у вас dotfiles лежат в папке Dotfiles:
    Dotfiles/
      ├── .config
      │   └── waybar
      ├── .zshrc
      ├── .config
      │   └── fish
      ...

    Можно рекурсивно скопировать .config и другие файлы в $HOME.
    """
    Logger.add_record("[+] Copying dotfiles from Dotfiles/")
    home = os.path.expanduser("~")
    dotfiles_dir = os.path.join(os.getcwd(), "Dotfiles")

    # Простейший вариант: скопировать всё содержимое Dotfiles в HOME.
    # Можно использовать rsync, если он установлен:
    rsync_cmd = f'rsync -av --exclude ".git" "{dotfiles_dir}/" "{home}/.config/"'
    os.system(rsync_cmd)

    Logger.add_record("[+] Dotfiles copied. Please check your configs and reload shell.")
