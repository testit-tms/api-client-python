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
from testit_api_client.models.attachment_model import AttachmentModel
from testit_api_client.models.link_model import LinkModel
from typing import Optional, Set
from typing_extensions import Self

class TestResultHistoryResponse(BaseModel):
    """
    TestResultHistoryResponse
    """ # noqa: E501
    id: StrictStr = Field(description="Internal test result identifier")
    created_date: datetime = Field(description="Test result creation date", alias="createdDate")
    modified_date: datetime = Field(description="Test result last modification date", alias="modifiedDate")
    user_id: StrictStr = Field(description="Internal identifier of user who stopped test run related to the test result or user who created the test result                If test run was stopped, this property equals identifier of user who stopped it.  Otherwise, the property equals identifier of user who created the test result", alias="userId")
    test_run_id: Optional[StrictStr] = Field(default=None, description="Identifier of test run related to the test result", alias="testRunId")
    test_run_name: Optional[StrictStr] = Field(default=None, description="Name of test run related to the test result", alias="testRunName")
    created_by_user_name: Optional[StrictStr] = Field(default=None, description="Username of user who created test run", alias="createdByUserName")
    test_plan_id: Optional[StrictStr] = Field(default=None, description="Internal identifier of test plan related to the test result's test run", alias="testPlanId")
    test_plan_global_id: Optional[StrictInt] = Field(default=None, description="Global identifier of test plan related to the test result's test run", alias="testPlanGlobalId")
    test_plan_name: Optional[StrictStr] = Field(default=None, description="Name of test plan related to the test result's test run", alias="testPlanName")
    configuration_name: Optional[StrictStr] = Field(default=None, description="Configuration name of test point related to the test result or from test result itself                If test point related to the test result has configuration, this property will be equal to the test point configuration name.  Otherwise, this property will be equal to the test result configuration name", alias="configurationName")
    is_automated: StrictBool = Field(description="Boolean flag defines if test point related to the test result is automated or not", alias="isAutomated")
    outcome: Optional[StrictStr] = Field(default=None, description="Outcome from test result with max modified date or from first created test result                Property can contain one of these values: Passed, Failed, InProgress, Blocked, Skipped.                If any test result related to the test run is linked with autotest and the run has an outcome, the outcome value equals to the  worst outcome of the last modified test result. Otherwise, the outcome equals to the outcome of first created test result in the  test run.")
    comment: Optional[StrictStr] = Field(default=None, description="Test result comment                If any test result related to the test run is linked with autotest, comment will have default value.  Otherwise, the comment equals to the comment of first created test result in the test run")
    links: Optional[List[LinkModel]] = Field(default=None, description="Test result links                If any test result related to the test run is linked with autotest, link will be equal to the links of last modified test result.  Otherwise, the links equals to the links of first created test result in the test run.")
    started_on: Optional[datetime] = Field(default=None, description="Start date time from test result or from test run (if test run new state is Running or Completed state)", alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, description="End date time from test result or from test run (if test run new state is In progress, Stopped or Completed)", alias="completedOn")
    duration: Optional[StrictInt] = Field(default=None, description="Duration of first created test result in the test run")
    created_by_id: StrictStr = Field(description="Unique identifier of user who created first test result in the test run", alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of user who applied last modification of first test result in the test run", alias="modifiedById")
    attachments: Optional[List[AttachmentModel]] = Field(default=None, description="Attachments related to the test result                If any test result related to the test run is linked with autotest, attachments will be equal to the attachments of last modified  test result. Otherwise, the attachments equals to the attachments of first created test result in the test run.")
    work_item_version_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of workitem version related to the first test result in the test run", alias="workItemVersionId")
    work_item_version_number: Optional[StrictInt] = Field(default=None, description="Number of workitem version related to the first test result in the test run", alias="workItemVersionNumber")
    launch_source: Optional[StrictStr] = Field(default=None, alias="launchSource")
    failure_class_ids: List[StrictStr] = Field(description="Unique identifier of failure classes related to the first test result in the test run", alias="failureClassIds")
    parameters: Optional[Dict[str, StrictStr]] = Field(default=None, description="Parameters of test result")
    __properties: ClassVar[List[str]] = ["id", "createdDate", "modifiedDate", "userId", "testRunId", "testRunName", "createdByUserName", "testPlanId", "testPlanGlobalId", "testPlanName", "configurationName", "isAutomated", "outcome", "comment", "links", "startedOn", "completedOn", "duration", "createdById", "modifiedById", "attachments", "workItemVersionId", "workItemVersionNumber", "launchSource", "failureClassIds", "parameters"]

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
        """Create an instance of TestResultHistoryResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # set to None if test_run_id (nullable) is None
        # and model_fields_set contains the field
        if self.test_run_id is None and "test_run_id" in self.model_fields_set:
            _dict['testRunId'] = None

        # set to None if test_run_name (nullable) is None
        # and model_fields_set contains the field
        if self.test_run_name is None and "test_run_name" in self.model_fields_set:
            _dict['testRunName'] = None

        # set to None if created_by_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_user_name is None and "created_by_user_name" in self.model_fields_set:
            _dict['createdByUserName'] = None

        # set to None if test_plan_id (nullable) is None
        # and model_fields_set contains the field
        if self.test_plan_id is None and "test_plan_id" in self.model_fields_set:
            _dict['testPlanId'] = None

        # set to None if test_plan_global_id (nullable) is None
        # and model_fields_set contains the field
        if self.test_plan_global_id is None and "test_plan_global_id" in self.model_fields_set:
            _dict['testPlanGlobalId'] = None

        # set to None if test_plan_name (nullable) is None
        # and model_fields_set contains the field
        if self.test_plan_name is None and "test_plan_name" in self.model_fields_set:
            _dict['testPlanName'] = None

        # set to None if configuration_name (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_name is None and "configuration_name" in self.model_fields_set:
            _dict['configurationName'] = None

        # set to None if outcome (nullable) is None
        # and model_fields_set contains the field
        if self.outcome is None and "outcome" in self.model_fields_set:
            _dict['outcome'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

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

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        # set to None if work_item_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_version_id is None and "work_item_version_id" in self.model_fields_set:
            _dict['workItemVersionId'] = None

        # set to None if work_item_version_number (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_version_number is None and "work_item_version_number" in self.model_fields_set:
            _dict['workItemVersionNumber'] = None

        # set to None if launch_source (nullable) is None
        # and model_fields_set contains the field
        if self.launch_source is None and "launch_source" in self.model_fields_set:
            _dict['launchSource'] = None

        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultHistoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "userId": obj.get("userId"),
            "testRunId": obj.get("testRunId"),
            "testRunName": obj.get("testRunName"),
            "createdByUserName": obj.get("createdByUserName"),
            "testPlanId": obj.get("testPlanId"),
            "testPlanGlobalId": obj.get("testPlanGlobalId"),
            "testPlanName": obj.get("testPlanName"),
            "configurationName": obj.get("configurationName"),
            "isAutomated": obj.get("isAutomated"),
            "outcome": obj.get("outcome"),
            "comment": obj.get("comment"),
            "links": [LinkModel.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "startedOn": obj.get("startedOn"),
            "completedOn": obj.get("completedOn"),
            "duration": obj.get("duration"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "attachments": [AttachmentModel.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "workItemVersionId": obj.get("workItemVersionId"),
            "workItemVersionNumber": obj.get("workItemVersionNumber"),
            "launchSource": obj.get("launchSource"),
            "failureClassIds": obj.get("failureClassIds"),
            "parameters": obj.get("parameters")
        })
        return _obj


