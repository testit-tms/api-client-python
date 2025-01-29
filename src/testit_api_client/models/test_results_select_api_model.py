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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from testit_api_client.models.test_results_extraction_api_model import TestResultsExtractionApiModel
from testit_api_client.models.test_results_filter_api_model import TestResultsFilterApiModel
from typing import Optional, Set
from typing_extensions import Self

class TestResultsSelectApiModel(BaseModel):
    """
    TestResultsSelectApiModel
    """ # noqa: E501
    filter: TestResultsFilterApiModel = Field(description="Test result filters")
    extraction_model: TestResultsExtractionApiModel = Field(description="Test results extraction model", alias="extractionModel")
    __properties: ClassVar[List[str]] = ["filter", "extractionModel"]

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
        """Create an instance of TestResultsSelectApiModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extraction_model
        if self.extraction_model:
            _dict['extractionModel'] = self.extraction_model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultsSelectApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": TestResultsFilterApiModel.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "extractionModel": TestResultsExtractionApiModel.from_dict(obj["extractionModel"]) if obj.get("extractionModel") is not None else None
        })
        return _obj


