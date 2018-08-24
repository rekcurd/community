from concurrent import futures

import grpc

import drucker_pb2_grpc

from drucker_client.core.drucker_worker_client import DruckerWorkerClient
from drucker_client.logger.logger_jsonlogger import SystemLogger

import drucker.core.drucker_worker_servicer
import drucker.core.drucker_dashboard_servicer

from tests.base import DruckerWorkerTest, patch_predictor, predictor, service_logger, system_logger

Type = drucker.core.drucker_worker_servicer.DruckerWorkerServicer.Type


def _fake_string_input():
    return 'Drucker'


def _fake_bytes_input():
    return b'u\x95jD\x0c\xf4\xf4{\xa6\xd7'


def _fake_arrint_input():
    return [124, 117,   2, 216]


def _fake_arrfloat_input():
    return [0.51558887, 0.07656534, 0.64258131, 0.45239403, 0.53738411,
            0.3863864, 0.33985784]


def _fake_arrstring_input():
    return ['Drucker', 'is', 'great']


class DruckerWorkerClientTest(DruckerWorkerTest):
    """Tests for DruckerWorkerClient.
    DruckerWorkerClient has to work with DruckerWorkerServicer so the server must be setup for every input/output type.
    """
    server = None
    client = None

    @classmethod
    def setUpClass(cls):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        drucker_pb2_grpc.add_DruckerDashboardServicer_to_server(
            drucker.core.drucker_dashboard_servicer.DruckerDashboardServicer(
                logger=system_logger, predictor=predictor),
            server)
        drucker_pb2_grpc.add_DruckerWorkerServicer_to_server(
            drucker.core.drucker_worker_servicer.DruckerWorkerServicer(
                logger=service_logger, predictor=predictor),
            server)
        server.add_insecure_port("[::]:5000")
        server.start()
        cls.server = server
        drucker_client_logger = SystemLogger(logger_name="test")
        cls.client = DruckerWorkerClient(logger=drucker_client_logger, host='127.0.0.1:5000')

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'server'):
            cls.server.stop(0)

    @patch_predictor(Type.STRING, Type.STRING)
    def test_string_string(self):
        response = self.client.run_predict_string_string(_fake_string_input())
        self.assertStringResponse(response)

    @patch_predictor(Type.STRING, Type.BYTES)
    def test_string_bytes(self):
        response = self.client.run_predict_string_bytes(_fake_string_input())
        self.assertBytesResponse(response)

    @patch_predictor(Type.STRING, Type.ARRAY_INT)
    def test_string_arrint(self):
        response = self.client.run_predict_string_arrint(_fake_string_input())
        self.assertArrIntResponse(response)

    @patch_predictor(Type.STRING, Type.ARRAY_FLOAT)
    def test_string_arrfloat(self):
        response = self.client.run_predict_string_arrfloat(_fake_string_input())
        self.assertArrFloatResponse(response)

    @patch_predictor(Type.STRING, Type.ARRAY_STRING)
    def test_string_arrstring(self):
        response = self.client.run_predict_string_arrstring(_fake_string_input())
        self.assertArrStringResponse(response)

    @patch_predictor(Type.BYTES, Type.STRING)
    def test_bytes_string(self):
        response = self.client.run_predict_bytes_string(_fake_bytes_input())
        self.assertStringResponse(response)

    @patch_predictor(Type.BYTES, Type.BYTES)
    def test_bytes_bytes(self):
        response = self.client.run_predict_bytes_bytes(_fake_bytes_input())
        self.assertBytesResponse(response)

    @patch_predictor(Type.BYTES, Type.ARRAY_INT)
    def test_bytes_arrint(self):
        response = self.client.run_predict_bytes_arrint(_fake_bytes_input())
        self.assertArrIntResponse(response)

    @patch_predictor(Type.BYTES, Type.ARRAY_FLOAT)
    def test_bytes_arrfloat(self):
        response = self.client.run_predict_bytes_arrfloat(_fake_bytes_input())
        self.assertArrFloatResponse(response)

    @patch_predictor(Type.BYTES, Type.ARRAY_STRING)
    def test_bytes_arrstring(self):
        response = self.client.run_predict_bytes_arrstring(_fake_bytes_input())
        self.assertArrStringResponse(response)

    @patch_predictor(Type.ARRAY_INT, Type.STRING)
    def test_arrint_string(self):
        response = self.client.run_predict_arrint_string(_fake_arrint_input())
        self.assertStringResponse(response)

    @patch_predictor(Type.ARRAY_INT, Type.BYTES)
    def test_arrint_bytes(self):
        response = self.client.run_predict_arrint_bytes(_fake_arrint_input())
        self.assertBytesResponse(response)

    @patch_predictor(Type.ARRAY_INT, Type.ARRAY_INT)
    def test_arrint_arrint(self):
        response = self.client.run_predict_arrint_arrint(_fake_arrint_input())
        self.assertArrIntResponse(response)

    @patch_predictor(Type.ARRAY_INT, Type.ARRAY_FLOAT)
    def test_arrint_arrfloat(self):
        response = self.client.run_predict_arrint_arrfloat(_fake_arrint_input())
        self.assertArrFloatResponse(response)

    @patch_predictor(Type.ARRAY_INT, Type.ARRAY_STRING)
    def test_arrint_arrstring(self):
        response = self.client.run_predict_arrint_arrstring(_fake_arrint_input())
        self.assertArrStringResponse(response)

    @patch_predictor(Type.ARRAY_FLOAT, Type.STRING)
    def test_arrfloat_string(self):
        response = self.client.run_predict_arrfloat_string(_fake_arrfloat_input())
        self.assertStringResponse(response)

    @patch_predictor(Type.ARRAY_FLOAT, Type.BYTES)
    def test_arrfloat_bytes(self):
        response = self.client.run_predict_arrfloat_bytes(_fake_arrfloat_input())
        self.assertBytesResponse(response)

    @patch_predictor(Type.ARRAY_FLOAT, Type.ARRAY_INT)
    def test_arrfloat_arrint(self):
        response = self.client.run_predict_arrfloat_arrint(_fake_arrfloat_input())
        self.assertArrIntResponse(response)

    @patch_predictor(Type.ARRAY_FLOAT, Type.ARRAY_FLOAT)
    def test_arrfloat_arrfloat(self):
        response = self.client.run_predict_arrfloat_arrfloat(_fake_arrfloat_input())
        self.assertArrFloatResponse(response)

    @patch_predictor(Type.ARRAY_FLOAT, Type.ARRAY_STRING)
    def test_arrfloat_arrstring(self):
        response = self.client.run_predict_arrfloat_arrstring(_fake_arrfloat_input())
        self.assertArrStringResponse(response)

    @patch_predictor(Type.ARRAY_STRING, Type.STRING)
    def test_arrstring_string(self):
        response = self.client.run_predict_arrstring_string(_fake_arrstring_input())
        self.assertStringResponse(response)

    @patch_predictor(Type.ARRAY_STRING, Type.BYTES)
    def test_arrstring_bytes(self):
        response = self.client.run_predict_arrstring_bytes(_fake_arrstring_input())
        self.assertBytesResponse(response)

    @patch_predictor(Type.ARRAY_STRING, Type.ARRAY_INT)
    def test_arrstring_arrint(self):
        response = self.client.run_predict_arrstring_arrint(_fake_arrstring_input())
        self.assertArrIntResponse(response)

    @patch_predictor(Type.ARRAY_STRING, Type.ARRAY_FLOAT)
    def test_arrstring_arrfloat(self):
        response = self.client.run_predict_arrstring_arrfloat(_fake_arrstring_input())
        self.assertArrFloatResponse(response)

    @patch_predictor(Type.ARRAY_STRING, Type.ARRAY_STRING)
    def test_arrstring_arrstring(self):
        response = self.client.run_predict_arrstring_arrstring(_fake_arrstring_input())
        self.assertArrStringResponse(response)
