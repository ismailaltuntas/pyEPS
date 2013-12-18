def s1SetupRequest(globalEnbId, enbName, supportedTas, csgIdList, defaultPagingDrx):
    return (
        "s1",
        {
         "streamId": 0
        },
        {
         "messageType": {
          "procedureCode": "s1Setup",
          "typeOfMessage": "initiatingMessage"
         },
         "globalEnbId": globalEnbId, # for the sake of simplicity assume that there is no macro/home eNB distinction
         "enbName": enbName,
         "supportedTas": supportedTas, # eg. ((43415, "00101", "00102"), (43788, "00101", "00102"))
         "csgIdList": csgIdList,
         "defaultPagingDrx": defaultPagingDrx,
        }
    )

def s1SetupResponse(mmeName, servedGummeis, relativeMmeCapacity, criticalityDiagnostics):
    return (
        "s1",
        {
         "streamId": 0
        },
        {
         "messageType": {
          "procedureCode": "s1Setup",
          "typeOfMessage": "successfulOutcome"
         },
         "mmeName": mmeName,
         "servedGummeis": servedGummeis,
         "relativeMmeCapacity": relativeMmeCapacity,
         "criticalityDiagnostics": criticalityDiagnostics,
        }
    )

def s1SetupFailure(cause, timeToWait, criticalityDiagnostics):
    return (
        "s1",
        {
         "streamId": 0
        },
        {
         "messageType": {
          "procedureCode": "s1Setup",
          "typeOfMessage": "unsuccessfulOutcome"
         },
         "cause": cause,
         "timeToWait": timeToWait,
         "criticalityDiagnostics": criticalityDiagnostics,
        }
    )

def initialUeMessage(enbUeS1apId, nasPdu, tai, eUtranCgi, rrcEstablishmentCause,
    sTmsi, csgId, gummei, cellAccessMode):
    return (
        "s1",
        {
         "streamId": 1
        },
        {
         "messageType": {
          "procedureCode": "initialUeMessage",
          "typeOfMessage": "initiatingMessage"
         },
         "enbUeS1apId": enbUeS1apId,
         "nasPdu": nasPdu,
         "tai": tai,
         "eUtranCgi": eUtranCgi,
         "rrcEstablishmentCause": rrcEstablishmentCause,
         "sTmsi": sTmsi,
         "csgId": csgId,
         "gummei": gummei,
         "cellAccessMode": cellAccessMode
        }
    )

def uplinkNasTransport(enbUeS1apId, mmeUeS1apId, nasPdu, tai):
    return (
        "s1",
        {
         "streamId": 1
        },
        {
         "messageType": {
          "procedureCode": "downlinkNasTransport",
          "typeOfMessage": "initiatingMessage"
         },
         "enbUeS1apId": enbUeS1apId,
         "mmeUeS1apId": enbUeS1apId,
         "nasPdu": nasPdu,
         "tai": tai,
        }
    )

def downlinkNasTransport(enbUeS1apId, mmeUeS1apId, nasPdu):
    return (
        "s1",
        {
         "streamId": 1
        },
        {
         "messageType": {
          "procedureCode": "downlinkNasTransport",
          "typeOfMessage": "initiatingMessage"
         },
         "enbUeS1apId": enbUeS1apId,
         "mmeUeS1apId": enbUeS1apId,
         "nasPdu": nasPdu,
        }
    )
def initialContextSetupRequest(mmeUeS1apId, enbUeS1apId, erabtoBeSetupList, UEAggregateMaxBitRate, 
    eRabID, eRabLevelQoSParameters, transportLayerAddress, gtpTeid, nasPdu, UeSecCapabilities, securityKey, 
    UeRadioCapability, mmeUeS1apId2,maxnoofeRabs):
    return (
        "s1",
        {
         "streamId": 1
         },
         {
          "messageType": {
          "procedureCode": "initialContextSetup",
          "typeOfMessage": "initiatingMessage"
           },
         "mmeUeS1apId": mmeUeS1apId,
         "enbUeS1apId": enbUeS1apId,
         "erabtoBeSetupList": erabtoBeSetupList,
         "UEAggregateMaxBitRate":UEAggregateMaxBitRate,
         "eRabID": eRabID,
         "eRabLevelQoSParameters":eRabLevelQoSParameters,
         "transportLayerAddress": transportLayerAddress,
         "gtpTeid": gtpTeid,
         "nasPdu": nasPdu,
         "UeSecCapabilities": UeSecCapabilities,
         "securityKey": securityKey,
         "UeRadioCapability":UeRadioCapability,
         "mmeUeS1apId2":mmeUeS1apId2,
         "maxnoofeRabs": maxnoofeRabs,
          }   
    )
def initialContextSetupResponse(mmeUeS1apId, enbUeS1apId, erabtoBeSetupList, eRabID, transportLayerAddress, 
    gtpTeid, maxnoofeRabs):
    return (
        "s1",
        {
         "streamId": 1
         },
         {
          "messageType": {
          "procedureCode": "initialContextSetup",
          "typeOfMessage": "successfulOutcome"
           },
         "mmeUeS1apId": mmeUeS1apId,
         "enbUeS1apId": enbUeS1apId,
         "erabtoBeSetupList": erabtoBeSetupList,
         "eRabID": eRabID,
         "transportLayerAddress": transportLayerAddress,
         "gtpTeid": gtpTeid,
         "maxnoofeRabs": maxnoofeRabs,
          }   
    )