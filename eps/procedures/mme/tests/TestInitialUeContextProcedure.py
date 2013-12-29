'''
Created on 29 Ara 2013

@author: ÝSMAÝL
'''
import time
import unittest

from eps.utils.io import IoService, localhost
from eps.procedures.enb.s1ap import initialContextSetupProcedure as EnbinitialContextSetupProcedure
from eps.procedures.mme.s1ap import initialContextSetupProcedureHandler as EnbinitialContextSetupProcedureHandler
from eps.nodes.enb.enb import Enb
from eps.nodes.mme.mme import Mme
from eps.messages.s1ap import initialContextSetupRequest, initialContextSetupResponse


class TestinitialUeContextSetupProcedure(unittest.TestCase):

    def setUp(self):
        self.mmeIoService = IoService("mme", 9000)
        self.enbIoService = IoService("enb", 9001)
        [s.start() for s in self.mmeIoService, self.enbIoService]
        self.enbProcedure = EnbinitialContextSetupProcedure(3, 0.5, self.enbIoService, 
            self.__procedureEnbCompleteCallback__)


    def tearDown(self):
        [s.stop() for s in self.enbIoService, self.ueIoService]

    def __procedureEnbCompleteCallback__(self, result, addr, a, b, args=None):
        self.enbResult = result
        
    def test_procedureSuccessful(self):
        self.enbProcedure.start((localhost(), 9001), 0, "12")
        time.sleep(0.1)
        self.mmeIoService.sendMessage("enb", *initialContextSetupRequest(0))
        time.sleep(0.1)
        self.assertEqual(self.result, EnbinitialContextSetupProcedureHandler.Complete)
        
    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()