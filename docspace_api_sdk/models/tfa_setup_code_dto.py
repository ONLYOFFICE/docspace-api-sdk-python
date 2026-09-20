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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TfaSetupCodeDto(BaseModel):
    """
    The secret to enrol in an authenticator application, in both of the forms an application can take it.
    """ # noqa: E501
    account: Optional[StrictStr] = Field(default=None, description="The label the authenticator application will list the credential under, which is the caller's own email  address. It identifies the entry to a person, and no application checks it.", json_schema_extra={"examples": ["john.doe@onlyoffice.com"]})
    manual_entry_key: Optional[StrictStr] = Field(default=None, description="The secret in the base32 form that is typed into an application by hand. It describes the very same  credential as `qrCodeSetupImageUrl`, and repeating the call hands back the same value for the account until  the credential is reset.", alias="manualEntryKey", json_schema_extra={"examples": ["JBSWY3DPEHPK3PXP"]})
    qr_code_setup_image_url: Optional[StrictStr] = Field(default=None, description="The same secret as a scannable image, given as a `data:image/png;base64,` URL that can be rendered  directly - it is not a link to fetch.", alias="qrCodeSetupImageUrl", json_schema_extra={"examples": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA6fptVAAAACklEQVR4nGMAAgAABAABiCEmiQAAAABJRU5ErkJggg=="]})
    __properties: ClassVar[List[str]] = ["account", "manualEntryKey", "qrCodeSetupImageUrl"]

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
        """Create an instance of TfaSetupCodeDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "account",
            "manual_entry_key",
            "qr_code_setup_image_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if account (nullable) is None
        # and model_fields_set contains the field
        if self.account is None and "account" in self.model_fields_set:
            _dict['account'] = None

        # set to None if manual_entry_key (nullable) is None
        # and model_fields_set contains the field
        if self.manual_entry_key is None and "manual_entry_key" in self.model_fields_set:
            _dict['manualEntryKey'] = None

        # set to None if qr_code_setup_image_url (nullable) is None
        # and model_fields_set contains the field
        if self.qr_code_setup_image_url is None and "qr_code_setup_image_url" in self.model_fields_set:
            _dict['qrCodeSetupImageUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TfaSetupCodeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "manualEntryKey": obj.get("manualEntryKey"),
            "qrCodeSetupImageUrl": obj.get("qrCodeSetupImageUrl")
        })
        return _obj


