# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_ingress import V1beta1Ingress


class TestV1beta1Ingress(unittest.TestCase):
    """ V1beta1Ingress unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1Ingress(self):
        """
        Test V1beta1Ingress
        """
        model = kubernetes.client.models.v1beta1_ingress.V1beta1Ingress()


if __name__ == '__main__':
    unittest.main()
