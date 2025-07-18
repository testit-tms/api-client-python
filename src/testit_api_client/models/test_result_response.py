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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from testit_api_client.models.attachment_api_result import AttachmentApiResult
from testit_api_client.models.auto_test import AutoTest
from testit_api_client.models.auto_test_step_result import AutoTestStepResult
from testit_api_client.models.link import Link
from testit_api_client.models.step_comment_api_model import StepCommentApiModel
from testit_api_client.models.step_result_api_model import StepResultApiModel
from testit_api_client.models.test_point import TestPoint
from testit_api_client.models.test_result_outcome import TestResultOutcome
from testit_api_client.models.test_status_api_result import TestStatusApiResult

class TestResultResponse(BaseModel):
    """
    TestResultResponse
    """
    id: StrictStr = Field(...)
    created_date: datetime = Field(default=..., alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    created_by_id: StrictStr = Field(default=..., alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    step_comments: Optional[conlist(StepCommentApiModel)] = Field(default=None, alias="stepComments")
    failure_class_ids: conlist(StrictStr) = Field(default=..., alias="failureClassIds")
    outcome: Optional[TestResultOutcome] = None
    status: Optional[TestStatusApiResult] = None
    comment: Optional[StrictStr] = None
    links: Optional[conlist(Link)] = None
    step_results: Optional[conlist(StepResultApiModel)] = Field(default=None, alias="stepResults")
    attachments: Optional[conlist(AttachmentApiResult)] = None
    auto_test_id: Optional[StrictStr] = Field(default=None, alias="autoTestId")
    configuration_id: StrictStr = Field(default=..., alias="configurationId")
    started_on: Optional[datetime] = Field(default=None, alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="completedOn")
    duration_in_ms: Optional[StrictInt] = Field(default=None, alias="durationInMs")
    traces: Optional[StrictStr] = None
    failure_type: Optional[StrictStr] = Field(default=None, alias="failureType")
    message: Optional[StrictStr] = None
    run_by_user_id: Optional[StrictStr] = Field(default=None, alias="runByUserId")
    stopped_by_user_id: Optional[StrictStr] = Field(default=None, alias="stoppedByUserId")
    test_point_id: StrictStr = Field(default=..., alias="testPointId")
    test_run_id: StrictStr = Field(default=..., alias="testRunId")
    test_point: Optional[TestPoint] = Field(default=None, alias="testPoint")
    auto_test: Optional[AutoTest] = Field(default=None, alias="autoTest")
    auto_test_step_results: Optional[conlist(AutoTestStepResult)] = Field(default=None, alias="autoTestStepResults")
    setup_results: Optional[conlist(AutoTestStepResult)] = Field(default=None, alias="setupResults")
    teardown_results: Optional[conlist(AutoTestStepResult)] = Field(default=None, alias="teardownResults")
    work_item_version_id: StrictStr = Field(default=..., alias="workItemVersionId")
    work_item_version_number: Optional[StrictInt] = Field(default=None, alias="workItemVersionNumber")
    parameters: Optional[Dict[str, StrictStr]] = None
    properties: Optional[Dict[str, StrictStr]] = None
    __properties = ["id", "createdDate", "modifiedDate", "createdById", "modifiedById", "stepComments", "failureClassIds", "outcome", "status", "comment", "links", "stepResults", "attachments", "autoTestId", "configurationId", "startedOn", "completedOn", "durationInMs", "traces", "failureType", "message", "runByUserId", "stoppedByUserId", "testPointId", "testRunId", "testPoint", "autoTest", "autoTestStepResults", "setupResults", "teardownResults", "workItemVersionId", "workItemVersionNumber", "parameters", "properties"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TestResultResponse:
        """Create an instance of TestResultResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in step_comments (list)
        _items = []
        if self.step_comments:
            for _item in self.step_comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stepComments'] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in step_results (list)
        _items = []
        if self.step_results:
            for _item in self.step_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stepResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of test_point
        if self.test_point:
            _dict['testPoint'] = self.test_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_test
        if self.auto_test:
            _dict['autoTest'] = self.auto_test.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in auto_test_step_results (list)
        _items = []
        if self.auto_test_step_results:
            for _item in self.auto_test_step_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['autoTestStepResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in setup_results (list)
        _items = []
        if self.setup_results:
            for _item in self.setup_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['setupResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in teardown_results (list)
        _items = []
        if self.teardown_results:
            for _item in self.teardown_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['teardownResults'] = _items
        # set to None if modified_date (nullable) is None
        # and __fields_set__ contains the field
        if self.modified_date is None and "modified_date" in self.__fields_set__:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and __fields_set__ contains the field
        if self.modified_by_id is None and "modified_by_id" in self.__fields_set__:
            _dict['modifiedById'] = None

        # set to None if step_comments (nullable) is None
        # and __fields_set__ contains the field
        if self.step_comments is None and "step_comments" in self.__fields_set__:
            _dict['stepComments'] = None

        # set to None if outcome (nullable) is None
        # and __fields_set__ contains the field
        if self.outcome is None and "outcome" in self.__fields_set__:
            _dict['outcome'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        # set to None if step_results (nullable) is None
        # and __fields_set__ contains the field
        if self.step_results is None and "step_results" in self.__fields_set__:
            _dict['stepResults'] = None

        # set to None if attachments (nullable) is None
        # and __fields_set__ contains the field
        if self.attachments is None and "attachments" in self.__fields_set__:
            _dict['attachments'] = None

        # set to None if auto_test_id (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_test_id is None and "auto_test_id" in self.__fields_set__:
            _dict['autoTestId'] = None

        # set to None if started_on (nullable) is None
        # and __fields_set__ contains the field
        if self.started_on is None and "started_on" in self.__fields_set__:
            _dict['startedOn'] = None

        # set to None if completed_on (nullable) is None
        # and __fields_set__ contains the field
        if self.completed_on is None and "completed_on" in self.__fields_set__:
            _dict['completedOn'] = None

        # set to None if duration_in_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.duration_in_ms is None and "duration_in_ms" in self.__fields_set__:
            _dict['durationInMs'] = None

        # set to None if traces (nullable) is None
        # and __fields_set__ contains the field
        if self.traces is None and "traces" in self.__fields_set__:
            _dict['traces'] = None

        # set to None if failure_type (nullable) is None
        # and __fields_set__ contains the field
        if self.failure_type is None and "failure_type" in self.__fields_set__:
            _dict['failureType'] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if run_by_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.run_by_user_id is None and "run_by_user_id" in self.__fields_set__:
            _dict['runByUserId'] = None

        # set to None if stopped_by_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.stopped_by_user_id is None and "stopped_by_user_id" in self.__fields_set__:
            _dict['stoppedByUserId'] = None

        # set to None if test_point (nullable) is None
        # and __fields_set__ contains the field
        if self.test_point is None and "test_point" in self.__fields_set__:
            _dict['testPoint'] = None

        # set to None if auto_test (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_test is None and "auto_test" in self.__fields_set__:
            _dict['autoTest'] = None

        # set to None if auto_test_step_results (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_test_step_results is None and "auto_test_step_results" in self.__fields_set__:
            _dict['autoTestStepResults'] = None

        # set to None if setup_results (nullable) is None
        # and __fields_set__ contains the field
        if self.setup_results is None and "setup_results" in self.__fields_set__:
            _dict['setupResults'] = None

        # set to None if teardown_results (nullable) is None
        # and __fields_set__ contains the field
        if self.teardown_results is None and "teardown_results" in self.__fields_set__:
            _dict['teardownResults'] = None

        # set to None if work_item_version_number (nullable) is None
        # and __fields_set__ contains the field
        if self.work_item_version_number is None and "work_item_version_number" in self.__fields_set__:
            _dict['workItemVersionNumber'] = None

        # set to None if parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.parameters is None and "parameters" in self.__fields_set__:
            _dict['parameters'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TestResultResponse:
        """Create an instance of TestResultResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TestResultResponse.parse_obj(obj)

        _obj = TestResultResponse.parse_obj({
            "id": obj.get("id"),
            "created_date": obj.get("createdDate"),
            "modified_date": obj.get("modifiedDate"),
            "created_by_id": obj.get("createdById"),
            "modified_by_id": obj.get("modifiedById"),
            "step_comments": [StepCommentApiModel.from_dict(_item) for _item in obj.get("stepComments")] if obj.get("stepComments") is not None else None,
            "failure_class_ids": obj.get("failureClassIds"),
            "outcome": obj.get("outcome"),
            "status": TestStatusApiResult.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "comment": obj.get("comment"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "step_results": [StepResultApiModel.from_dict(_item) for _item in obj.get("stepResults")] if obj.get("stepResults") is not None else None,
            "attachments": [AttachmentApiResult.from_dict(_item) for _item in obj.get("attachments")] if obj.get("attachments") is not None else None,
            "auto_test_id": obj.get("autoTestId"),
            "configuration_id": obj.get("configurationId"),
            "started_on": obj.get("startedOn"),
            "completed_on": obj.get("completedOn"),
            "duration_in_ms": obj.get("durationInMs"),
            "traces": obj.get("traces"),
            "failure_type": obj.get("failureType"),
            "message": obj.get("message"),
            "run_by_user_id": obj.get("runByUserId"),
            "stopped_by_user_id": obj.get("stoppedByUserId"),
            "test_point_id": obj.get("testPointId"),
            "test_run_id": obj.get("testRunId"),
            "test_point": TestPoint.from_dict(obj.get("testPoint")) if obj.get("testPoint") is not None else None,
            "auto_test": AutoTest.from_dict(obj.get("autoTest")) if obj.get("autoTest") is not None else None,
            "auto_test_step_results": [AutoTestStepResult.from_dict(_item) for _item in obj.get("autoTestStepResults")] if obj.get("autoTestStepResults") is not None else None,
            "setup_results": [AutoTestStepResult.from_dict(_item) for _item in obj.get("setupResults")] if obj.get("setupResults") is not None else None,
            "teardown_results": [AutoTestStepResult.from_dict(_item) for _item in obj.get("teardownResults")] if obj.get("teardownResults") is not None else None,
            "work_item_version_id": obj.get("workItemVersionId"),
            "work_item_version_number": obj.get("workItemVersionNumber"),
            "parameters": obj.get("parameters"),
            "properties": obj.get("properties")
        })
        return _obj


