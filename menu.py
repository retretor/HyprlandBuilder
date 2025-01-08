# menu.py
import curses

MENU_ITEMS = [
    "Установить окружение (Hyprland, Waybar, Rofi, Hyprpaper...)",
    "Установить оболочку Fish и утилиты",
    "Установить драйверы (NVIDIA, AMD, Intel)",
    "Установить программы для работы (браузеры, мессенджеры, офис)",
    "Установить программы для игр",
    "Установить системные утилиты (звук, Wi-Fi, Bluetooth и т.д.)",
    "Скопировать Dotfiles и настроить окружение",
    "Выход"
]

def run_menu(stdscr):
    curses.curs_set(0)  # Скрываем курсор в TUI
    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        title = " Post-Install Setup Menu (Arch + Hyprland) "
        stdscr.addstr(0, (width // 2) - (len(title) // 2), title, curses.A_BOLD)

        for idx, item in enumerate(MENU_ITEMS):
            x = 2 + idx
            y = 2
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(x, y, f"> {item}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(x, y, f"  {item}")

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(MENU_ITEMS) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            return current_row

def start_menu():
    curses.wrapper(main)

def main(stdscr):
    # Настраиваем цветовые пары
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    choice = run_menu(stdscr)
    return choice
