# main.py
from menu import start_menu, MENU_ITEMS
from installer import (
    install_hyprland,
    install_shell_utility,
    install_drivers,
    install_work_apps,
    install_game_apps,
    install_system_utils,
    copy_dotfiles,
    update_system
)
from logger import Logger


def run_installer():
    update_system()

    while True:
        choice_index = start_menu()
        if choice_index is None:
            Logger.add_record("Меню прервано пользователем.")
            break

        item = MENU_ITEMS[choice_index]

        if item.startswith("Установить окружение"):
            install_hyprland()

        elif item.startswith("Установить оболочку"):
            install_shell_utility()

        elif item.startswith("Установить драйверы"):
            print("\nВыберите драйверы: [nvidia/amd/intel]")
            driver_type = input("> ").strip().lower()
            install_drivers(driver_type)

        elif item.startswith("Установить программы для работы"):
            install_work_apps()

        elif item.startswith("Установить программы для игр"):
            install_game_apps()

        elif item.startswith("Установить системные утилиты"):
            install_system_utils()

        elif item.startswith("Скопировать Dotfiles"):
            copy_dotfiles()

        elif item.startswith("Выход"):
            Logger.add_record("Завершение работы.")
            break

        input("\nНажмите Enter, чтобы вернуться в меню...")


if __name__ == '__main__':
    run_installer()
