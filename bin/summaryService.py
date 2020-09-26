# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 23:12:28 2020

@author: ThisPc
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run('0.0.0.0',80)