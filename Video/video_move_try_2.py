import cv2
import from robomaster
from robomaster import robot

def main():
    # 드론 초기화
    tl_drone = robot.Drone()
    tl_drone.initialize()

    # 드론 비행 객체 설정
    tl_flight = tl_drone.flight

    # 드론 카메라 설정
    tl_camera = tl_drone.camera
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)

    try:
        # 이륙
        tl_flight.takeoff().wait_for_completed()

        # 전진 50cm
        tl_flight.forward(distance=50).wait_for_completed()

        # 후진 50cm
        tl_flight.backward(distance=50).wait_for_completed()

        # 착륙
        tl_flight.land().wait_for_completed()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # 비디오 스트림 중지 및 종료
        tl_camera.stop_video_stream()
        cv2.destroyAllWindows()

        # 드론 연결 종료
        tl_drone.close()

if __name__ == '__main__':
    main()
