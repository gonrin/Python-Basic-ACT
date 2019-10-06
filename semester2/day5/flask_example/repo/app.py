# flask run --host=0.0.0.0
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


########### Loai hang hoa #############

@app.route('/loaihanghoa/list')
def loaihanghoa_list():
    
    objs = [
        {"id": "DA", "ten": "Đồ ăn"},
        {"id": "DU", "ten": "Đồ uống"},
    ]
    return render_template('loaihanghoa/list.html', list_item=objs)

@app.route('/loaihanghoa/create', methods=['POST', 'GET'])
def loaihanghoa_create():
    if request.method == 'GET':
        return render_template('loaihanghoa/create.html')
    if request.method == 'POST':
        #nhan request data
        id = request.form['id']
        ten = request.form['ten']
        #save vao datas tore
        #chuyen nguoi dung vao trang danh sach
        return redirect("/loaihanghoa/list")

@app.route('/loaihanghoa/read')
def loaihanghoa_read():
    id = request.args.get('id', '')

    ### get thong tin loai hang hoa tu file

    obj = {"id": id, "ten": "Coca", "ghichu": "Ghi chu Coca cola"}
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