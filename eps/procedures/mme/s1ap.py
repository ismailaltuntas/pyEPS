import random
from eps.messages.s1ap import s1SetupResponse, s1SetupFailure
from eps.messages.s1ap import initialContextSetupResponse

class S1SetupProcedureHandler(object):

    def __init__(self, procedureParameters, mmeServiceArea, ioService, enbRegisteredCallback):
        self.procedureParameters = procedureParameters
        self.mmeServiceArea = mmeServiceArea
        self.ioService = ioService
        self.enbRegisteredCallback = enbRegisteredCallback
    
    def execute(self):
        def verifySettings():
            requiredProcedureParameters, requiredProcedureFlags = (
                ("mmeName", "servedGummeis", "timeToWait", "flags"),
                ("rejectS1SetupRequestsFromRegisteredEnbs",)
            )
            missingParameters = set(requiredProcedureParameters) - set(self.procedureParameters)
            missingFlags = set(requiredProcedureFlags) - set(self.procedureParameters["flags"])
            assert not missingParameters, "Missing parameters in mmeSettings: {}".format(missingParameters)
            assert not missingFlags, "Missing flags in procedureParameters['flags']: {}".format(missingFlags)
        verifySettings()
    
    def terminate(self):
        pass
    
    def handleIncomingS1SetupMessage(self, source, interface, channelInfo, message):
        def sendReject(destination, cause, timeToWait):
            self.ioService.sendMessage(destination, *s1SetupFailure(cause, timeToWait, None))
        
        def sendAccept(destination):
            params = (
                self.procedureParameters["mmeName"],
                self.procedureParameters["servedGummeis"],
                255, None
            )
            self.ioService.sendMessage(destination, *s1SetupResponse(*params))
        if self.mmeServiceArea.congested():
            sendReject(source, "congestion", self.procedureParameters["timeToWait"])
            return
        globalEnbId = message["globalEnbId"]
        if globalEnbId in self.mmeServiceArea and \
            self.procedureParameters["flags"]["rejectS1SetupRequestsFromRegisteredEnbs"]:
                sendReject(source, "unspecified", None)
                return
        sendAccept(source)
        self.enbRegisteredCallback(source, globalEnbId)
        
class initialContextSetupProcedureHandler(object):
    def __init__(self, ioService,):
     Success, Failure = range(2)
 
     def __init__(self, ioService, procedureCompletionCallback):
         self.ioService = ioService
         self.procedureCompletionCallback = procedureCompletionCallback
         self.outstandingProcedures = set()
  
    def handleIncomingMessage(self, source, message):
     def handleIncomingMessage(self, source, interface, channelInfo, message):
         if message["procedureCode"] == "initialContextSetup":
             pass
             mmeUeS1apId = message["mmeUeS1apId"]
             self.outstandingProcedures.remove(mmeUeS1apId)
             self.ioService.sendMessage(source, *initialContextSetupResponse(
                 mmeUeS1apId, "12"))
             self.procedureCompletionCallback(self.Complete, mmeUeS1apId)
             return True
         return False
    def start(self, ueAddress, procedureCode="successfulOutcome", mmeUeS1apId="12"):
        self.ioService.sendMessage(ueAddress, *initialContextSetupResponse(
            mmeUeS1apId, procedureCode))
        self.outstandingProcedures.add(mmeUeS1apId)