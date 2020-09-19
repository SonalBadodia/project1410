# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:54:10 2020

@author: ThisPc
"""



from flask import Flask, request

app = Flask(__name__) 

@app.route('/home',methods=['GET'])
def checkStatus():
    return "Yay!! its working"

app.run(host='localhost',port = 8025)