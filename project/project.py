from flask import Flask,render_template,request,jsonify
import json,os

Basepath=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload_img',methods=['POST'])
def upload_img():
	img=request.files.get('img')
	path=Basepath+'/static/upload/'
	img_path=path+img.filename
	test_path='../static/upload/'+img.filename
	img.save(img_path)
	return  jsonify({'signal':1,'img_path':test_path})



if __name__ == '__main__':
    app.run()
