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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.date_time_range_selector_model import DateTimeRangeSelectorModel
from testit_api_client.models.failure_category_model import FailureCategoryModel
from testit_api_client.models.int64_range_selector_model import Int64RangeSelectorModel
from testit_api_client.models.test_result_outcome import TestResultOutcome
from typing import Optional, Set
from typing_extensions import Self

class TestResultsFilterRequest(BaseModel):
    """
    TestResultsFilterRequest
    """ # noqa: E501
    configuration_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test result configuration IDs to search for", alias="configurationIds")
    outcomes: Optional[List[TestResultOutcome]] = Field(default=None, description="Specifies a test result outcomes to search for")
    status_codes: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test result status codes to search for", alias="statusCodes")
    failure_categories: Optional[List[FailureCategoryModel]] = Field(default=None, description="Specifies a test result failure categories to search for", alias="failureCategories")
    namespace: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Specifies a test result namespace to search for")
    class_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Specifies a test result class name to search for", alias="className")
    auto_test_global_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies an autotest global IDs to search results for", alias="autoTestGlobalIds")
    name: Optional[StrictStr] = Field(default=None, description="Specifies an autotest name to search results for")
    created_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a test result creation date and time range to search for", alias="createdDate")
    modified_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a test result modified date and time range to search for", alias="modifiedDate")
    started_on: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a test result started on date and time range to search for", alias="startedOn")
    completed_on: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a test result completed on date and time range to search for", alias="completedOn")
    duration: Optional[Int64RangeSelectorModel] = Field(default=None, description="Specifies a test result duration range to search for")
    result_reasons: Optional[List[StrictStr]] = Field(default=None, description="Specifies result reasons for searching test results", alias="resultReasons")
    test_run_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test result test run IDs to search for", alias="testRunIds")
    __properties: ClassVar[List[str]] = ["configurationIds", "outcomes", "statusCodes", "failureCategories", "namespace", "className", "autoTestGlobalIds", "name", "createdDate", "modifiedDate", "startedOn", "completedOn", "duration", "resultReasons", "testRunIds"]

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
        """Create an instance of TestResultsFilterRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_date
        if self.created_date:
            _dict['createdDate'] = self.created_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_date
        if self.modified_date:
            _dict['modifiedDate'] = self.modified_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of started_on
        if self.started_on:
            _dict['startedOn'] = self.started_on.to_dict()
        # override the default output from pydantic by calling `to_dict()` of completed_on
        if self.completed_on:
            _dict['completedOn'] = self.completed_on.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
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

        # set to None if auto_test_global_ids (nullable) is None
        # and model_fields_set contains the field
        if self.auto_test_global_ids is None and "auto_test_global_ids" in self.model_fields_set:
            _dict['autoTestGlobalIds'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if started_on (nullable) is None
        # and model_fields_set contains the field
        if self.started_on is None and "started_on" in self.model_fields_set:
            _dict['startedOn'] = None

        # set to None if completed_on (nullable) is None
        # and model_fields_set contains the field
        if self.completed_on is None and "completed_on" in self.model_fields_set:
            _dict['completedOn'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if result_reasons (nullable) is None
        # and model_fields_set contains the field
        if self.result_reasons is None and "result_reasons" in self.model_fields_set:
            _dict['resultReasons'] = None

        # set to None if test_run_ids (nullable) is None
        # and model_fields_set contains the field
        if self.test_run_ids is None and "test_run_ids" in self.model_fields_set:
            _dict['testRunIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultsFilterRequest from a dict"""
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
            "className": obj.get("className"),
            "autoTestGlobalIds": obj.get("autoTestGlobalIds"),
            "name": obj.get("name"),
            "createdDate": DateTimeRangeSelectorModel.from_dict(obj["createdDate"]) if obj.get("createdDate") is not None else None,
            "modifiedDate": DateTimeRangeSelectorModel.from_dict(obj["modifiedDate"]) if obj.get("modifiedDate") is not None else None,
            "startedOn": DateTimeRangeSelectorModel.from_dict(obj["startedOn"]) if obj.get("startedOn") is not None else None,
            "completedOn": DateTimeRangeSelectorModel.from_dict(obj["completedOn"]) if obj.get("completedOn") is not None else None,
            "duration": Int64RangeSelectorModel.from_dict(obj["duration"]) if obj.get("duration") is not None else None,
            "resultReasons": obj.get("resultReasons"),
            "testRunIds": obj.get("testRunIds")
        })
        return _obj

