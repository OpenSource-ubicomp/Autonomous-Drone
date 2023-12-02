import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR = "192.168.10.3"

if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_flight = tl_drone.flight

    tl_flight.takeoff().wait_for_completed()

    tl_flight.forward(distance=50).wait_for_completed()
    tl_flight.backward(distance=50).wait_for_completed()

    tl_flight.land().wait_for_completed()

    tl_drone.close()
