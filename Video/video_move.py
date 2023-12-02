import cv2
import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR = "192.168.10.3"

if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_flight = tl_drone.flight
    tl_camera = tl_drone.camera

    # 비행 시작
    tl_flight.takeoff().wait_for_completed()

    # 비디오 스트림 시작
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)

    # 전진 후진 수행
    tl_flight.forward(distance=50).wait_for_completed()
    tl_flight.backward(distance=50).wait_for_completed()

    # 착륙
    tl_flight.land().wait_for_completed()

    # 비디오 스트림 종료
    tl_camera.stop_video_stream()

    # 영상 스트림 확인 및 종료
    for _ in range(302):
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone Video Stream", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

    tl_drone.close()  # 드론 연결 종료
