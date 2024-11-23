"""
Monitor Brightness Controller
"""
from typing import List

import monitorcontrol
import pkg_resources
import pystray
from PIL import Image


def set_brightness(brightness: int, monitors: List[monitorcontrol.Monitor]) -> None:
    """
    Sets the brightness of all monitors in the list to the desired value
    :param monitors: The list of monitors
    :param brightness: The desired value
    """
    print(f'set_brightness called with brightness={brightness}, monitors={monitors}')
    for monitor in monitors:
        with monitor:
            monitor.set_luminance(brightness)


def get_brightness(monitors: List[monitorcontrol.Monitor]) -> str:
    """
    Returns the brightness of the first monitor.
    It is assumed that all monitors will have the same value.
    :param monitors: The list of monitors
    :return: The brightness of the first monitor in the list
    """
    print(f'get_brightness called with monitors={monitors}')
    for monitor in monitors:
        with monitor:
            brightness = monitor.get_luminance()
            return f'Brightness at {brightness}%'


def exit_program(icon: pystray.Icon) -> None:
    """
    Stops the menu and makes the program end
    :param icon: the pystray Icon
    """
    icon.stop()


def setup_menu(monitors: List[monitorcontrol.Monitor]) -> pystray.Menu:
    """
    Sets up the menu with the desired options
    :param monitors: The list of monitors
    :return: The menu
    """
    menu = pystray.Menu(
        pystray.MenuItem(text=lambda text: get_brightness(monitors=monitors), action=None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Set brightness to 100%', action=lambda: set_brightness(100, monitors)),
        pystray.MenuItem(text='Set brightness to 75%', action=lambda: set_brightness(75, monitors)),
        pystray.MenuItem(text='Set brightness to 50%', action=lambda: set_brightness(50, monitors)),
        pystray.MenuItem(text='Set brightness to 25%', action=lambda: set_brightness(25, monitors)),
        pystray.MenuItem(text='Set brightness to 0%', action=lambda: set_brightness(0, monitors)),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Exit', action=exit_program),
    )
    return menu


def main() -> None:
    """
    Main function
    """
    monitors = monitorcontrol.get_monitors()
    icon = Image.open(pkg_resources.resource_filename(__name__, 'icon.png'))
    menu = setup_menu(monitors=monitors)
    icon = pystray.Icon(name='Monitor Brightness Controller', icon=icon, title='Monitor Brightness Controller v0.2', menu=menu)
    icon.run()


if __name__ == '__main__':
    main()
