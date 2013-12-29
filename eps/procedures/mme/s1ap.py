from eps.messages.s1ap import s1SetupResponse, s1SetupFailure
from eps.messages.s1ap import initialContextSetupRequest

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
    Complete, Failure = range(2)
 
    def __init__(self, ioService, procedureCompletionCallback):
        self.ioService = ioService
        self.procedureCompletionCallback = procedureCompletionCallback
        self.outstandingProcedures = set()
         
    def terminate(self):
        pass
    
    def handleInitialUESetupMessage(self, source, interface, channelInfo, message):
        if message["procedureCode"] == "initialContextSetup":
            self.enbAddress = source
            enbUeS1apId = message["enbUeS1apId"]
            self.outstandingProcedures.remove(enbUeS1apId)
            self.ioService.sendMessage(source, *initialContextSetupRequest(
                enbUeS1apId, "12"))
            self.procedureCompletionCallback(self.Complete, enbUeS1apId)
            return True
        return False
#    def start(self, enbAddress, procedureCode="successfulOutcome", enbUeS1apId="12"):
#       self.ioService.sendMessage(enbAddress, *initialContextSetupRequest(
#            enbUeS1apId, procedureCode))
#        self.outstandingProcedures.add(enbUeS1apId)