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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.employee_dto import EmployeeDto
from typing import Optional, Set
from typing_extensions import Self

class WebPluginDto(BaseModel):
    """
    One web plugin available to the portal: its manifest, where to load it from, and the state the portal keeps.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(description="The plugin's manifest name, which is what every other operation of this group addresses it by and what  makes it unique within the portal - an installation-wide plugin wins the name over a portal one.", json_schema_extra={"examples": ["Example Plugin"]})
    version: Optional[StrictStr] = Field(description="The plugin's own version from its manifest. The portal does not compare it against anything; it is there  for a person to read.", json_schema_extra={"examples": ["1.0.0"]})
    min_doc_space_version: Optional[StrictStr] = Field(default=None, description="The oldest portal version the plugin declares it works with. It is a claim from the manifest and is not  enforced, so a plugin can be loaded on an older portal and simply misbehave; compare it with the `version`  of `GET api/2.0/settings`.", alias="minDocSpaceVersion", json_schema_extra={"examples": ["12.0.0"]})
    description: Optional[StrictStr] = Field(description="The plugin's description from its manifest, in the language the manifest was written in. The translations  of it are in `descriptionLocale`.", json_schema_extra={"examples": ["A plugin that provides additional functionality"]})
    license: Optional[StrictStr] = Field(description="The licence the plugin is published under, as its manifest states it. Nothing checks it.", json_schema_extra={"examples": ["MIT"]})
    author: Optional[StrictStr] = Field(description="Who wrote the plugin, as its manifest states it - not the portal member who uploaded it, who is  `createBy`.", json_schema_extra={"examples": ["ONLYOFFICE"]})
    home_page: Optional[StrictStr] = Field(description="The plugin's own page, for a person to read more about it. It is empty when the manifest names none.", alias="homePage", json_schema_extra={"examples": ["https://example.com"]})
    plugin_name: Optional[StrictStr] = Field(description="The global the plugin registers itself under in the browser once its script has run, which is how a  client reaches it. It is distinct from `name`, the identifier the portal uses.", alias="pluginName", json_schema_extra={"examples": ["examplePlugin"]})
    scopes: Optional[StrictStr] = Field(description="Which parts of the interface the plugin hooks into, as one comma-separated string rather than a list.", json_schema_extra={"examples": ["Files,Rooms"]})
    image: Optional[StrictStr] = Field(description="The plugin's icon exactly as its manifest declares it, which is normally a file name inside the plugin's  own package rather than an absolute address - resolve it against the directory `url` points into.", json_schema_extra={"examples": ["icon.svg"]})
    create_by: EmployeeDto = Field(description="The portal member who uploaded the plugin. For a plugin that ships with the installation it is an empty  profile, since no member put it there.", alias="createBy")
    create_on: datetime = Field(description="When the plugin was uploaded. It stays at its zero value for a plugin that ships with the installation.", alias="createOn", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    enabled: StrictBool = Field(description="Whether the portal loads the plugin. It is the state this portal stored, so an installation-wide plugin  can be on for one portal and off for another.", json_schema_extra={"examples": [True]})
    system: StrictBool = Field(description="Whether the plugin ships with the installation rather than having been uploaded here. A system plugin  cannot be deleted through `DELETE api/2.0/settings/webplugins/{name}`, only switched off.", json_schema_extra={"examples": [False]})
    url: Optional[StrictStr] = Field(description="The address of the plugin's script, which a client loads to run it. It ends in a `hash` query taken from  `version`, so the address changes whenever the plugin is updated and an old one may be cached.", json_schema_extra={"examples": ["https://example.com/plugin.js"]})
    css_url: Optional[StrictStr] = Field(description="The absolute address of the plugin's stylesheet, empty for a plugin that ships none.", alias="cssUrl", json_schema_extra={"examples": ["https://example.com/plugin.css"]})
    settings: Optional[StrictStr] = Field(description="The settings string the portal keeps for the plugin, stored and returned verbatim - only the plugin knows  its shape. It is empty until `PUT api/2.0/settings/webplugins/{name}` saves one.", json_schema_extra={"examples": ["{\"theme\":\"dark\"}"]})
    name_locale: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="The plugin's name translated, keyed by culture name. A culture that is missing falls back to `name`, and  the whole map is empty for a plugin that ships no translations.", alias="nameLocale", json_schema_extra={"examples": [{"en-US": "Example plugin", "de-DE": "Beispiel-Plugin"}]})
    description_locale: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="The plugin's description translated, keyed the same way as `nameLocale` and falling back to  `description`.", alias="descriptionLocale", json_schema_extra={"examples": [{"en-US": "Adds extra actions", "de-DE": "Fugt Aktionen hinzu"}]})
    runtime: Optional[StrictStr] = Field(default=None, description="How the script at `url` is to be loaded - as an ES module or as a classic script. It is empty for a  plugin whose manifest does not say, which a client treats as a classic script.", json_schema_extra={"examples": ["module"]})
    __properties: ClassVar[List[str]] = ["name", "version", "minDocSpaceVersion", "description", "license", "author", "homePage", "pluginName", "scopes", "image", "createBy", "createOn", "enabled", "system", "url", "cssUrl", "settings", "nameLocale", "descriptionLocale", "runtime"]

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

        # set to None if min_doc_space_version (nullable) is None
        # and model_fields_set contains the field
        if self.min_doc_space_version is None and "min_doc_space_version" in self.model_fields_set:
            _dict['minDocSpaceVersion'] = None

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

        # set to None if css_url (nullable) is None
        # and model_fields_set contains the field
        if self.css_url is None and "css_url" in self.model_fields_set:
            _dict['cssUrl'] = None

        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        # set to None if runtime (nullable) is None
        # and model_fields_set contains the field
        if self.runtime is None and "runtime" in self.model_fields_set:
            _dict['runtime'] = None

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
            "minDocSpaceVersion": obj.get("minDocSpaceVersion"),
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
            "cssUrl": obj.get("cssUrl"),
            "settings": obj.get("settings"),
            "nameLocale": obj.get("nameLocale"),
            "descriptionLocale": obj.get("descriptionLocale"),
            "runtime": obj.get("runtime")
        })
        return _obj


