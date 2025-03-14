import time

from pynput import keyboard
from decoratorOperations import throttle

class DashdancingService:
    DIRECTION_HOLD_DELAY   = 0.050
    DIRECTION_CHANGE_DELAY = 0.025

    DANCE_START_DELAY = 1
    DANCE_LOOP_TIME   = 10

    def __init__(self, activator_key):
        self.rules = []

        self.keyboard_ctrl = keyboard.Controller()
        self.activator_key = activator_key
        self.listener = None


    # Only dashdance for 'DANCE_LOOP_TIME' seconds at a time (including 1 second
    # starting delay), otherwise ignore the signal (via the throttle)
    @throttle(1)
    def _dashdance(self):
        print('Initiating dance ritual...')

        # Pause for 1 second before dancing
        time.sleep(self.DANCE_START_DELAY)

        start_time = time.time()
        end_time   = start_time + self.DANCE_LOOP_TIME

        while time.time() < end_time:
            # Go to the left
            self.keyboard_ctrl.press('a')
            time.sleep(self.DIRECTION_HOLD_DELAY)
            self.keyboard_ctrl.release('a')

            # Wait for some time before changing direction
            time.sleep(self.DIRECTION_CHANGE_DELAY)

            # Go to the right
            self.keyboard_ctrl.press('d')
            time.sleep(self.DIRECTION_HOLD_DELAY)
            self.keyboard_ctrl.release('d')

            # Wait for some time before changing direction
            time.sleep(self.DIRECTION_CHANGE_DELAY)


    def start(self):
        if self.listener is None or not self.listener.running:
            # NOTE: When a thread is started and stopped, a new one must be instantiated
            self.listener = keyboard.GlobalHotKeys({
                self.activator_key: self._dashdance
            })

            self.listener.start()
            self.listener.wait()
            print(f'Listener started! Press "{self.activator_key}" to start dashdancing. Press Ctrl+C to stop this service.')


    def stop(self):
        if self.listener is not None and self.listener.running:
            self.listener.stop()

        self.listener = None
        print('Listener stopped!')


if __name__ == '__main__':
    service = DashdancingService(
        activator_key='<ctrl>+2'
    )

    service.start()
    running = True

    while running:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            running = False

    service.stop()
