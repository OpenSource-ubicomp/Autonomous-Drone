import cv2
import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR = "192.168.10.3"

if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_camera = tl_drone.camera
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)
    for i in range(0, 302):
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()

    tl_drone.close()
