# -*- coding: utf-8 -*-
from html2word import Html2word
class Object2word(object):
    
    def __init__(self,document):
        self.document = document
        
    def handleproject(self,project):
        bugs = project.bug_set.all()
        #bug字段为unicode类型
        for bug in bugs:
            
            self.document.add_heading(bug.b_name, level=1) # 漏洞名称
            
            self.document.add_heading(u'风险分析', level=3) # 风险分析
            
            self.document.add_paragraph(bug.b_risk)
            
            self.document.add_heading(u'测试详情', level=3) # 测试详情
            
            h2w = Html2word(str(bug.b_details),self.document)
            h2w.handhtml()
          
            self.document.add_heading(u'风险等级', level=3) # 风险等级
            self.document.add_paragraph(bug.b_level)
            
            self.document.add_heading(u'修复建议', level=3) # 修复建议
            self.document.add_paragraph(bug.b_repair)
            
        return self.document

        
        
        
        
        
            
            
            
        
        
        
          
        
        
        
    
    


