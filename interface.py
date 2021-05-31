# import sys
# sys.path.append('D:/Tai Lieu/HUST-Study/20202/NLP/project/code')

from flask import Flask, request, render_template
from url_input import main
from NLP import findAll

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('homepage.html')


@app.route('/', methods=['POST'])
def information():
    try:
        url = request.form['text']
        infor = main(url)
    except:
        url = None
        infor = request.form['text']
    if infor is None or infor == '':
        return {"message": "error"}

    typeE, cateE, ae, road, dt, ct, pr, number, fullname = findAll(infor)
    if number != [[]]:
        number = ', '.join(str(i) for i in number)
    else:
        number = 'None'
    if fullname != [[]]:
        fullname = ', '.join(fullname)
    else:
        fullname = 'None'
    return render_template('homepage.html', output=infor, input=url, typeE=', '.join(typeE),
                           cateE=', '.join(cateE), ae=', '.join(ae), road=', '.join(road),
                           dt=', '.join(dt), ct=', '.join(ct), pr=', '.join(pr),
                           number=number, fullname=fullname)


if __name__ == '__main__':
    app.run()
