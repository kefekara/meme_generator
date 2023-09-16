# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory
import random

app = Flask(__name__)

# Form sonuçları


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print()
        # seçilen resmi almak
        selected_image = request.form.get('image_selector')
        textTop = request.form.get('text_top')
        textBottom = request.form.get('text_bottom')


        # Görev #3. Metnin konumunu almak
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Görev #3. Metnin rengini almak
        selected_color = request.form.get('color_selector')
        if selected_color == 'Random':
            selected_color = random_color()

        return render_template('index.html',
                               image_selector=selected_image,
                               text_top=textTop,
                               text_bottom=textBottom,
                               textTop_y=text_top_y,
                               textBottom_y=text_bottom_y,
                               selected_color=selected_color,
                               color_selector = request.form.get('color_selector')
                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', image_selector='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)


def random_color():
    return "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])


app.run(debug=True)
