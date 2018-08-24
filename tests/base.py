import unittest
from functools import wraps
from unittest.mock import patch, Mock

import drucker_pb2

from drucker.core.predict_interface import PredictResult
from tests.drucker.predict_dummy import PredictDummy
from drucker.logger.logger_jsonlogger import ServiceLogger, SystemLogger
import drucker.core.drucker_worker_servicer

service_logger = ServiceLogger(app_name="test", app_env="development")
system_logger = SystemLogger(logger_name="test", app_name="test", app_env="development")
predictor = PredictDummy()
Type = drucker.core.drucker_worker_servicer.DruckerWorkerServicer.Type

class DruckerWorkerTest(unittest.TestCase):
    """DruckerWorkerTest is a base class for testing DruckerWorkerClient and DruckerWorkerServicer.
    The methods of both will xxxOutput instance and this test base class implements
    several methods to check that the return values have correct type.
    """

    def assertStringResponse(self, response):
        self.assertIsInstance(response, drucker_pb2.StringOutput)

    def assertBytesResponse(self, response):
        for item in response:
            self.assertIsInstance(item, drucker_pb2.BytesOutput)

    def assertArrIntResponse(self, response):
        self.assertIsInstance(response, drucker_pb2.ArrIntOutput)

    def assertArrFloatResponse(self, response):
        self.assertIsInstance(response, drucker_pb2.ArrFloatOutput)

    def assertArrStringResponse(self, response):
        self.assertIsInstance(response, drucker_pb2.ArrStringOutput)


_prediction_value_map = {
    Type.STRING: PredictResult('Drucker', 1.0, option={}),
    Type.BYTES: PredictResult(b'\x8f\xfa;\xc8a\xa3T%', 1.0, option={}),
    Type.ARRAY_INT: PredictResult([2, 3, 5, 7], [1.0, 1.0, 1.0, 1.0], option={}),
    Type.ARRAY_FLOAT: PredictResult([0.78341155, 0.03166816, 0.92745938], [1.0, 1.0, 1.0], option={}),
    Type.ARRAY_STRING: PredictResult(['Drucker', 'is', 'awesome'], [1.0, 1.0, 1.0], option={}),
}


def patch_predictor(input_type, output_type):
    """Decorator to mock the predictor.
    Patch the several methods of the Predict class to make a fake predictor.
    """
    def test_method(func):
        @wraps(func)
        def inner_method(*args, **kwargs):
            with patch('tests.drucker.predict_dummy.PredictDummy.get_type_input',
                       new=Mock(return_value=input_type)) as _,\
                    patch('tests.drucker.predict_dummy.PredictDummy.get_type_output',
                          new=Mock(return_value=output_type)) as _, \
                    patch('tests.drucker.predict_dummy.PredictDummy.load_model') as _, \
                    patch('tests.drucker.predict_dummy.PredictDummy.predict',
                          new=Mock(return_value=_prediction_value_map[output_type])) as _:
                return func(*args, **kwargs)
        return inner_method
    return test_method
