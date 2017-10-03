#encoding:utf-8

from flask import Flask
from flask import request
from flask.templating import render_template
import json
from dataTools import DataTools
from dataTools import saveObjToExcel


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/getData',methods=['POST'])
def getData():
    username=request.form['username'].strip()
    password=request.form['password'].strip()
    startDate=request.form['startDate'].strip()
    endDate=request.form['endDate'].strip()
    checkNum=int(request.form['checkNum'].strip())
    dts=DataTools(username,password,startDate,endDate,checkNum)
    dts.getAllData()
    jsonData=json.dumps(dict(dates=dts.mydates,staffs=dts.mystaffs,dateStaffStatues=dts.dateStaffStatue))
    return jsonData

@app.route('/saveData',methods=['POST'])
def saveData():
    mydates=json.loads(request.form['dates'])
    mystaffs=json.loads(request.form['staffs'])
    mystatues=json.loads(request.form['statues'])
    return saveObjToExcel(mydates,mystaffs,mystatues)

    

if __name__ == '__main__':
    app.run(host='10.158.249.14',port=80)