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
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from docspace_api_sdk.models.file_share import FileShare
from typing import Optional, Set
from typing_extensions import Self

class FolderLinkRequest(BaseModel):
    """
    The folder link parameters.
    """ # noqa: E501
    link_id: Optional[UUID] = Field(default=None, description="The folder link ID.", alias="linkId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    access: Optional[FileShare] = Field(default=None, description="The link sharing rights.")
    expiration_date: Optional[datetime] = Field(default=None, description="The link expiration date.", alias="expirationDate", json_schema_extra={"examples": ["2021-01-01T00:00:00Z"]})
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The link name.", json_schema_extra={"examples": ["My Document"]})
    password: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The link password.", json_schema_extra={"examples": ["p@ssw0rd"]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Specifies if downloading the file from the link is disabled or not.", alias="denyDownload", json_schema_extra={"examples": [False]})
    internal: Optional[StrictBool] = Field(default=None, description="The link scope, whether it is internal or not.", json_schema_extra={"examples": [False]})
    primary: Optional[StrictBool] = Field(default=None, description="Specifies whether the folder link is primary or not.", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["linkId", "access", "expirationDate", "title", "password", "denyDownload", "internal", "primary"]

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
        """Create an instance of FolderLinkRequest from a JSON string"""
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
        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expirationDate'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FolderLinkRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkId": obj.get("linkId"),
            "access": obj.get("access"),
            "expirationDate": obj.get("expirationDate"),
            "title": obj.get("title"),
            "password": obj.get("password"),
            "denyDownload": obj.get("denyDownload"),
            "internal": obj.get("internal"),
            "primary": obj.get("primary")
        })
        return _obj


