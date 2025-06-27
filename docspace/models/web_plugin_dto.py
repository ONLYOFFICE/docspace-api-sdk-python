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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace.models.employee_dto import EmployeeDto
from typing import Optional, Set
from typing_extensions import Self

class WebPluginDto(BaseModel):
    """
    The web plugin information.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The web plugin name.")
    version: Optional[StrictStr] = Field(default=None, description="The web plugin version.")
    description: Optional[StrictStr] = Field(default=None, description="The web plugin description.")
    license: Optional[StrictStr] = Field(default=None, description="The web plugin license.")
    author: Optional[StrictStr] = Field(default=None, description="The web plugin author.")
    home_page: Optional[StrictStr] = Field(default=None, description="The web plugin home page URL.", alias="homePage")
    plugin_name: Optional[StrictStr] = Field(default=None, description="The name by which the web plugin is registered in the window object.", alias="pluginName")
    scopes: Optional[StrictStr] = Field(default=None, description="The web plugin scopes.")
    image: Optional[StrictStr] = Field(default=None, description="The web plugin image.")
    create_by: Optional[EmployeeDto] = Field(default=None, alias="createBy")
    create_on: Optional[datetime] = Field(default=None, description="The date and time when the web plugin was created.", alias="createOn")
    enabled: Optional[StrictBool] = Field(default=None, description="Specifies if the web plugin is enabled or not.")
    system: Optional[StrictBool] = Field(default=None, description="Specifies if the web plugin is system or not.")
    url: Optional[StrictStr] = Field(default=None, description="The web plugin URL.")
    settings: Optional[StrictStr] = Field(default=None, description="The web plugin settings.")
    __properties: ClassVar[List[str]] = ["name", "version", "description", "license", "author", "homePage", "pluginName", "scopes", "image", "createBy", "createOn", "enabled", "system", "url", "settings"]

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
        """Create an instance of WebPluginDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of create_by
        if self.create_by:
            _dict['createBy'] = self.create_by.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if license (nullable) is None
        # and model_fields_set contains the field
        if self.license is None and "license" in self.model_fields_set:
            _dict['license'] = None

        # set to None if author (nullable) is None
        # and model_fields_set contains the field
        if self.author is None and "author" in self.model_fields_set:
            _dict['author'] = None

        # set to None if home_page (nullable) is None
        # and model_fields_set contains the field
        if self.home_page is None and "home_page" in self.model_fields_set:
            _dict['homePage'] = None

        # set to None if plugin_name (nullable) is None
        # and model_fields_set contains the field
        if self.plugin_name is None and "plugin_name" in self.model_fields_set:
            _dict['pluginName'] = None

        # set to None if scopes (nullable) is None
        # and model_fields_set contains the field
        if self.scopes is None and "scopes" in self.model_fields_set:
            _dict['scopes'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebPluginDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "version": obj.get("version"),
            "description": obj.get("description"),
            "license": obj.get("license"),
            "author": obj.get("author"),
            "homePage": obj.get("homePage"),
            "pluginName": obj.get("pluginName"),
            "scopes": obj.get("scopes"),
            "image": obj.get("image"),
            "createBy": EmployeeDto.from_dict(obj["createBy"]) if obj.get("createBy") is not None else None,
            "createOn": obj.get("createOn"),
            "enabled": obj.get("enabled"),
            "system": obj.get("system"),
            "url": obj.get("url"),
            "settings": obj.get("settings")
        })
        return _obj


