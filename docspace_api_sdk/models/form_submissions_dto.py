#
# (c) Copyright Ascensio System SIA 2026
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.form_metadata import FormMetadata
from docspace_api_sdk.models.form_results_dto import FormResultsDto
from typing import Optional, Set
from typing_extensions import Self

class FormSubmissionsDto(BaseModel):
    """
    All submissions of a form, together with the metadata of its fields.
    """ # noqa: E501
    metadata: Optional[List[FormMetadata]] = Field(default=None, description="The form field metadata.", json_schema_extra={"examples": [[]]})
    submissions: Optional[List[FormResultsDto]] = Field(default=None, description="All submissions.", json_schema_extra={"examples": [[]]})
    __properties: ClassVar[List[str]] = ["metadata", "submissions"]

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
        """Create an instance of FormSubmissionsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item_metadata in self.metadata:
                if _item_metadata:
                    _items.append(_item_metadata.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in submissions (list)
        _items = []
        if self.submissions:
            for _item_submissions in self.submissions:
                if _item_submissions:
                    _items.append(_item_submissions.to_dict())
            _dict['submissions'] = _items
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if submissions (nullable) is None
        # and model_fields_set contains the field
        if self.submissions is None and "submissions" in self.model_fields_set:
            _dict['submissions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FormSubmissionsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": [FormMetadata.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None,
            "submissions": [FormResultsDto.from_dict(_item) for _item in obj["submissions"]] if obj.get("submissions") is not None else None
        })
        return _obj


