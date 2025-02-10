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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.attachment_api_result import AttachmentApiResult
from testit_api_client.models.auto_test_api_result import AutoTestApiResult
from testit_api_client.models.auto_test_step_results_api_result import AutoTestStepResultsApiResult
from testit_api_client.models.link_api_result import LinkApiResult
from testit_api_client.models.step_comment_api_result import StepCommentApiResult
from testit_api_client.models.test_point_short_api_result import TestPointShortApiResult
from testit_api_client.models.test_result_failure_class_api_result import TestResultFailureClassApiResult
from testit_api_client.models.test_status_api_result import TestStatusApiResult
from typing import Optional, Set
from typing_extensions import Self

class TestResultApiResult(BaseModel):
    """
    TestResultApiResult
    """ # noqa: E501
    id: StrictStr
    started_on: Optional[datetime] = Field(default=None, alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="completedOn")
    duration_in_ms: Optional[StrictInt] = Field(default=None, alias="durationInMs")
    traces: Optional[StrictStr] = None
    failure_type: Optional[StrictStr] = Field(default=None, alias="failureType")
    message: Optional[StrictStr] = None
    run_by_user_id: Optional[StrictStr] = Field(default=None, alias="runByUserId")
    stopped_by_user_id: Optional[StrictStr] = Field(default=None, alias="stoppedByUserId")
    outcome: StrictStr
    auto_test_id: Optional[StrictStr] = Field(default=None, alias="autoTestId")
    test_point_id: Optional[StrictStr] = Field(default=None, alias="testPointId")
    test_run_id: StrictStr = Field(alias="testRunId")
    configuration_id: StrictStr = Field(alias="configurationId")
    status: TestStatusApiResult
    test_point: Optional[TestPointShortApiResult] = Field(default=None, alias="testPoint")
    auto_test: Optional[AutoTestApiResult] = Field(default=None, alias="autoTest")
    auto_test_step_results: Optional[List[AutoTestStepResultsApiResult]] = Field(default=None, alias="autoTestStepResults")
    setup_results: Optional[List[AutoTestStepResultsApiResult]] = Field(default=None, alias="setupResults")
    teardown_results: Optional[List[AutoTestStepResultsApiResult]] = Field(default=None, alias="teardownResults")
    work_item_version_id: Optional[StrictStr] = Field(default=None, alias="workItemVersionId")
    work_item_version_number: Optional[StrictInt] = Field(default=None, alias="workItemVersionNumber")
    attachments: List[AttachmentApiResult]
    links: List[LinkApiResult]
    failure_classes: List[TestResultFailureClassApiResult] = Field(alias="failureClasses")
    step_comments: Optional[List[StepCommentApiResult]] = Field(default=None, alias="stepComments")
    parameters: Optional[Dict[str, StrictStr]] = None
    properties: Optional[Dict[str, StrictStr]] = None
    created_date: datetime = Field(alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    is_deleted: StrictBool = Field(alias="isDeleted")
    __properties: ClassVar[List[str]] = ["id", "startedOn", "completedOn", "durationInMs", "traces", "failureType", "message", "runByUserId", "stoppedByUserId", "outcome", "autoTestId", "testPointId", "testRunId", "configurationId", "status", "testPoint", "autoTest", "autoTestStepResults", "setupResults", "teardownResults", "workItemVersionId", "workItemVersionNumber", "attachments", "links", "failureClasses", "stepComments", "parameters", "properties", "createdDate", "modifiedDate", "createdById", "modifiedById", "isDeleted"]

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
        """Create an instance of TestResultApiResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test_point
        if self.test_point:
            _dict['testPoint'] = self.test_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_test
        if self.auto_test:
            _dict['autoTest'] = self.auto_test.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in auto_test_step_results (list)
        _items = []
        if self.auto_test_step_results:
            for _item_auto_test_step_results in self.auto_test_step_results:
                if _item_auto_test_step_results:
                    _items.append(_item_auto_test_step_results.to_dict())
            _dict['autoTestStepResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in setup_results (list)
        _items = []
        if self.setup_results:
            for _item_setup_results in self.setup_results:
                if _item_setup_results:
                    _items.append(_item_setup_results.to_dict())
            _dict['setupResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in teardown_results (list)
        _items = []
        if self.teardown_results:
            for _item_teardown_results in self.teardown_results:
                if _item_teardown_results:
                    _items.append(_item_teardown_results.to_dict())
            _dict['teardownResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in failure_classes (list)
        _items = []
        if self.failure_classes:
            for _item_failure_classes in self.failure_classes:
                if _item_failure_classes:
                    _items.append(_item_failure_classes.to_dict())
            _dict['failureClasses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in step_comments (list)
        _items = []
        if self.step_comments:
            for _item_step_comments in self.step_comments:
                if _item_step_comments:
                    _items.append(_item_step_comments.to_dict())
            _dict['stepComments'] = _items
        # set to None if started_on (nullable) is None
        # and model_fields_set contains the field
        if self.started_on is None and "started_on" in self.model_fields_set:
            _dict['startedOn'] = None

        # set to None if completed_on (nullable) is None
        # and model_fields_set contains the field
        if self.completed_on is None and "completed_on" in self.model_fields_set:
            _dict['completedOn'] = None

        # set to None if duration_in_ms (nullable) is None
        # and model_fields_set contains the field
        if self.duration_in_ms is None and "duration_in_ms" in self.model_fields_set:
            _dict['durationInMs'] = None

        # set to None if traces (nullable) is None
        # and model_fields_set contains the field
        if self.traces is None and "traces" in self.model_fields_set:
            _dict['traces'] = None

        # set to None if failure_type (nullable) is None
        # and model_fields_set contains the field
        if self.failure_type is None and "failure_type" in self.model_fields_set:
            _dict['failureType'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if run_by_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_by_user_id is None and "run_by_user_id" in self.model_fields_set:
            _dict['runByUserId'] = None

        # set to None if stopped_by_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.stopped_by_user_id is None and "stopped_by_user_id" in self.model_fields_set:
            _dict['stoppedByUserId'] = None

        # set to None if auto_test_id (nullable) is None
        # and model_fields_set contains the field
        if self.auto_test_id is None and "auto_test_id" in self.model_fields_set:
            _dict['autoTestId'] = None

        # set to None if test_point_id (nullable) is None
        # and model_fields_set contains the field
        if self.test_point_id is None and "test_point_id" in self.model_fields_set:
            _dict['testPointId'] = None

        # set to None if test_point (nullable) is None
        # and model_fields_set contains the field
        if self.test_point is None and "test_point" in self.model_fields_set:
            _dict['testPoint'] = None

        # set to None if auto_test (nullable) is None
        # and model_fields_set contains the field
        if self.auto_test is None and "auto_test" in self.model_fields_set:
            _dict['autoTest'] = None

        # set to None if auto_test_step_results (nullable) is None
        # and model_fields_set contains the field
        if self.auto_test_step_results is None and "auto_test_step_results" in self.model_fields_set:
            _dict['autoTestStepResults'] = None

        # set to None if setup_results (nullable) is None
        # and model_fields_set contains the field
        if self.setup_results is None and "setup_results" in self.model_fields_set:
            _dict['setupResults'] = None

        # set to None if teardown_results (nullable) is None
        # and model_fields_set contains the field
        if self.teardown_results is None and "teardown_results" in self.model_fields_set:
            _dict['teardownResults'] = None

        # set to None if work_item_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_version_id is None and "work_item_version_id" in self.model_fields_set:
            _dict['workItemVersionId'] = None

        # set to None if work_item_version_number (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_version_number is None and "work_item_version_number" in self.model_fields_set:
            _dict['workItemVersionNumber'] = None

        # set to None if step_comments (nullable) is None
        # and model_fields_set contains the field
        if self.step_comments is None and "step_comments" in self.model_fields_set:
            _dict['stepComments'] = None

        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict['properties'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultApiResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "startedOn": obj.get("startedOn"),
            "completedOn": obj.get("completedOn"),
            "durationInMs": obj.get("durationInMs"),
            "traces": obj.get("traces"),
            "failureType": obj.get("failureType"),
            "message": obj.get("message"),
            "runByUserId": obj.get("runByUserId"),
            "stoppedByUserId": obj.get("stoppedByUserId"),
            "outcome": obj.get("outcome"),
            "autoTestId": obj.get("autoTestId"),
            "testPointId": obj.get("testPointId"),
            "testRunId": obj.get("testRunId"),
            "configurationId": obj.get("configurationId"),
            "status": TestStatusApiResult.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "testPoint": TestPointShortApiResult.from_dict(obj["testPoint"]) if obj.get("testPoint") is not None else None,
            "autoTest": AutoTestApiResult.from_dict(obj["autoTest"]) if obj.get("autoTest") is not None else None,
            "autoTestStepResults": [AutoTestStepResultsApiResult.from_dict(_item) for _item in obj["autoTestStepResults"]] if obj.get("autoTestStepResults") is not None else None,
            "setupResults": [AutoTestStepResultsApiResult.from_dict(_item) for _item in obj["setupResults"]] if obj.get("setupResults") is not None else None,
            "teardownResults": [AutoTestStepResultsApiResult.from_dict(_item) for _item in obj["teardownResults"]] if obj.get("teardownResults") is not None else None,
            "workItemVersionId": obj.get("workItemVersionId"),
            "workItemVersionNumber": obj.get("workItemVersionNumber"),
            "attachments": [AttachmentApiResult.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "links": [LinkApiResult.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "failureClasses": [TestResultFailureClassApiResult.from_dict(_item) for _item in obj["failureClasses"]] if obj.get("failureClasses") is not None else None,
            "stepComments": [StepCommentApiResult.from_dict(_item) for _item in obj["stepComments"]] if obj.get("stepComments") is not None else None,
            "parameters": obj.get("parameters"),
            "properties": obj.get("properties"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "isDeleted": obj.get("isDeleted")
        })
        return _obj


