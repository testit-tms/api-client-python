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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.attachment_api_result import AttachmentApiResult
from testit_api_client.models.auto_test_result_reason_short import AutoTestResultReasonShort
from testit_api_client.models.link_short import LinkShort
from testit_api_client.models.test_status_api_result import TestStatusApiResult
from typing import Optional, Set
from typing_extensions import Self

class TestResultShortResponse(BaseModel):
    """
    TestResultShortResponse
    """ # noqa: E501
    id: StrictStr = Field(description="Unique ID of the test result")
    name: StrictStr = Field(description="Name of autotest represented by the test result")
    autotest_global_id: StrictInt = Field(description="Global ID of autotest represented by the test result", alias="autotestGlobalId")
    test_run_id: StrictStr = Field(description="Unique ID of test run where the test result is located", alias="testRunId")
    configuration_id: StrictStr = Field(description="Unique ID of configuration which the test result uses", alias="configurationId")
    configuration_name: StrictStr = Field(description="Name of configuration which the test result uses", alias="configurationName")
    outcome: Optional[StrictStr] = Field(default=None, description="Outcome of the test result")
    status: Optional[TestStatusApiResult] = None
    result_reasons: List[AutoTestResultReasonShort] = Field(description="Collection of result reasons which the test result have", alias="resultReasons")
    comment: Optional[StrictStr] = Field(default=None, description="Comment to the test result")
    var_date: datetime = Field(description="Date when the test result was completed or started or created", alias="date")
    created_date: datetime = Field(description="Date when the test result has been created", alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, description="Date when the test result has been modified", alias="modifiedDate")
    started_on: Optional[datetime] = Field(default=None, description="Date when the test result has been started", alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, description="Date when the test result has been completed", alias="completedOn")
    duration: Optional[StrictInt] = Field(default=None, description="Time which it took to run the test")
    links: List[LinkShort] = Field(description="Collection of links attached to the test result")
    attachments: List[AttachmentApiResult] = Field(description="Collection of files attached to the test result")
    rerun_completed_count: StrictInt = Field(description="Run count", alias="rerunCompletedCount")
    __properties: ClassVar[List[str]] = ["id", "name", "autotestGlobalId", "testRunId", "configurationId", "configurationName", "outcome", "status", "resultReasons", "comment", "date", "createdDate", "modifiedDate", "startedOn", "completedOn", "duration", "links", "attachments", "rerunCompletedCount"]

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
        """Create an instance of TestResultShortResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in result_reasons (list)
        _items = []
        if self.result_reasons:
            for _item_result_reasons in self.result_reasons:
                if _item_result_reasons:
                    _items.append(_item_result_reasons.to_dict())
            _dict['resultReasons'] = _items
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
        # set to None if outcome (nullable) is None
        # and model_fields_set contains the field
        if self.outcome is None and "outcome" in self.model_fields_set:
            _dict['outcome'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultShortResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "autotestGlobalId": obj.get("autotestGlobalId"),
            "testRunId": obj.get("testRunId"),
            "configurationId": obj.get("configurationId"),
            "configurationName": obj.get("configurationName"),
            "outcome": obj.get("outcome"),
            "status": TestStatusApiResult.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "resultReasons": [AutoTestResultReasonShort.from_dict(_item) for _item in obj["resultReasons"]] if obj.get("resultReasons") is not None else None,
            "comment": obj.get("comment"),
            "date": obj.get("date"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "startedOn": obj.get("startedOn"),
            "completedOn": obj.get("completedOn"),
            "duration": obj.get("duration"),
            "links": [LinkShort.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "attachments": [AttachmentApiResult.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "rerunCompletedCount": obj.get("rerunCompletedCount")
        })
        return _obj


