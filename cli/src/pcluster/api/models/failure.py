# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from pcluster.api import util
from pcluster.api.models.base_model_ import Model


class Failure(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, failure_code=None, failure_reason=None):  # noqa: E501
        """Failure - a model defined in OpenAPI

        :param failure_code: The failure_code of this Failure.  # noqa: E501
        :type failure_code: str
        :param failure_reason: The failure_reason of this Failure.  # noqa: E501
        :type failure_reason: str
        """
        self.openapi_types = {"failure_code": str, "failure_reason": str}

        self.attribute_map = {"failure_code": "failureCode", "failure_reason": "failureReason"}

        self._failure_code = failure_code
        self._failure_reason = failure_reason

    @classmethod
    def from_dict(cls, dikt) -> "Failure":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Failure of this Failure.  # noqa: E501
        :rtype: Failure
        """
        return util.deserialize_model(dikt, cls)

    @property
    def failure_code(self):
        """Gets the failure_code of this Failure.

        Failure code  # noqa: E501

        :return: The failure_code of this Failure.
        :rtype: str
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this Failure.

        Failure code  # noqa: E501

        :param failure_code: The failure_code of this Failure.
        :type failure_code: str
        """

        self._failure_code = failure_code

    @property
    def failure_reason(self):
        """Gets the failure_reason of this Failure.

        Failure reason  # noqa: E501

        :return: The failure_reason of this Failure.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this Failure.

        Failure reason  # noqa: E501

        :param failure_reason: The failure_reason of this Failure.
        :type failure_reason: str
        """

        self._failure_reason = failure_reason