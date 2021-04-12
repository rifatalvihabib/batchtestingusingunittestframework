import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from  Package2.TC_PaymentReturnsTest import PaymentReturnsTest
from Package2.TC_PayementTest import PaymentTest

#get all test from login signup,paymentest and paymentREturnsTEst
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating test suits

sanityTestSuite= unittest.TestSuite([tc1, tc2]) #sanity test suite
#unittest.TextTestRunner().run(sanityTestSuite)
functionaltestSuite= unittest.TestSuite([tc3, tc4]) #functional test suite
mastertestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])  #mASTER TEST SUITE

unittest.TextTestRunner(verbosity=2).run(mastertestSuite)  #verbosity will show detail information of log






