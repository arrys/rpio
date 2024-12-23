# **********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************

from RoboSapiensAdaptivePlatform.utils.nodes import TriggeredNode
from RoboSapiensAdaptivePlatform.utils.constants import *
from RoboSapiensAdaptivePlatform.Communication.Messages.messages import *


class analysis(TriggeredNode):

    def __init__(self,logger=None,knowledgeBase=None, verbose=False):
        super().__init__(logger=logger,knowledge=knowledgeBase,verbose=verbose)

        self._name="analysis"
    # ------------------------------------------------------------------------------------------------
    # -------------------------------------INTERNAL FUNCTIONS----------------------------------------
    # ------------------------------------------------------------------------------------------------
    def _SpinOnceFcn(self, args):
        # 1. FETCH KNOWLEDGE FROM KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT
        k1, history1 = self.knowledge.read("temperature_average", queueSize=10)

        # 2. PERFORM ANALYSIS

        # 3. SIGNAL ANALYSIS STATE VIA KNOWLEDGE
        self.RaPSignalStatus(component=adaptivityComponents.ANALYSIS,status=analysisStatus.ANOMALY,accuracy=1.0)    #DUMMY

        self.logger.log("["+self._name+"] - "+"Analyzing knowledge: " + k1.name + " with values:" + history1.__str__())

        # 4. return status of execution (fail = False, success = True)
        return True

    def _EnterInitializationModeFcn(self):
        if self._verbose: print("Enter initializationModeFcn not implemented")

    def _ExitInitializationModeFcn(self):
        # initial signal after startup
        self.RaPSignalStatus(component=adaptivityComponents.ANALYSIS,status=analysisStatus.NORMAL,accuracy=1.0)

    def _EnterConfigurationModeFcn(self):
        if self._verbose: print("Enter configurationModeFcn not implemented")

        