import mediapipe as mp
mpdrawing=mp.solutions.drawing_utils
mpstyle=mp.solutions.drawing_styles
import cv2
videocapture=cv2.VideoCapture(0)
mpfacemesh=mp.solutions.face_mesh
with mpfacemesh.FaceMesh(max_num_faces=2,refine_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5) as facemesh:

    while videocapture.isOpened():
        success,image=videocapture.read()
        if not success:
            break

        results=facemesh.process(image)

        for face_landmarks in results.multi_face_landmarks:
            mpdrawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mpfacemesh.FACEMESH_TESSELATION,landmark_drawing_spec=None,connection_drawing_spec=mpstyle.get_default_face_mesh_tesselation_style())
            mpdrawing.draw_landmarks(image=image, landmark_list=face_landmarks,
                                     connections=mpfacemesh.FACEMESH_CONTOURS, landmark_drawing_spec=None,
                                     connection_drawing_spec=mpstyle.get_default_face_mesh_contours_style())


        cv2.imshow("video",cv2.flip(image,1))
        if cv2.waitKey(100)==ord('q'):
            break
    videocapture.release()
    cv2.destroyAllWindows()



