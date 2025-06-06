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
from testit_api_client.models.int64_range_selector_model import Int64RangeSelectorModel
from testit_api_client.models.test_point_status import TestPointStatus
from testit_api_client.models.work_item_priority_model import WorkItemPriorityModel
from typing import Optional, Set
from typing_extensions import Self

class TestPlanTestPointsSearchApiModel(BaseModel):
    """
    TestPlanTestPointsSearchApiModel
    """ # noqa: E501
    test_suite_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point test suite IDs to search for", alias="testSuiteIds")
    work_item_global_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies a test point work item global IDs to search for", alias="workItemGlobalIds")
    work_item_median_duration: Optional[Int64RangeSelectorModel] = Field(default=None, description="Specifies a test point work item median duration range to search for", alias="workItemMedianDuration")
    statuses: Optional[List[TestPointStatus]] = Field(default=None, description="Specifies a test point statuses to search for")
    status_codes: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point status codes to search for", alias="statusCodes")
    priorities: Optional[List[WorkItemPriorityModel]] = Field(default=None, description="Specifies a test point priorities to search for")
    is_automated: Optional[StrictBool] = Field(default=None, description="Specifies a test point automation status to search for", alias="isAutomated")
    name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Specifies a test point name to search for")
    configuration_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point configuration IDs to search for", alias="configurationIds")
    tester_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point assigned user IDs to search for", alias="testerIds")
    duration: Optional[Int64RangeSelectorModel] = Field(default=None, description="Specifies a test point range of duration to search for")
    section_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point work item section IDs to search for", alias="sectionIds")
    created_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a test point range of creation date to search for", alias="createdDate")
    created_by_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point creator IDs to search for", alias="createdByIds")
    modified_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a test point range of last modification date to search for", alias="modifiedDate")
    modified_by_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point last editor IDs to search for", alias="modifiedByIds")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Specifies a test point tags to search for")
    attributes: Optional[Dict[str, Optional[List[StrictStr]]]] = Field(default=None, description="Specifies a test point attributes to search for")
    work_item_created_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a work item range of creation date to search for", alias="workItemCreatedDate")
    work_item_created_by_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a work item creator IDs to search for", alias="workItemCreatedByIds")
    work_item_modified_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, description="Specifies a work item range of last modification date to search for", alias="workItemModifiedDate")
    work_item_modified_by_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a work item last editor IDs to search for", alias="workItemModifiedByIds")
    __properties: ClassVar[List[str]] = ["testSuiteIds", "workItemGlobalIds", "workItemMedianDuration", "statuses", "statusCodes", "priorities", "isAutomated", "name", "configurationIds", "testerIds", "duration", "sectionIds", "createdDate", "createdByIds", "modifiedDate", "modifiedByIds", "tags", "attributes", "workItemCreatedDate", "workItemCreatedByIds", "workItemModifiedDate", "workItemModifiedByIds"]

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
        """Create an instance of TestPlanTestPointsSearchApiModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of work_item_median_duration
        if self.work_item_median_duration:
            _dict['workItemMedianDuration'] = self.work_item_median_duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_date
        if self.created_date:
            _dict['createdDate'] = self.created_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_date
        if self.modified_date:
            _dict['modifiedDate'] = self.modified_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_item_created_date
        if self.work_item_created_date:
            _dict['workItemCreatedDate'] = self.work_item_created_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_item_modified_date
        if self.work_item_modified_date:
            _dict['workItemModifiedDate'] = self.work_item_modified_date.to_dict()
        # set to None if test_suite_ids (nullable) is None
        # and model_fields_set contains the field
        if self.test_suite_ids is None and "test_suite_ids" in self.model_fields_set:
            _dict['testSuiteIds'] = None

        # set to None if work_item_global_ids (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_global_ids is None and "work_item_global_ids" in self.model_fields_set:
            _dict['workItemGlobalIds'] = None

        # set to None if work_item_median_duration (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_median_duration is None and "work_item_median_duration" in self.model_fields_set:
            _dict['workItemMedianDuration'] = None

        # set to None if statuses (nullable) is None
        # and model_fields_set contains the field
        if self.statuses is None and "statuses" in self.model_fields_set:
            _dict['statuses'] = None

        # set to None if status_codes (nullable) is None
        # and model_fields_set contains the field
        if self.status_codes is None and "status_codes" in self.model_fields_set:
            _dict['statusCodes'] = None

        # set to None if priorities (nullable) is None
        # and model_fields_set contains the field
        if self.priorities is None and "priorities" in self.model_fields_set:
            _dict['priorities'] = None

        # set to None if is_automated (nullable) is None
        # and model_fields_set contains the field
        if self.is_automated is None and "is_automated" in self.model_fields_set:
            _dict['isAutomated'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if configuration_ids (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_ids is None and "configuration_ids" in self.model_fields_set:
            _dict['configurationIds'] = None

        # set to None if tester_ids (nullable) is None
        # and model_fields_set contains the field
        if self.tester_ids is None and "tester_ids" in self.model_fields_set:
            _dict['testerIds'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if section_ids (nullable) is None
        # and model_fields_set contains the field
        if self.section_ids is None and "section_ids" in self.model_fields_set:
            _dict['sectionIds'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if created_by_ids (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_ids is None and "created_by_ids" in self.model_fields_set:
            _dict['createdByIds'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if modified_by_ids (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_ids is None and "modified_by_ids" in self.model_fields_set:
            _dict['modifiedByIds'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        # set to None if work_item_created_date (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_created_date is None and "work_item_created_date" in self.model_fields_set:
            _dict['workItemCreatedDate'] = None

        # set to None if work_item_created_by_ids (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_created_by_ids is None and "work_item_created_by_ids" in self.model_fields_set:
            _dict['workItemCreatedByIds'] = None

        # set to None if work_item_modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_modified_date is None and "work_item_modified_date" in self.model_fields_set:
            _dict['workItemModifiedDate'] = None

        # set to None if work_item_modified_by_ids (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_modified_by_ids is None and "work_item_modified_by_ids" in self.model_fields_set:
            _dict['workItemModifiedByIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestPlanTestPointsSearchApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "testSuiteIds": obj.get("testSuiteIds"),
            "workItemGlobalIds": obj.get("workItemGlobalIds"),
            "workItemMedianDuration": Int64RangeSelectorModel.from_dict(obj["workItemMedianDuration"]) if obj.get("workItemMedianDuration") is not None else None,
            "statuses": obj.get("statuses"),
            "statusCodes": obj.get("statusCodes"),
            "priorities": obj.get("priorities"),
            "isAutomated": obj.get("isAutomated"),
            "name": obj.get("name"),
            "configurationIds": obj.get("configurationIds"),
            "testerIds": obj.get("testerIds"),
            "duration": Int64RangeSelectorModel.from_dict(obj["duration"]) if obj.get("duration") is not None else None,
            "sectionIds": obj.get("sectionIds"),
            "createdDate": DateTimeRangeSelectorModel.from_dict(obj["createdDate"]) if obj.get("createdDate") is not None else None,
            "createdByIds": obj.get("createdByIds"),
            "modifiedDate": DateTimeRangeSelectorModel.from_dict(obj["modifiedDate"]) if obj.get("modifiedDate") is not None else None,
            "modifiedByIds": obj.get("modifiedByIds"),
            "tags": obj.get("tags"),
            "attributes": obj.get("attributes"),
            "workItemCreatedDate": DateTimeRangeSelectorModel.from_dict(obj["workItemCreatedDate"]) if obj.get("workItemCreatedDate") is not None else None,
            "workItemCreatedByIds": obj.get("workItemCreatedByIds"),
            "workItemModifiedDate": DateTimeRangeSelectorModel.from_dict(obj["workItemModifiedDate"]) if obj.get("workItemModifiedDate") is not None else None,
            "workItemModifiedByIds": obj.get("workItemModifiedByIds")
        })
        return _obj


