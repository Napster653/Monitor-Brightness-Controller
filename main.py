from typing import List

import monitorcontrol
import pystray
from PIL import Image


def set_brightness(brightness: int, monitors: List[monitorcontrol.Monitor]):
    """
    Sets the brightness of all monitors in the list to the desired value
    :param monitors: The list of monitors
    :param brightness: The desired value
    """
    print(f'set_brightness called with brightness={brightness}, monitors={monitors}')
    for monitor in monitors:
        with monitor:
            monitor.set_luminance(brightness)


def get_brightness(monitors: List[monitorcontrol.Monitor]):
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


def indirect_set_brightness_100(monitors: List[monitorcontrol.Monitor]):
    """
    Sets brightness to 100%
    :param monitors: The list of monitors
    :return: A callable to the function
    """

    def set_brightness_100():
        set_brightness(brightness=100, monitors=monitors)

    return set_brightness_100


def indirect_set_brightness_50(monitors: List[monitorcontrol.Monitor]):
    """
    Sets brightness to 100%
    :param monitors: The list of monitors
    :return: A callable to the function
    """

    def set_brightness_50():
        set_brightness(brightness=50, monitors=monitors)

    return set_brightness_50


def indirect_set_brightness_0(monitors: List[monitorcontrol.Monitor]):
    """
    Sets brightness to 100%
    :param monitors: The list of monitors
    :return: A callable to the function
    """

    def set_brightness_0():
        set_brightness(brightness=0, monitors=monitors)

    return set_brightness_0


def exit_program(icon: pystray.Icon):
    """
    Stops the menu and makes the program end
    :param icon: the pystray Icon
    """
    icon.stop()


def setup_menu(icon, monitors: List[monitorcontrol.Monitor]) -> pystray.Menu:
    menu = pystray.Menu(
        pystray.MenuItem(text=lambda text: get_brightness(monitors=monitors), action=None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Set brightness to 100%', action=indirect_set_brightness_100(monitors)),
        pystray.MenuItem(text='Set brightness to 50%', action=indirect_set_brightness_50(monitors)),
        pystray.MenuItem(text='Set brightness to 0%', action=indirect_set_brightness_0(monitors)),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(text='Exit', action=exit_program)
    )
    return menu


def main():
    monitors = monitorcontrol.get_monitors()
    icon = Image.open('icon.png')
    menu = setup_menu(icon=icon, monitors=monitors)
    icon = pystray.Icon(name='Monitor Brightness Controller', icon=icon, title='Monitor Brightness Controller v0.1',
                        menu=menu)
    icon.run()


if __name__ == '__main__':
    main()
