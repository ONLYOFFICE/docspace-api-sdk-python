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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChunkedUploadSessionResponseInteger(BaseModel):
    """
    Represents the response returned from a chunked upload session.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the entity.", json_schema_extra={"examples": ["0af4bc0d-9a9d-450c-a72b-f14d9ac55c89"]})
    path: Optional[List[StrictInt]] = Field(default=None, description="Represents the hierarchical path of folders associated with a chunked upload session.", json_schema_extra={"examples": [["123", "456", "789"]]})
    created: Optional[datetime] = Field(default=None, description="The timestamp indicating when the chunked upload session was created.", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    expired: Optional[datetime] = Field(default=None, description="The date and time when the chunked upload session is set to expire.", json_schema_extra={"examples": ["2024-01-15T11:30:00Z"]})
    location: Optional[StrictStr] = Field(default=None, description="Represents the URI or path of the chunked upload session's current location.", json_schema_extra={"examples": ["https://example.com/products/files/httphandlers/filehandler.ashx?action=upload"]})
    bytes_total: Optional[StrictInt] = Field(default=None, description="The total size, in bytes, of the file being uploaded in the chunked upload session.", json_schema_extra={"examples": [10485760]})
    __properties: ClassVar[List[str]] = ["id", "path", "created", "expired", "location", "bytes_total"]

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
        """Create an instance of ChunkedUploadSessionResponseInteger from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChunkedUploadSessionResponseInteger from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "created": obj.get("created"),
            "expired": obj.get("expired"),
            "location": obj.get("location"),
            "bytes_total": obj.get("bytes_total")
        })
        return _obj


