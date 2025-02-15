# coding: utf-8

"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.failure_category_model import FailureCategoryModel
from testit_api_client.models.test_result_outcome import TestResultOutcome
from typing import Optional, Set
from typing_extensions import Self

class TestResultsLocalFilterModel(BaseModel):
    """
    TestResultsLocalFilterModel
    """ # noqa: E501
    configuration_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test result configuration IDs to search for", alias="configurationIds")
    outcomes: Optional[List[TestResultOutcome]] = Field(default=None, description="Specifies a test result outcomes to search for")
    status_codes: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test result status codes to search for", alias="statusCodes")
    failure_categories: Optional[List[FailureCategoryModel]] = Field(default=None, description="Specifies a test result failure categories to search for", alias="failureCategories")
    namespace: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Specifies a test result namespace to search for")
    class_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Specifies a test result class name to search for", alias="className")
    __properties: ClassVar[List[str]] = ["configurationIds", "outcomes", "statusCodes", "failureCategories", "namespace", "className"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TestResultsLocalFilterModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if configuration_ids (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_ids is None and "configuration_ids" in self.model_fields_set:
            _dict['configurationIds'] = None

        # set to None if outcomes (nullable) is None
        # and model_fields_set contains the field
        if self.outcomes is None and "outcomes" in self.model_fields_set:
            _dict['outcomes'] = None

        # set to None if status_codes (nullable) is None
        # and model_fields_set contains the field
        if self.status_codes is None and "status_codes" in self.model_fields_set:
            _dict['statusCodes'] = None

        # set to None if failure_categories (nullable) is None
        # and model_fields_set contains the field
        if self.failure_categories is None and "failure_categories" in self.model_fields_set:
            _dict['failureCategories'] = None

        # set to None if namespace (nullable) is None
        # and model_fields_set contains the field
        if self.namespace is None and "namespace" in self.model_fields_set:
            _dict['namespace'] = None

        # set to None if class_name (nullable) is None
        # and model_fields_set contains the field
        if self.class_name is None and "class_name" in self.model_fields_set:
            _dict['className'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultsLocalFilterModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configurationIds": obj.get("configurationIds"),
            "outcomes": obj.get("outcomes"),
            "statusCodes": obj.get("statusCodes"),
            "failureCategories": obj.get("failureCategories"),
            "namespace": obj.get("namespace"),
            "className": obj.get("className")
        })
        return _obj


