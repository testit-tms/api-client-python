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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from testit_api_client.models.project_type_model import ProjectTypeModel

class ProjectShortModel(BaseModel):
    """
    ProjectShortModel
    """
    id: StrictStr = Field(default=..., description="Unique ID of the project")
    description: Optional[StrictStr] = Field(default=None, description="Description of the project")
    name: StrictStr = Field(default=..., description="Name of the project")
    is_favorite: StrictBool = Field(default=..., alias="isFavorite", description="Indicates if the project is marked as favorite")
    test_cases_count: Optional[StrictInt] = Field(default=None, alias="testCasesCount", description="Number of test cases in the project")
    shared_steps_count: Optional[StrictInt] = Field(default=None, alias="sharedStepsCount", description="Number of shared steps in the project")
    check_lists_count: Optional[StrictInt] = Field(default=None, alias="checkListsCount", description="Number of checklists in the project")
    auto_tests_count: Optional[StrictInt] = Field(default=None, alias="autoTestsCount", description="Number of autotests in the project")
    is_deleted: StrictBool = Field(default=..., alias="isDeleted", description="Indicates if the project is deleted")
    created_date: datetime = Field(default=..., alias="createdDate", description="Creation date of the project")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate", description="Last modification date of the project")
    created_by_id: StrictStr = Field(default=..., alias="createdById", description="Unique ID of the project creator")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById", description="Unique ID of the project last editor")
    global_id: StrictInt = Field(default=..., alias="globalId", description="Global ID of the project")
    type: ProjectTypeModel = Field(default=..., description="Type of the project")
    is_flaky_auto: StrictBool = Field(default=..., alias="isFlakyAuto", description="Indicates if the status \"Flaky/Stable\" sets automatically")
    workflow_id: StrictStr = Field(default=..., alias="workflowId")
    __properties = ["id", "description", "name", "isFavorite", "testCasesCount", "sharedStepsCount", "checkListsCount", "autoTestsCount", "isDeleted", "createdDate", "modifiedDate", "createdById", "modifiedById", "globalId", "type", "isFlakyAuto", "workflowId"]

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
    def from_json(cls, json_str: str) -> ProjectShortModel:
        """Create an instance of ProjectShortModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if test_cases_count (nullable) is None
        # and __fields_set__ contains the field
        if self.test_cases_count is None and "test_cases_count" in self.__fields_set__:
            _dict['testCasesCount'] = None

        # set to None if shared_steps_count (nullable) is None
        # and __fields_set__ contains the field
        if self.shared_steps_count is None and "shared_steps_count" in self.__fields_set__:
            _dict['sharedStepsCount'] = None

        # set to None if check_lists_count (nullable) is None
        # and __fields_set__ contains the field
        if self.check_lists_count is None and "check_lists_count" in self.__fields_set__:
            _dict['checkListsCount'] = None

        # set to None if auto_tests_count (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_tests_count is None and "auto_tests_count" in self.__fields_set__:
            _dict['autoTestsCount'] = None

        # set to None if modified_date (nullable) is None
        # and __fields_set__ contains the field
        if self.modified_date is None and "modified_date" in self.__fields_set__:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and __fields_set__ contains the field
        if self.modified_by_id is None and "modified_by_id" in self.__fields_set__:
            _dict['modifiedById'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectShortModel:
        """Create an instance of ProjectShortModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProjectShortModel.parse_obj(obj)

        _obj = ProjectShortModel.parse_obj({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "name": obj.get("name"),
            "is_favorite": obj.get("isFavorite"),
            "test_cases_count": obj.get("testCasesCount"),
            "shared_steps_count": obj.get("sharedStepsCount"),
            "check_lists_count": obj.get("checkListsCount"),
            "auto_tests_count": obj.get("autoTestsCount"),
            "is_deleted": obj.get("isDeleted"),
            "created_date": obj.get("createdDate"),
            "modified_date": obj.get("modifiedDate"),
            "created_by_id": obj.get("createdById"),
            "modified_by_id": obj.get("modifiedById"),
            "global_id": obj.get("globalId"),
            "type": obj.get("type"),
            "is_flaky_auto": obj.get("isFlakyAuto"),
            "workflow_id": obj.get("workflowId")
        })
        return _obj


