# menu.py

import curses

MENU_ITEMS = [
    "Install Hyprland environment (Hyprland, Waybar, Rofi, Hyprpaper, etc.)",
    "Install shell (Fish) and utilities",
    "Install drivers (NVIDIA, AMD, Intel)",
    "Install work applications (browsers, messengers, office)",
    "Install game applications (Steam, etc.)",
    "Install system utilities (sound, Wi-Fi, Bluetooth, etc.)",
    "Copy Dotfiles and configure environment",
    "Exit"
]

def run_menu(stdscr):
    curses.curs_set(0)  # Hide cursor in TUI
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

def main(stdscr):
    # Init color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    choice = run_menu(stdscr)
    return choice

def start_menu():
    return curses.wrapper(main)
