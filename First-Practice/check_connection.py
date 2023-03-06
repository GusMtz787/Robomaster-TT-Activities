import robomaster
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    # 获取飞机版本信息
    drone_version = tl_drone.get_sdk_version()
    print("Drone sdk version: {0}".format(drone_version))

    tl_drone.close()