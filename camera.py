from flask import Flask, render_template, Response,redirect
from pyzbar.pyzbar import decode
import cv2
import winsound
import sys
found = False
app = Flask(__name__)
camera = cv2.VideoCapture(0)


def hello():
    print('hello')
    redirect("http:/127.0.0.1/found.html")

def generate_frames():

    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            for code in decode(frame):
                print(code.data.decode('utf-8'))
                if str(code.data.decode('utf-8')) == '3082025c02010002818100a04cc053afdcbf36b09f2347292d75ee5ae0bb03f788fe6b8433d734bc7820f22520b8d3311c3e963b55ccef2a1aab53f931a8bb4217e6263bce317cda9c62a4583aa2a7f28fce26b32665c56adac5fe46cec8478029465bf12b9986bc4c914705113315f431e8062c268a9927eee4fec5c9a9a60979506c4a2303840142e4cb02030100010281801052cb2c4fcbe930d6dad8607bb74f10b447b98e4031141a10bea805e26ca7e0e09a576d3222ba80d9394b2d78efcef88b2207c3a1df05d1be39fe076fca33052339967ad38db086769bdc4cfcebaf724421712a80cab062823ef10e35150b92fa321ffb8b6bfe9e51ad4ee1b9dabbc282e9f7fd4144f333de416f900bf8b479024100baef8b7065f559ae1786f8f67dd1d731deeac1e25337c6c2387255c1f4d83559895feb1081825fecc7dd2fc9737f988d2165ec5b837413c03a7c6d30cf4f49d7024100db85f8adf6e420d0c424ce25409b9164f743d61066f62218f309ec74cb37855e3b316f2fbaffa6988e40eb73a6cfedc3423224ddd72b424ada51adb4b5eb262d024042c105ef36499e23bffd0fec9dd390601bb58354f9d8a21e7b1fc12608f42860f7e08bc59229e76d5b95cdd9c767da2713b51ce93510ff7896aa1627e6efee7302410092d1ef98aa5fb972e73c968363caa85b96e4cfeef86df630299ca1811bc96e71afb5485febf9c03a9829e34fde6982e3ed0a0c8e32b2c40bbc2894bd204ebda102404e0160fb1aaf929d81a34d8be394e842a53ed949d7d61fa2ab1e6ba093c55b58ccec2587fd5b46e75c64a8f8a2b4320bc6536084bcb3829b58961c5363adcb7d':
                    winsound.Beep(400, 500)
                    #found = True
                    #return redirect('https://www.google.com/')
                    #return (found)
                    #hello()


                    print(found)




            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()


        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/found')
def found():
     return redirect('found.html')

@app.route('/main')
def index():

    return render_template('main.html')


@app.route('/video')
def video():
    if found == True:
         return redirect('/found')
    else:
         return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(debug=True)



