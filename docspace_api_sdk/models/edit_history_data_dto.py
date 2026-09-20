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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.edit_history_url import EditHistoryUrl
from typing import Optional, Set
from typing_extensions import Self

class EditHistoryDataDto(BaseModel):
    """
    Everything an editor needs in order to show what one revision of a file changed.
    """ # noqa: E501
    changes_url: Optional[StrictStr] = Field(default=None, description="The address the editor downloads the recorded changes of this revision from. It is filled in only when the  portal has a change record for the revision; without it the revision can be shown as a whole document but not  as a set of changes.", alias="changesUrl", json_schema_extra={"examples": ["https://example.com/changes"]})
    key: Optional[StrictStr] = Field(description="The document key of the revision being shown, which the editing service uses to identify it and to reuse the  copy it has cached.", json_schema_extra={"examples": ["doc1"]})
    previous: Optional[EditHistoryUrl] = Field(default=None, description="The revision this one is compared against. It arrives together with `changesUrl`, and when the revision shown  is the first one the file ever had, it points at the blank template the file was created from instead of at an  earlier revision.")
    token: Optional[StrictStr] = Field(default=None, description="The signature over the whole answer, as a JSON Web Token that the editing service verifies before it accepts  the addresses in it. Empty when the portal runs without a document-service secret.", json_schema_extra={"examples": ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2ZXJzaW9uIjoxfQ.7HxQ0Zx1"]})
    url: Optional[StrictStr] = Field(description="The address the content of this revision is served from. It is meant for the editing service and carries its  own key, which is valid for a limited time.", json_schema_extra={"examples": ["https://example.com/file.docx"]})
    version: StrictInt = Field(description="Echoes the revision that was asked for, so it reports 0 when the request named no version and the current  revision was taken.", json_schema_extra={"examples": [1]})
    file_type: Optional[StrictStr] = Field(description="The format of the revision being shown, as an extension without the leading dot.", alias="fileType", json_schema_extra={"examples": ["docx"]})
    __properties: ClassVar[List[str]] = ["changesUrl", "key", "previous", "token", "url", "version", "fileType"]

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
        """Create an instance of EditHistoryDataDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of previous
        if self.previous:
            _dict['previous'] = self.previous.to_dict()
        # set to None if changes_url (nullable) is None
        # and model_fields_set contains the field
        if self.changes_url is None and "changes_url" in self.model_fields_set:
            _dict['changesUrl'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if file_type (nullable) is None
        # and model_fields_set contains the field
        if self.file_type is None and "file_type" in self.model_fields_set:
            _dict['fileType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EditHistoryDataDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changesUrl": obj.get("changesUrl"),
            "key": obj.get("key"),
            "previous": EditHistoryUrl.from_dict(obj["previous"]) if obj.get("previous") is not None else None,
            "token": obj.get("token"),
            "url": obj.get("url"),
            "version": obj.get("version"),
            "fileType": obj.get("fileType")
        })
        return _obj


