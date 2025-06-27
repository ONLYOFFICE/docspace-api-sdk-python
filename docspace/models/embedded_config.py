# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EmbeddedConfig(BaseModel):
    """
    The configuration parameters for the embedded document type.
    """ # noqa: E501
    embed_url: Optional[StrictStr] = Field(default=None, description="The absolute URL to the document serving as a source file for the document embedded into the web page.", alias="embedUrl")
    save_url: Optional[StrictStr] = Field(default=None, description="The absolute URL that will allow the document to be saved onto the user personal computer.", alias="saveUrl")
    share_link_param: Optional[StrictStr] = Field(default=None, description="The shared URL parameter.", alias="shareLinkParam")
    share_url: Optional[StrictStr] = Field(default=None, description="The absolute URL that will allow other users to share this document.", alias="shareUrl")
    toolbar_docked: Optional[StrictStr] = Field(default=None, description="The place for the embedded viewer toolbar, can be either \"top\" or \"bottom\".", alias="toolbarDocked")
    __properties: ClassVar[List[str]] = ["embedUrl", "saveUrl", "shareLinkParam", "shareUrl", "toolbarDocked"]

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
        """Create an instance of EmbeddedConfig from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "save_url",
            "toolbar_docked",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if embed_url (nullable) is None
        # and model_fields_set contains the field
        if self.embed_url is None and "embed_url" in self.model_fields_set:
            _dict['embedUrl'] = None

        # set to None if save_url (nullable) is None
        # and model_fields_set contains the field
        if self.save_url is None and "save_url" in self.model_fields_set:
            _dict['saveUrl'] = None

        # set to None if share_link_param (nullable) is None
        # and model_fields_set contains the field
        if self.share_link_param is None and "share_link_param" in self.model_fields_set:
            _dict['shareLinkParam'] = None

        # set to None if share_url (nullable) is None
        # and model_fields_set contains the field
        if self.share_url is None and "share_url" in self.model_fields_set:
            _dict['shareUrl'] = None

        # set to None if toolbar_docked (nullable) is None
        # and model_fields_set contains the field
        if self.toolbar_docked is None and "toolbar_docked" in self.model_fields_set:
            _dict['toolbarDocked'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmbeddedConfig from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "embedUrl": obj.get("embedUrl"),
            "saveUrl": obj.get("saveUrl"),
            "shareLinkParam": obj.get("shareLinkParam"),
            "shareUrl": obj.get("shareUrl"),
            "toolbarDocked": obj.get("toolbarDocked")
        })
        return _obj


