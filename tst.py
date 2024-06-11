import curses

def draw_menu(stdscr):
    # Define colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    # Clear screen
    stdscr.clear()

    # Define the menu content
    menu = [
        "❤️ ❤️ ❤️ ",
        "🛡️  ",
        "⚔️ ⚔️ ⚔️ ⚔️ ",
        "",
        "BARBARIAN",
        "🪓 HERO POWER",
        "THROWING AXE",
        "",
        "[X] BUY",
        "[A] PLAY",
        "[Y] HELP",
        "[B] EXIT",
    ]

    # Display the menu
    for idx, row in enumerate(menu):
        if "❤️" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(1))
        elif "🛡️" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(2))
        elif "⚔️" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(3))
        elif "🪓" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(4))
        elif "[X]" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(5))
        elif "[A]" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(6))
        elif "[Y]" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(4))
        elif "[B]" in row:
            stdscr.addstr(idx, 0, row, curses.color_pair(1))
        else:
            stdscr.addstr(idx, 0, row)

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(draw_menu)
