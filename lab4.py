import cv2

mode = int(input('mode:'))  # Считываем номер преобразования.

if (mode == 0): # Подключение к веб-камере
    capture = cv2.VideoCapture(0)
    while (capture.isOpened()):
        ret, frame = capture.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('x'):
            break
    capture.release()
    cv2.destroyAllWindows()

if (mode == 1): # Использование фильтров
    capture = cv2.VideoCapture(0)
    while (capture.isOpened()):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray1', gray)
        cv2.imshow('gray2', gray)
        cv2.imshow('gray3', gray)
        cv2.imshow('gray4', gray)
        cv2.imshow('gray5', gray)

        if cv2.waitKey(1) == ord('x'):
            break
    capture.release()
    cv2.destroyAllWindows()

if (mode == 2): # Сохранение видео
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while (capture.isOpened()):
        ret, frame = capture.read()
        cv2.imshow('frame', frame)
        out.write(frame)

        if cv2.waitKey(1) == ord('x'):
            break

    capture.release()
    out.release()
    cv2.destroyAllWindows()

if (mode == 3):  # Чтение видео
    cap = cv2.VideoCapture('output.avi')
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        cv2.imshow('app', frame)
        if cv2.waitKey(1) == ord('x'):
            break
    cap.release()
    cv2.destroyAllWindows()

if (mode == 4): # Числовой анализ видеопотока
    video = cv2.VideoCapture(0)
    a = 0

    while True:
        a = a + 1  # miliseconds
        check, frame = video.read()
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('MyCam', gray)
        if cv2.waitKey(1) == ord('x'):
            break

    print(a)
    video.release()
    cv2.destroyAllWindows()

