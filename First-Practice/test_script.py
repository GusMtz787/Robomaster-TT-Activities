import robomaster
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_flight = tl_drone.flight

    # Set the QUAV to takeoff
    tl_flight.takeoff().wait_for_completed()

    # Make the QUAV execute movements
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()

    # Set the QUAV to land
    tl_flight.land().wait_for_completed()

    # Close resources
    tl_drone.close()