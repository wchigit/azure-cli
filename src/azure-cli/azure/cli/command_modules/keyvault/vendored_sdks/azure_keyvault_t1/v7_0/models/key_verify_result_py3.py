# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: skip-file
# flake8: noqa
from msrest.serialization import Model


class KeyVerifyResult(Model):
    """The key verify result.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: True if the signature is verified, otherwise false.
    :vartype value: bool
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(self, **kwargs) -> None:
        super(KeyVerifyResult, self).__init__(**kwargs)
        self.value = None
