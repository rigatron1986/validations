import pipeline.tools.Validation.validationController as validationController
reload(validationController)
import pipeline.tools.Validation.validationsUI as validationsUI
reload(validationsUI)

import pipeline.core.pyside_util as pysideUtil
reload(pysideUtil)
validation_result=validationController.validate()
succeded=[v for v in validation_result if v[1][0] == True]
parentA = pysideUtil.getMayaWindow()
if len(succeded)==len(validation_result):
    print 'good'
else:
    validationsUI.Validation_UI(validation_result,parentA)
