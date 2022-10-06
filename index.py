from flask import Flask, request, send_file
import pytube
app = Flask(__name__)


@app.route('/download', methods=['POST'])
def my_form_post():
    link = request.form['text']
    yt = pytube.YouTube(link)
    stream = yt.streams.filter(res="360p").first()
    stream.download("./download/", filename='temp.mp4')
    file_location = './download/temp.mp4'
    return send_file(file_location, as_attachment=True)

if __name__ == "__main__":
    app.run(port=3003)
