from gpiozero import Button
from signal import pause

def touched():
    print("Touched!")
    
def not_touched():
    print("Not Touched!")

# initialize a Button object for the touch sensor;
# GPIO 17: the pin connected to the sensor;
# pull_up=None; disables internal pull-up/pull-down resistors;
# active_state= True; high voltage is considered the active state
touch_sensor = Button(17, pull_up=None, active_state=True) 

#Assign functions to sensor events
touch_sensor.when_pressed = touched
touch_sensor.when_released = not_touched

pause()