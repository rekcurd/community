#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

# noinspection PyUnresolvedReferences
from drucker.core.predict_interface import PredictInterface, PredictLabel, PredictResult, EvaluateResult


class PredictDummy(PredictInterface):
    def __init__(self):
        super().__init__()

    def set_type(self, type_input: Enum, type_output: Enum) -> None:
        super().set_type(type_input, type_output)

    def get_type_input(self) -> Enum:
        return super().get_type_input()

    def get_type_output(self) -> Enum:
        return super().get_type_output()

    def load_model(self, model_path: str = None) -> None:
        pass

    def predict(self, input: PredictLabel, option: dict = None) -> PredictResult:
        pass

    def evaluate(self, file: bytes) -> EvaluateResult:
        pass
