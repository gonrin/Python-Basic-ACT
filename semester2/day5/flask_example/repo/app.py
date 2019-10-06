from flask import request, render_template

# flask run --host=0.0.0.0
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


########### Loai hang hoa #############

@app.route('/loaihanghoa')
def loaihanghoa_list():
    return 'List loai hang hoa'

@app.route('/loaihanghoa/create')
def loaihanghoa_create():
    return 'Create loai hang hoa'

@app.route('/loaihanghoa/read')
def loaihanghoa_read():
    id = request.args.get('id', '')

    ### get thong tin loai hang hoa tu file

    obj = {"id": 13, "ten": "Coca", "ghichu": "Ghi chu Coca cola"}
    print(request.args)
    return render_template('loaihanghoa/read.html', id=obj.get("id"), ten=obj.get("ten"),\
        ghichu=obj.get("ghichu"))

@app.route('/loaihanghoa/update')
def loaihanghoa_update():
    return 'Update loai hang hoa'

@app.route('/loaihanghoa/delete')
def loaihanghoa_delete():
    return 'Delete loai hang hoa'

########### End of Loai hang hoa #############