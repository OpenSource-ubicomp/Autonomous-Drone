import cv2
import robomaster
from robomaster import robot



if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_camera = tl_drone.camera
    tl_camera.start_video_stream(display=False)  # 비디오 스트림 시작
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)

    while True:
        img = tl_camera.read_cv2_image()  # 비디오 프레임 읽어오기
        cv2.imshow("Drone Video Stream", img)  # 영상 화면에 표시

        # 키보드 입력을 기다리고 'q'를 누르면 비디오 스트림 종료
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()  # 모든 창 닫기
    tl_camera.stop_video_stream()  # 비디오 스트림 중지

    tl_drone.close()  # 드론 연결 종료
