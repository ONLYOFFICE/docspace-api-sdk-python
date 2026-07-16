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
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class FileKeys(BaseModel):
    """
    FileKeys
    """ # noqa: E501
    user_id: Optional[UUID] = Field(default=None, alias="userId")
    public_key_id: Optional[UUID] = Field(default=None, alias="publicKeyId")
    private_key_enc: Optional[StrictStr] = Field(default=None, alias="privateKeyEnc")
    tenant_id: Optional[StrictInt] = Field(default=None, alias="tenantId")
    file_id: Optional[StrictInt] = Field(default=None, alias="fileId")
    create_on: Optional[datetime] = Field(default=None, alias="createOn")
    __properties: ClassVar[List[str]] = ["userId", "publicKeyId", "privateKeyEnc", "tenantId", "fileId", "createOn"]

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
        """Create an instance of FileKeys from a JSON string"""
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
        # set to None if private_key_enc (nullable) is None
        # and model_fields_set contains the field
        if self.private_key_enc is None and "private_key_enc" in self.model_fields_set:
            _dict['privateKeyEnc'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileKeys from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userId": obj.get("userId"),
            "publicKeyId": obj.get("publicKeyId"),
            "privateKeyEnc": obj.get("privateKeyEnc"),
            "tenantId": obj.get("tenantId"),
            "fileId": obj.get("fileId"),
            "createOn": obj.get("createOn")
        })
        return _obj


