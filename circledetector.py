import cv2
import numpy

def circle_detector(video_capture, windowname, minimum_radius, maximum_radius):
    while True:

        # FRAME = VIDEO READ
        ret, frame = video_capture.read() # setting frame and ret = vc.read() to allow for individual image processing

        # BLACK AND WHITE = IMAGE, BGR2GRAY
        bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts it to grayscale

        # BLUR = B&W, 3x3
        blur = cv2.blur(bw, (5, 5)) # blurs image

        #edge = cv2.Canny(blur, 50, 150)

        # DETECTED = BW.HOUGHCIRCLES
        detected = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=90, minRadius=minimum_radius, maxRadius=maximum_radius)  # detects circles

        # IF CIRCLES DETECTED IS NOT 0
        if detected is not None:  # makes sure that it detected at least one

            # CIRCLES = NUMPY DETECTED
            circles = numpy.uint16(numpy.around(detected))  # converts circles to x, y, and radius parameters

            # FOR PARAMETER IN CIRCLES
            for parameter in circles[0, :]:  # iterating through all circles' detected parameters

                # X = PARAM 0, Y = PARAM 1, R = PARAM 2
                x, y, r = parameter[0], parameter[1], parameter[2]  # setting x, y, and radius to the respective parameters

                # DRAW CIRCLE RADIUS = R
                cv2.circle(frame, (x, y), r, (150, 255, 0), 7)  # args: image, coordinates, radius, color, stroke

                # DRAW CIRCLE RADIUS = 1
                cv2.circle(frame, (x, y), 1, (0, 0, 255), 10)  # drawing a circle with a radius of 1 (dot) at same coordinates

                # IMSHOW WINDOW
                cv2.imshow(windowname, frame)  # creating window called circle that displays output image
                cv2.waitKey(15)

    video_capture.release()
    cv2.destroyWindow(windowname)