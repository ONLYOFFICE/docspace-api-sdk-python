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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class EncryptionKeyDto(BaseModel):
    """
    An encryption key pair as the portal reports it: the public half of some member's key, with the encrypted private  half filled in only when the pair belongs to the caller.
    """ # noqa: E501
    id: Optional[UUID] = Field(default=None, description="Names the pair inside its owner's key set. Pass it back to rotate the pair or to delete it; the all-zero value  belongs to a client that stores its keys without sending an identifier.", json_schema_extra={"examples": ["9924256B-447C-4F19-9dbd-8ad8c39e8ff5"]})
    user_id: Optional[UUID] = Field(default=None, description="The member the pair belongs to. In the key set of a room or of a file this is how the caller tells its own  entries, the ones carrying a private half, from those of the other members.", alias="userId", json_schema_extra={"examples": ["9924256B-447C-4F19-9dbd-8ad8c39e8ff5"]})
    var_date: Optional[datetime] = Field(default=None, description="When this key material was written. Rotating the pair refreshes it, so it dates the material that is being  reported rather than the first appearance of the identifier.", alias="date", json_schema_extra={"examples": ["2025-01-01T00:00:00"]})
    public_key: Optional[StrictStr] = Field(default=None, description="The public half of the pair, the half a client encrypts file keys with. A pair whose public half is missing  is treated as no access and left out of a room's or a file's key set.", alias="publicKey", json_schema_extra={"examples": ["MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A..."]})
    private_key_enc: Optional[StrictStr] = Field(default=None, description="The private half, encrypted with its owner's password. It is filled in only when the pair belongs to the  calling user; on another member's entry it comes back empty, because the private half is not handed out.", alias="privateKeyEnc", json_schema_extra={"examples": ["U2FsdGVkX1+Lm3s..."]})
    crypto_engine_id: Optional[StrictStr] = Field(default=None, description="The crypto engine this material was issued for, as a braced GUID. The engine is portal-wide, so the same value  comes back for every key of every member.", alias="cryptoEngineId", json_schema_extra={"examples": ["{DC522726-5E0E-43E5-AA02-8EA156BECBC5}"]})
    __properties: ClassVar[List[str]] = ["id", "userId", "date", "publicKey", "privateKeyEnc", "cryptoEngineId"]

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
        """Create an instance of EncryptionKeyDto from a JSON string"""
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
        # set to None if public_key (nullable) is None
        # and model_fields_set contains the field
        if self.public_key is None and "public_key" in self.model_fields_set:
            _dict['publicKey'] = None

        # set to None if private_key_enc (nullable) is None
        # and model_fields_set contains the field
        if self.private_key_enc is None and "private_key_enc" in self.model_fields_set:
            _dict['privateKeyEnc'] = None

        # set to None if crypto_engine_id (nullable) is None
        # and model_fields_set contains the field
        if self.crypto_engine_id is None and "crypto_engine_id" in self.model_fields_set:
            _dict['cryptoEngineId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EncryptionKeyDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "userId": obj.get("userId"),
            "date": obj.get("date"),
            "publicKey": obj.get("publicKey"),
            "privateKeyEnc": obj.get("privateKeyEnc"),
            "cryptoEngineId": obj.get("cryptoEngineId")
        })
        return _obj


