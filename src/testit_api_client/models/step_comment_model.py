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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.attachment_model import AttachmentModel
from typing import Optional, Set
from typing_extensions import Self

class StepCommentModel(BaseModel):
    """
    StepCommentModel
    """ # noqa: E501
    id: StrictStr
    text: Optional[StrictStr] = None
    step_id: StrictStr = Field(alias="stepId")
    parent_step_id: Optional[StrictStr] = Field(default=None, alias="parentStepId")
    attachments: Optional[List[AttachmentModel]] = None
    test_result_id: StrictStr = Field(alias="testResultId")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    created_date: datetime = Field(alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    __properties: ClassVar[List[str]] = ["id", "text", "stepId", "parentStepId", "attachments", "testResultId", "createdById", "modifiedById", "createdDate", "modifiedDate"]

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
        """Create an instance of StepCommentModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if parent_step_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_step_id is None and "parent_step_id" in self.model_fields_set:
            _dict['parentStepId'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StepCommentModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "text": obj.get("text"),
            "stepId": obj.get("stepId"),
            "parentStepId": obj.get("parentStepId"),
            "attachments": [AttachmentModel.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "testResultId": obj.get("testResultId"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate")
        })
        return _obj

