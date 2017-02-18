import validations
reload(validations)

def validate(selective=False):
    validations_list=[validations.PublishDataFolderExistsOnLocal(),
                      validations.startFrameCheck()]

    result=[]
    for validation in validations_list:
        result.append([validation,validation.check()])
    return result
