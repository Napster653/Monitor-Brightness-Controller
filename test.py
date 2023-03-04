import time

import monitorcontrol

monitors = monitorcontrol.get_monitors()
for monitor in monitors:
    with monitor:
        print('off')
        monitor.set_power_mode(5)
        time.sleep(5)
        print('off')
        monitor.set_power_mode(1)
        time.sleep(5)

        exit()
