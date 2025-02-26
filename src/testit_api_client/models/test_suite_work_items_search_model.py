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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.date_time_range_selector_model import DateTimeRangeSelectorModel
from testit_api_client.models.int32_range_selector_model import Int32RangeSelectorModel
from testit_api_client.models.int64_range_selector_model import Int64RangeSelectorModel
from testit_api_client.models.work_item_entity_types import WorkItemEntityTypes
from testit_api_client.models.work_item_link_filter_model import WorkItemLinkFilterModel
from testit_api_client.models.work_item_priority_model import WorkItemPriorityModel
from testit_api_client.models.work_item_states import WorkItemStates
from typing import Optional, Set
from typing_extensions import Self

class TestSuiteWorkItemsSearchModel(BaseModel):
    """
    TestSuiteWorkItemsSearchModel
    """ # noqa: E501
    tag_names: Optional[List[StrictStr]] = Field(default=None, description="Collection of tags", alias="tagNames")
    entity_types: Optional[List[WorkItemEntityTypes]] = Field(default=None, description="Collection of types of work item   Allowed values: `TestCases`, `CheckLists`, `SharedSteps`", alias="entityTypes")
    name_or_id: Optional[StrictStr] = Field(default=None, description="Name or identifier (UUID) of work item", alias="nameOrId")
    include_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of identifiers of work items which need to be included in result regardless of filtering", alias="includeIds")
    exclude_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of identifiers of work items which need to be excluded from result regardless of filtering", alias="excludeIds")
    project_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of project identifiers", alias="projectIds")
    links: Optional[WorkItemLinkFilterModel] = Field(default=None, description="Specifies a work item filter by its links")
    name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Name of work item")
    ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a work item unique IDs to search for")
    global_ids: Optional[List[StrictInt]] = Field(default=None, description="Collection of global (integer) identifiers", alias="globalIds")
    attributes: Optional[Dict[str, Optional[List[StrictStr]]]] = Field(default=None, description="Custom attributes of work item")
    is_deleted: Optional[StrictBool] = Field(default=None, description="Is result must consist of only actual/deleted work items", alias="isDeleted")
    section_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of section identifiers", alias="sectionIds")
    created_by_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of identifiers of users who created work item", alias="createdByIds")
    modified_by_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of identifiers of users who applied last modification to work item", alias="modifiedByIds")
    states: Optional[List[WorkItemStates]] = Field(default=None, description="Collection of states of work item")
    priorities: Optional[List[WorkItemPriorityModel]] = Field(default=None, description="Collection of priorities of work item")
    types: Optional[List[WorkItemEntityTypes]] = Field(default=None, description="Collection of types of work item")
    created_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a work item range of creation date to search for", alias="createdDate")
    modified_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a work item range of last modification date to search for", alias="modifiedDate")
    duration: Optional[Int32RangeSelectorModel] = Field(default=None, description="Specifies a work item duration range to search for")
    median_duration: Optional[Int64RangeSelectorModel] = Field(default=None, description="Specifies a work item median duration range to search for", alias="medianDuration")
    is_automated: Optional[StrictBool] = Field(default=None, description="Is result must consist of only manual/automated work items", alias="isAutomated")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Collection of tags")
    auto_test_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of identifiers of linked autotests", alias="autoTestIds")
    work_item_version_ids: Optional[List[StrictStr]] = Field(default=None, description="Collection of identifiers work items versions.", alias="workItemVersionIds")
    __properties: ClassVar[List[str]] = ["tagNames", "entityTypes", "nameOrId", "includeIds", "excludeIds", "projectIds", "links", "name", "ids", "globalIds", "attributes", "isDeleted", "sectionIds", "createdByIds", "modifiedByIds", "states", "priorities", "types", "createdDate", "modifiedDate", "duration", "medianDuration", "isAutomated", "tags", "autoTestIds", "workItemVersionIds"]

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
        """Create an instance of TestSuiteWorkItemsSearchModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_date
        if self.created_date:
            _dict['createdDate'] = self.created_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_date
        if self.modified_date:
            _dict['modifiedDate'] = self.modified_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of median_duration
        if self.median_duration:
            _dict['medianDuration'] = self.median_duration.to_dict()
        # set to None if tag_names (nullable) is None
        # and model_fields_set contains the field
        if self.tag_names is None and "tag_names" in self.model_fields_set:
            _dict['tagNames'] = None

        # set to None if entity_types (nullable) is None
        # and model_fields_set contains the field
        if self.entity_types is None and "entity_types" in self.model_fields_set:
            _dict['entityTypes'] = None

        # set to None if name_or_id (nullable) is None
        # and model_fields_set contains the field
        if self.name_or_id is None and "name_or_id" in self.model_fields_set:
            _dict['nameOrId'] = None

        # set to None if include_ids (nullable) is None
        # and model_fields_set contains the field
        if self.include_ids is None and "include_ids" in self.model_fields_set:
            _dict['includeIds'] = None

        # set to None if exclude_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_ids is None and "exclude_ids" in self.model_fields_set:
            _dict['excludeIds'] = None

        # set to None if project_ids (nullable) is None
        # and model_fields_set contains the field
        if self.project_ids is None and "project_ids" in self.model_fields_set:
            _dict['projectIds'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        # set to None if global_ids (nullable) is None
        # and model_fields_set contains the field
        if self.global_ids is None and "global_ids" in self.model_fields_set:
            _dict['globalIds'] = None

        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        # set to None if is_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_deleted is None and "is_deleted" in self.model_fields_set:
            _dict['isDeleted'] = None

        # set to None if section_ids (nullable) is None
        # and model_fields_set contains the field
        if self.section_ids is None and "section_ids" in self.model_fields_set:
            _dict['sectionIds'] = None

        # set to None if created_by_ids (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_ids is None and "created_by_ids" in self.model_fields_set:
            _dict['createdByIds'] = None

        # set to None if modified_by_ids (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_ids is None and "modified_by_ids" in self.model_fields_set:
            _dict['modifiedByIds'] = None

        # set to None if states (nullable) is None
        # and model_fields_set contains the field
        if self.states is None and "states" in self.model_fields_set:
            _dict['states'] = None

        # set to None if priorities (nullable) is None
        # and model_fields_set contains the field
        if self.priorities is None and "priorities" in self.model_fields_set:
            _dict['priorities'] = None

        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if median_duration (nullable) is None
        # and model_fields_set contains the field
        if self.median_duration is None and "median_duration" in self.model_fields_set:
            _dict['medianDuration'] = None

        # set to None if is_automated (nullable) is None
        # and model_fields_set contains the field
        if self.is_automated is None and "is_automated" in self.model_fields_set:
            _dict['isAutomated'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if auto_test_ids (nullable) is None
        # and model_fields_set contains the field
        if self.auto_test_ids is None and "auto_test_ids" in self.model_fields_set:
            _dict['autoTestIds'] = None

        # set to None if work_item_version_ids (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_version_ids is None and "work_item_version_ids" in self.model_fields_set:
            _dict['workItemVersionIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestSuiteWorkItemsSearchModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tagNames": obj.get("tagNames"),
            "entityTypes": obj.get("entityTypes"),
            "nameOrId": obj.get("nameOrId"),
            "includeIds": obj.get("includeIds"),
            "excludeIds": obj.get("excludeIds"),
            "projectIds": obj.get("projectIds"),
            "links": WorkItemLinkFilterModel.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "name": obj.get("name"),
            "ids": obj.get("ids"),
            "globalIds": obj.get("globalIds"),
            "attributes": obj.get("attributes"),
            "isDeleted": obj.get("isDeleted"),
            "sectionIds": obj.get("sectionIds"),
            "createdByIds": obj.get("createdByIds"),
            "modifiedByIds": obj.get("modifiedByIds"),
            "states": obj.get("states"),
            "priorities": obj.get("priorities"),
            "types": obj.get("types"),
            "createdDate": DateTimeRangeSelectorModel.from_dict(obj["createdDate"]) if obj.get("createdDate") is not None else None,
            "modifiedDate": DateTimeRangeSelectorModel.from_dict(obj["modifiedDate"]) if obj.get("modifiedDate") is not None else None,
            "duration": Int32RangeSelectorModel.from_dict(obj["duration"]) if obj.get("duration") is not None else None,
            "medianDuration": Int64RangeSelectorModel.from_dict(obj["medianDuration"]) if obj.get("medianDuration") is not None else None,
            "isAutomated": obj.get("isAutomated"),
            "tags": obj.get("tags"),
            "autoTestIds": obj.get("autoTestIds"),
            "workItemVersionIds": obj.get("workItemVersionIds")
        })
        return _obj


