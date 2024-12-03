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
from testit_api_client.models.iteration_model import IterationModel
from testit_api_client.models.link_short_model import LinkShortModel
from testit_api_client.models.work_item_priority_model import WorkItemPriorityModel
from testit_api_client.models.work_item_states import WorkItemStates
from typing import Optional, Set
from typing_extensions import Self

class WorkItemShortModel(BaseModel):
    """
    WorkItemShortModel
    """ # noqa: E501
    id: StrictStr = Field(description="Work Item internal unique identifier")
    version_id: StrictStr = Field(description="Work Item version identifier", alias="versionId")
    version_number: StrictInt = Field(description="Work Item version number", alias="versionNumber")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Work Item name")
    entity_type_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Work Item type. Possible values: CheckLists, SharedSteps, TestCases", alias="entityTypeName")
    project_id: StrictStr = Field(description="Project unique identifier", alias="projectId")
    section_id: StrictStr = Field(description="Identifier of Section where Work Item is located", alias="sectionId")
    section_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Section name of Work Item", alias="sectionName")
    is_automated: StrictBool = Field(description="Boolean flag determining whether Work Item is automated", alias="isAutomated")
    global_id: StrictInt = Field(description="Work Item global identifier", alias="globalId")
    duration: StrictInt = Field(description="Work Item duration")
    median_duration: Optional[StrictInt] = Field(default=None, description="Work Item median duration", alias="medianDuration")
    attributes: Optional[Dict[str, Any]] = Field(default=None, description="Work Item attributes")
    created_by_id: StrictStr = Field(description="Unique identifier of user who created Work Item", alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of user who applied the latest modification of Work Item", alias="modifiedById")
    created_date: Optional[datetime] = Field(default=None, description="Date and time of Work Item creation", alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, description="Date and time of the latest modification of Work Item", alias="modifiedDate")
    state: WorkItemStates = Field(description="The current state of Work Item")
    priority: WorkItemPriorityModel = Field(description="Work Item priority level")
    is_deleted: StrictBool = Field(description="Flag determining whether Work Item is deleted", alias="isDeleted")
    tag_names: Optional[List[StrictStr]] = Field(default=None, description="Array of tag names of Work Item", alias="tagNames")
    iterations: List[IterationModel] = Field(description="Set of iterations related to Work Item")
    links: List[LinkShortModel] = Field(description="Set of links related to Work Item")
    __properties: ClassVar[List[str]] = ["id", "versionId", "versionNumber", "name", "entityTypeName", "projectId", "sectionId", "sectionName", "isAutomated", "globalId", "duration", "medianDuration", "attributes", "createdById", "modifiedById", "createdDate", "modifiedDate", "state", "priority", "isDeleted", "tagNames", "iterations", "links"]

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
        """Create an instance of WorkItemShortModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in iterations (list)
        _items = []
        if self.iterations:
            for _item_iterations in self.iterations:
                if _item_iterations:
                    _items.append(_item_iterations.to_dict())
            _dict['iterations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # set to None if median_duration (nullable) is None
        # and model_fields_set contains the field
        if self.median_duration is None and "median_duration" in self.model_fields_set:
            _dict['medianDuration'] = None

        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if tag_names (nullable) is None
        # and model_fields_set contains the field
        if self.tag_names is None and "tag_names" in self.model_fields_set:
            _dict['tagNames'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkItemShortModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "versionId": obj.get("versionId"),
            "versionNumber": obj.get("versionNumber"),
            "name": obj.get("name"),
            "entityTypeName": obj.get("entityTypeName"),
            "projectId": obj.get("projectId"),
            "sectionId": obj.get("sectionId"),
            "sectionName": obj.get("sectionName"),
            "isAutomated": obj.get("isAutomated"),
            "globalId": obj.get("globalId"),
            "duration": obj.get("duration"),
            "medianDuration": obj.get("medianDuration"),
            "attributes": obj.get("attributes"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "state": obj.get("state"),
            "priority": obj.get("priority"),
            "isDeleted": obj.get("isDeleted"),
            "tagNames": obj.get("tagNames"),
            "iterations": [IterationModel.from_dict(_item) for _item in obj["iterations"]] if obj.get("iterations") is not None else None,
            "links": [LinkShortModel.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj

