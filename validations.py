import pymel.core as pm
import maya.cmds as cmds
import os
import shutil
class Utils:
    @staticmethod
    def isReferenced(pynode):
        return pm.referenceQuery(pynode,isNodeReferenced=True)
    @staticmethod
    def getLocalNodesOfType(typename):
        nodes = pm.ls(type=typename)
        return [each for each in nodes if not Utils.isReferenced(each)]

class Validation:
    def __init__(self):
        self.title=""
    @property
    def has_fix(self):
        return hasattr(self,'fix')# and inspect.ismethod(self.fix)
    def check(self):
        pass

class PublishDataFolderExistsOnLocal(Validation):
    '''
    checks if the folder is present in the local
    '''
    def __init__(self):
        self.title='Folder exists in local'
    def check(self):
        filename=pm.sceneName().__str__()
        shotname=os.path.basename(filename).split('.')[0]
        self.publishLocal=os.path.join(os.path.dirname(filename),'PublishData_{0}'.format(shotname))
        if os.path.exists(self.publishLocal):
            return [False,'PublishData_{0} folder exists in local.'.format(shotname)]
        else:
            return [True]

    def fix(self):
        shutil.rmtree(self.publishLocal,ignore_errors=True)

class startFrameCheck(Validation):
    '''
    checks the start frame of the scene and camera
    '''
    def __init__(self):
        self.title='startFrameCheck'
    def check(self):
        defaultCameras = ['persp', 'top', 'front', 'side']
        allCam = [cmds.listRelatives(x, p=1)[0] for x in cmds.ls(type='camera')]
        finalCam = [x for x in allCam if not x in defaultCameras]
        if len(finalCam) > 1:
            return [False, 'many cam present.']
        startFrame = cmds.playbackOptions(q=1, ast=1)
        endFrame = cmds.playbackOptions(q=1, aet=1)
        if not str(startFrame) == '1.0':
            return [False, 'start frame is not from 1.']
        if finalCam:
            if cmds.keyframe(finalCam[0], query=True, timeChange=True):
                t = list(set(cmds.keyframe(finalCam[0], query=True, timeChange=True)))
                t.sort()
                if not str(t[0]) == '1.0':
                    return [False, 'offset the cam to 1st Frame.']
        else:
            return [False,'No camera present in the scene.']
        return [True]
