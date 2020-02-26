from cv2 import cv2
import time,os
from flask import Flask
app = Flask(__name__)

@app.route('/frame',methods= ['POST','GET'])
def frame():

    cap = cv2.VideoCapture(0)
    i = 0
    while True:
        i = i+1
        print(time)
        _,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("BGR_SCALE",frame)
        cv2.imshow("GRAY_SCALE",gray)
        cv2.imwrite('Images/{}.png'.format(i),gray)

        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    count = len(os.listdir("images"))

    return "Total No Image saved are {}".format(count)

if __name__ == "__main__":
    app.run(debug=True,port=8001)