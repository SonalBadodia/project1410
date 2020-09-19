# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:16:58 2020

@author: ThisPc
"""
import yaml 

class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml','r') as f1:
            self.config = yaml.load(f1)
            
    def loadConfig(self,filepath):
        with open(filePath,'r') as f1:
            text = f1.read()
        return text
    
    def splitSentences(self,text):
        sentences = text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstSent, restOfSent = sentences[0],sentences[1:]
        return firstSent,restOfSent
    
    
summarizeDocObj = SummarizeDoc()
summarizeDocObj.loadConfig()