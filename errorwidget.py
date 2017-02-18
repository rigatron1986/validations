import os
from PySide import QtGui, QtCore

import pipeline.core.pyside_util as pysideUtil

reload(pysideUtil)

uiPath = os.path.join(os.path.dirname(__file__), 'errorwidget.ui')
super_widget = pysideUtil.get_pyside_class(uiPath)


class UI(super_widget[0], super_widget[1]):
    def __init__(self, parent=pysideUtil.getMayaWindow()):
        super(UI, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.btn_fix.setVisible(False)

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
        self.lbl_error.setText(self._msg)

    @property
    def has_fix(self):
        return self._has_fix

    @has_fix.setter
    def has_fix(self, value):
        self._has_fix = value
        if self._has_fix:
            self.btn_fix.setVisible(True)
        else:
            self.btn_fix.setVisible(False)

    @property
    def has_failed(self):
        return self._has_failed

    @has_failed.setter
    def has_failed(self, value):
        self._has_failed = value
