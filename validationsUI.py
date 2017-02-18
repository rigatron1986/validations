import os
from PySide import QtGui, QtCore

import pipeline.core.pyside_util as pysideUtil

reload(pysideUtil)
import errorwidget
reload(errorwidget)

uiPath=os.path.join(os.path.dirname(__file__),'validation.ui')
super_widget = pysideUtil.get_pyside_class(uiPath)

class UI(super_widget[0],super_widget[1]):
    def __init__(self,validation_result,parent=pysideUtil.getMayaWindow()):
        super(UI,self).__init__(parent)
        self.validations_result=validation_result

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.initUi()
    def initUi(self):
        self.listValidations(succeded=False)

    def listValidations(self,succeded=False):
        self.lw_errors.clear()

        validation_result = [each for each in self.validations_result if each[1][0]==succeded]
        for v in validation_result:
            widget = errorwidget.UI()

            if succeded:
                widget.has_fix=False
            else:
                widget.has_fix=v[0].has_fix
                if widget.has_fix:
                    if v[0].__class__.__name__=='timeNodeKeyedCheck':
                        widget.btn_fix.setText('Sel')
                try:
                    widget.btn_fix.clicked.connect(v[0].fix)
                except:
                    pass
            widget.has_failed = not v[1][0]
            if v[1][0]:
                widget.msg=v[0].title
            else:
                widget.msg=v[1][1]
            item=QtGui.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(400,60))
            self.lw_errors.addItem(item)
            self.lw_errors.setItemWidget(item,widget)
    def displayValidationsCount(self):
        succeded=[v for v in self.validations_result if v[1][0] ==True]

def Validation_UI(validation_result,parent):
    global WIN
    try:
        WIN.close()
    except:
        pass
    WIN = UI(validation_result,parent)
    WIN.show()
