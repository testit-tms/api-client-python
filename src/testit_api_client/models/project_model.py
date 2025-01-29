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
from testit_api_client.models.custom_attribute_model import CustomAttributeModel
from testit_api_client.models.project_type_model import ProjectTypeModel
from typing import Optional, Set
from typing_extensions import Self

class ProjectModel(BaseModel):
    """
    ProjectModel
    """ # noqa: E501
    id: StrictStr = Field(description="Unique ID of the project")
    description: Optional[StrictStr] = Field(default=None, description="Description of the project")
    name: StrictStr = Field(description="Name of the project")
    is_favorite: StrictBool = Field(description="Indicates if the project is marked as favorite", alias="isFavorite")
    attributes_scheme: Optional[List[CustomAttributeModel]] = Field(default=None, description="Collection of the project attributes", alias="attributesScheme")
    test_plans_attributes_scheme: Optional[List[CustomAttributeModel]] = Field(default=None, description="Collection of the project test plans attributes", alias="testPlansAttributesScheme")
    test_cases_count: Optional[StrictInt] = Field(default=None, description="Number of test cases in the project", alias="testCasesCount")
    shared_steps_count: Optional[StrictInt] = Field(default=None, description="Number of shared steps in the project", alias="sharedStepsCount")
    check_lists_count: Optional[StrictInt] = Field(default=None, description="Number of checklists in the project", alias="checkListsCount")
    auto_tests_count: Optional[StrictInt] = Field(default=None, description="Number of autotests in the project", alias="autoTestsCount")
    is_deleted: StrictBool = Field(description="Indicates if the project is deleted", alias="isDeleted")
    created_date: datetime = Field(description="Creation date of the project", alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, description="Last modification date of the project", alias="modifiedDate")
    created_by_id: StrictStr = Field(description="Unique ID of the project creator", alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the project last editor", alias="modifiedById")
    global_id: StrictInt = Field(description="Global ID of the project", alias="globalId")
    type: ProjectTypeModel = Field(description="Type of the project")
    __properties: ClassVar[List[str]] = ["id", "description", "name", "isFavorite", "attributesScheme", "testPlansAttributesScheme", "testCasesCount", "sharedStepsCount", "checkListsCount", "autoTestsCount", "isDeleted", "createdDate", "modifiedDate", "createdById", "modifiedById", "globalId", "type"]

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
        """Create an instance of ProjectModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes_scheme (list)
        _items = []
        if self.attributes_scheme:
            for _item_attributes_scheme in self.attributes_scheme:
                if _item_attributes_scheme:
                    _items.append(_item_attributes_scheme.to_dict())
            _dict['attributesScheme'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in test_plans_attributes_scheme (list)
        _items = []
        if self.test_plans_attributes_scheme:
            for _item_test_plans_attributes_scheme in self.test_plans_attributes_scheme:
                if _item_test_plans_attributes_scheme:
                    _items.append(_item_test_plans_attributes_scheme.to_dict())
            _dict['testPlansAttributesScheme'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if attributes_scheme (nullable) is None
        # and model_fields_set contains the field
        if self.attributes_scheme is None and "attributes_scheme" in self.model_fields_set:
            _dict['attributesScheme'] = None

        # set to None if test_plans_attributes_scheme (nullable) is None
        # and model_fields_set contains the field
        if self.test_plans_attributes_scheme is None and "test_plans_attributes_scheme" in self.model_fields_set:
            _dict['testPlansAttributesScheme'] = None

        # set to None if test_cases_count (nullable) is None
        # and model_fields_set contains the field
        if self.test_cases_count is None and "test_cases_count" in self.model_fields_set:
            _dict['testCasesCount'] = None

        # set to None if shared_steps_count (nullable) is None
        # and model_fields_set contains the field
        if self.shared_steps_count is None and "shared_steps_count" in self.model_fields_set:
            _dict['sharedStepsCount'] = None

        # set to None if check_lists_count (nullable) is None
        # and model_fields_set contains the field
        if self.check_lists_count is None and "check_lists_count" in self.model_fields_set:
            _dict['checkListsCount'] = None

        # set to None if auto_tests_count (nullable) is None
        # and model_fields_set contains the field
        if self.auto_tests_count is None and "auto_tests_count" in self.model_fields_set:
            _dict['autoTestsCount'] = None

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
        """Create an instance of ProjectModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "name": obj.get("name"),
            "isFavorite": obj.get("isFavorite"),
            "attributesScheme": [CustomAttributeModel.from_dict(_item) for _item in obj["attributesScheme"]] if obj.get("attributesScheme") is not None else None,
            "testPlansAttributesScheme": [CustomAttributeModel.from_dict(_item) for _item in obj["testPlansAttributesScheme"]] if obj.get("testPlansAttributesScheme") is not None else None,
            "testCasesCount": obj.get("testCasesCount"),
            "sharedStepsCount": obj.get("sharedStepsCount"),
            "checkListsCount": obj.get("checkListsCount"),
            "autoTestsCount": obj.get("autoTestsCount"),
            "isDeleted": obj.get("isDeleted"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "globalId": obj.get("globalId"),
            "type": obj.get("type")
        })
        return _obj


