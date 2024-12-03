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
from typing_extensions import Annotated
from testit_api_client.models.auto_test_model import AutoTestModel
from testit_api_client.models.test_plan_model import TestPlanModel
from testit_api_client.models.test_result_model import TestResultModel
from testit_api_client.models.test_run_analytic_result_model import TestRunAnalyticResultModel
from testit_api_client.models.test_run_state import TestRunState
from typing import Optional, Set
from typing_extensions import Self

class TestRunModel(BaseModel):
    """
    TestRunModel
    """ # noqa: E501
    auto_tests: Optional[List[AutoTestModel]] = Field(default=None, alias="autoTests")
    auto_tests_count: StrictInt = Field(alias="autoTestsCount")
    test_suite_ids: Optional[List[StrictStr]] = Field(default=None, alias="testSuiteIds")
    is_automated: StrictBool = Field(alias="isAutomated")
    analytic: TestRunAnalyticResultModel
    test_results: Optional[List[TestResultModel]] = Field(default=None, alias="testResults")
    test_plan: Optional[TestPlanModel] = Field(default=None, alias="testPlan")
    created_date: datetime = Field(alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    created_by_user_name: Optional[StrictStr] = Field(default=None, alias="createdByUserName")
    started_date: Optional[datetime] = Field(default=None, alias="startedDate")
    completed_date: Optional[datetime] = Field(default=None, alias="completedDate")
    build: Annotated[str, Field(min_length=0, strict=True, max_length=450)]
    description: StrictStr
    state_name: TestRunState = Field(alias="stateName")
    project_id: StrictStr = Field(alias="projectId")
    test_plan_id: Optional[StrictStr] = Field(default=None, alias="testPlanId")
    run_by_user_id: Optional[StrictStr] = Field(default=None, alias="runByUserId")
    stopped_by_user_id: Optional[StrictStr] = Field(default=None, alias="stoppedByUserId")
    name: StrictStr
    launch_source: StrictStr = Field(alias="launchSource")
    id: StrictStr = Field(description="Unique ID of the entity")
    is_deleted: StrictBool = Field(description="Indicates if the entity is deleted", alias="isDeleted")
    __properties: ClassVar[List[str]] = ["autoTests", "autoTestsCount", "testSuiteIds", "isAutomated", "analytic", "testResults", "testPlan", "createdDate", "modifiedDate", "createdById", "modifiedById", "createdByUserName", "startedDate", "completedDate", "build", "description", "stateName", "projectId", "testPlanId", "runByUserId", "stoppedByUserId", "name", "launchSource", "id", "isDeleted"]

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
        """Create an instance of TestRunModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in auto_tests (list)
        _items = []
        if self.auto_tests:
            for _item_auto_tests in self.auto_tests:
                if _item_auto_tests:
                    _items.append(_item_auto_tests.to_dict())
            _dict['autoTests'] = _items
        # override the default output from pydantic by calling `to_dict()` of analytic
        if self.analytic:
            _dict['analytic'] = self.analytic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in test_results (list)
        _items = []
        if self.test_results:
            for _item_test_results in self.test_results:
                if _item_test_results:
                    _items.append(_item_test_results.to_dict())
            _dict['testResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of test_plan
        if self.test_plan:
            _dict['testPlan'] = self.test_plan.to_dict()
        # set to None if auto_tests (nullable) is None
        # and model_fields_set contains the field
        if self.auto_tests is None and "auto_tests" in self.model_fields_set:
            _dict['autoTests'] = None

        # set to None if test_suite_ids (nullable) is None
        # and model_fields_set contains the field
        if self.test_suite_ids is None and "test_suite_ids" in self.model_fields_set:
            _dict['testSuiteIds'] = None

        # set to None if test_results (nullable) is None
        # and model_fields_set contains the field
        if self.test_results is None and "test_results" in self.model_fields_set:
            _dict['testResults'] = None

        # set to None if test_plan (nullable) is None
        # and model_fields_set contains the field
        if self.test_plan is None and "test_plan" in self.model_fields_set:
            _dict['testPlan'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if created_by_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_user_name is None and "created_by_user_name" in self.model_fields_set:
            _dict['createdByUserName'] = None

        # set to None if started_date (nullable) is None
        # and model_fields_set contains the field
        if self.started_date is None and "started_date" in self.model_fields_set:
            _dict['startedDate'] = None

        # set to None if completed_date (nullable) is None
        # and model_fields_set contains the field
        if self.completed_date is None and "completed_date" in self.model_fields_set:
            _dict['completedDate'] = None

        # set to None if test_plan_id (nullable) is None
        # and model_fields_set contains the field
        if self.test_plan_id is None and "test_plan_id" in self.model_fields_set:
            _dict['testPlanId'] = None

        # set to None if run_by_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_by_user_id is None and "run_by_user_id" in self.model_fields_set:
            _dict['runByUserId'] = None

        # set to None if stopped_by_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.stopped_by_user_id is None and "stopped_by_user_id" in self.model_fields_set:
            _dict['stoppedByUserId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestRunModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoTests": [AutoTestModel.from_dict(_item) for _item in obj["autoTests"]] if obj.get("autoTests") is not None else None,
            "autoTestsCount": obj.get("autoTestsCount"),
            "testSuiteIds": obj.get("testSuiteIds"),
            "isAutomated": obj.get("isAutomated"),
            "analytic": TestRunAnalyticResultModel.from_dict(obj["analytic"]) if obj.get("analytic") is not None else None,
            "testResults": [TestResultModel.from_dict(_item) for _item in obj["testResults"]] if obj.get("testResults") is not None else None,
            "testPlan": TestPlanModel.from_dict(obj["testPlan"]) if obj.get("testPlan") is not None else None,
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "createdByUserName": obj.get("createdByUserName"),
            "startedDate": obj.get("startedDate"),
            "completedDate": obj.get("completedDate"),
            "build": obj.get("build"),
            "description": obj.get("description"),
            "stateName": obj.get("stateName"),
            "projectId": obj.get("projectId"),
            "testPlanId": obj.get("testPlanId"),
            "runByUserId": obj.get("runByUserId"),
            "stoppedByUserId": obj.get("stoppedByUserId"),
            "name": obj.get("name"),
            "launchSource": obj.get("launchSource"),
            "id": obj.get("id"),
            "isDeleted": obj.get("isDeleted")
        })
        return _obj

