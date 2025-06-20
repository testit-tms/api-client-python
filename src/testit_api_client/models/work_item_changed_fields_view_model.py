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


from typing import Dict, Optional
from pydantic import BaseModel, Field
from testit_api_client.models.attachment_change_view_model_array_changed_field_view_model import AttachmentChangeViewModelArrayChangedFieldViewModel
from testit_api_client.models.auto_test_change_view_model_array_changed_field_view_model import AutoTestChangeViewModelArrayChangedFieldViewModel
from testit_api_client.models.boolean_changed_field_view_model import BooleanChangedFieldViewModel
from testit_api_client.models.guid_changed_field_view_model import GuidChangedFieldViewModel
from testit_api_client.models.int32_changed_field_view_model import Int32ChangedFieldViewModel
from testit_api_client.models.int64_changed_field_view_model import Int64ChangedFieldViewModel
from testit_api_client.models.string_array_changed_field_view_model import StringArrayChangedFieldViewModel
from testit_api_client.models.string_changed_field_view_model import StringChangedFieldViewModel
from testit_api_client.models.string_changed_field_with_diffs_view_model import StringChangedFieldWithDiffsViewModel
from testit_api_client.models.work_item_changed_attribute_view_model import WorkItemChangedAttributeViewModel
from testit_api_client.models.work_item_link_change_view_model_array_changed_field_view_model import WorkItemLinkChangeViewModelArrayChangedFieldViewModel
from testit_api_client.models.work_item_step_change_view_model_array_changed_field_with_diffs_view_model import WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel

class WorkItemChangedFieldsViewModel(BaseModel):
    """
    WorkItemChangedFieldsViewModel
    """
    name: Optional[StringChangedFieldWithDiffsViewModel] = None
    is_deleted: BooleanChangedFieldViewModel = Field(default=..., alias="isDeleted")
    project_id: GuidChangedFieldViewModel = Field(default=..., alias="projectId")
    is_automated: BooleanChangedFieldViewModel = Field(default=..., alias="isAutomated")
    section_id: GuidChangedFieldViewModel = Field(default=..., alias="sectionId")
    description: Optional[StringChangedFieldWithDiffsViewModel] = None
    state: StringChangedFieldViewModel = Field(...)
    priority: StringChangedFieldViewModel = Field(...)
    duration: Int32ChangedFieldViewModel = Field(...)
    attributes: Dict[str, WorkItemChangedAttributeViewModel] = Field(...)
    steps: WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel = Field(...)
    precondition_steps: WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel = Field(default=..., alias="preconditionSteps")
    postcondition_steps: WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel = Field(default=..., alias="postconditionSteps")
    auto_tests: AutoTestChangeViewModelArrayChangedFieldViewModel = Field(default=..., alias="autoTests")
    attachments: AttachmentChangeViewModelArrayChangedFieldViewModel = Field(...)
    tags: StringArrayChangedFieldViewModel = Field(...)
    links: WorkItemLinkChangeViewModelArrayChangedFieldViewModel = Field(...)
    global_id: Int64ChangedFieldViewModel = Field(default=..., alias="globalId")
    version_number: Int32ChangedFieldViewModel = Field(default=..., alias="versionNumber")
    entity_type_name: StringChangedFieldViewModel = Field(default=..., alias="entityTypeName")
    __properties = ["name", "isDeleted", "projectId", "isAutomated", "sectionId", "description", "state", "priority", "duration", "attributes", "steps", "preconditionSteps", "postconditionSteps", "autoTests", "attachments", "tags", "links", "globalId", "versionNumber", "entityTypeName"]

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
    def from_json(cls, json_str: str) -> WorkItemChangedFieldsViewModel:
        """Create an instance of WorkItemChangedFieldsViewModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_deleted
        if self.is_deleted:
            _dict['isDeleted'] = self.is_deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_id
        if self.project_id:
            _dict['projectId'] = self.project_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_automated
        if self.is_automated:
            _dict['isAutomated'] = self.is_automated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of section_id
        if self.section_id:
            _dict['sectionId'] = self.section_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key in self.attributes:
                if self.attributes[_key]:
                    _field_dict[_key] = self.attributes[_key].to_dict()
            _dict['attributes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of steps
        if self.steps:
            _dict['steps'] = self.steps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of precondition_steps
        if self.precondition_steps:
            _dict['preconditionSteps'] = self.precondition_steps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of postcondition_steps
        if self.postcondition_steps:
            _dict['postconditionSteps'] = self.postcondition_steps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_tests
        if self.auto_tests:
            _dict['autoTests'] = self.auto_tests.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attachments
        if self.attachments:
            _dict['attachments'] = self.attachments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of global_id
        if self.global_id:
            _dict['globalId'] = self.global_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_number
        if self.version_number:
            _dict['versionNumber'] = self.version_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_type_name
        if self.entity_type_name:
            _dict['entityTypeName'] = self.entity_type_name.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkItemChangedFieldsViewModel:
        """Create an instance of WorkItemChangedFieldsViewModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkItemChangedFieldsViewModel.parse_obj(obj)

        _obj = WorkItemChangedFieldsViewModel.parse_obj({
            "name": StringChangedFieldWithDiffsViewModel.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "is_deleted": BooleanChangedFieldViewModel.from_dict(obj.get("isDeleted")) if obj.get("isDeleted") is not None else None,
            "project_id": GuidChangedFieldViewModel.from_dict(obj.get("projectId")) if obj.get("projectId") is not None else None,
            "is_automated": BooleanChangedFieldViewModel.from_dict(obj.get("isAutomated")) if obj.get("isAutomated") is not None else None,
            "section_id": GuidChangedFieldViewModel.from_dict(obj.get("sectionId")) if obj.get("sectionId") is not None else None,
            "description": StringChangedFieldWithDiffsViewModel.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "state": StringChangedFieldViewModel.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "priority": StringChangedFieldViewModel.from_dict(obj.get("priority")) if obj.get("priority") is not None else None,
            "duration": Int32ChangedFieldViewModel.from_dict(obj.get("duration")) if obj.get("duration") is not None else None,
            "attributes": dict(
                (_k, WorkItemChangedAttributeViewModel.from_dict(_v))
                for _k, _v in obj.get("attributes").items()
            )
            if obj.get("attributes") is not None
            else None,
            "steps": WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.from_dict(obj.get("steps")) if obj.get("steps") is not None else None,
            "precondition_steps": WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.from_dict(obj.get("preconditionSteps")) if obj.get("preconditionSteps") is not None else None,
            "postcondition_steps": WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.from_dict(obj.get("postconditionSteps")) if obj.get("postconditionSteps") is not None else None,
            "auto_tests": AutoTestChangeViewModelArrayChangedFieldViewModel.from_dict(obj.get("autoTests")) if obj.get("autoTests") is not None else None,
            "attachments": AttachmentChangeViewModelArrayChangedFieldViewModel.from_dict(obj.get("attachments")) if obj.get("attachments") is not None else None,
            "tags": StringArrayChangedFieldViewModel.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "links": WorkItemLinkChangeViewModelArrayChangedFieldViewModel.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "global_id": Int64ChangedFieldViewModel.from_dict(obj.get("globalId")) if obj.get("globalId") is not None else None,
            "version_number": Int32ChangedFieldViewModel.from_dict(obj.get("versionNumber")) if obj.get("versionNumber") is not None else None,
            "entity_type_name": StringChangedFieldViewModel.from_dict(obj.get("entityTypeName")) if obj.get("entityTypeName") is not None else None
        })
        return _obj


