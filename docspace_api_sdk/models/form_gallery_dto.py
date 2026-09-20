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

class FormGalleryDto(BaseModel):
    """
    Where the ready-made form templates are served from, for browsing them and for submitting new ones.
    """ # noqa: E501
    path: Optional[StrictStr] = Field(description="The path under `domain` that the gallery's own listing API is reached at. It is joined to `domain` by the  client; the portal only relays the values from its configuration.", json_schema_extra={"examples": ["/forms/templates"]})
    domain: Optional[StrictStr] = Field(description="The address of the gallery service, which is a service of the vendor rather than part of the portal. Every  field of this object is empty on an installation that configures no gallery, and a client should then not  offer the gallery at all.", json_schema_extra={"examples": ["https://forms.example.com"]})
    ext: Optional[StrictStr] = Field(description="The file extension to ask the gallery for, which decides which rendition of a template is downloaded when  several are published.", json_schema_extra={"examples": [".docxf"]})
    upload_path: Optional[StrictStr] = Field(description="The path used for submitting a form of one's own to the gallery, the counterpart of `path` for the upload  side. The four `upload` fields are empty when the installation allows browsing but not submitting.", alias="uploadPath", json_schema_extra={"examples": ["/forms/upload"]})
    upload_domain: Optional[StrictStr] = Field(description="The address the submission is sent to, which may differ from `domain`.", alias="uploadDomain", json_schema_extra={"examples": ["https://upload.forms.example.com"]})
    upload_ext: Optional[StrictStr] = Field(description="The file extension a submitted form has to carry.", alias="uploadExt", json_schema_extra={"examples": [".docxf"]})
    upload_dashboard: Optional[StrictStr] = Field(description="The page a person is sent to in order to follow up on a submission, joined to `uploadDomain` the same way  as `uploadPath`.", alias="uploadDashboard", json_schema_extra={"examples": ["/dashboard/forms"]})
    __properties: ClassVar[List[str]] = ["path", "domain", "ext", "uploadPath", "uploadDomain", "uploadExt", "uploadDashboard"]

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
        """Create an instance of FormGalleryDto from a JSON string"""
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
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if ext (nullable) is None
        # and model_fields_set contains the field
        if self.ext is None and "ext" in self.model_fields_set:
            _dict['ext'] = None

        # set to None if upload_path (nullable) is None
        # and model_fields_set contains the field
        if self.upload_path is None and "upload_path" in self.model_fields_set:
            _dict['uploadPath'] = None

        # set to None if upload_domain (nullable) is None
        # and model_fields_set contains the field
        if self.upload_domain is None and "upload_domain" in self.model_fields_set:
            _dict['uploadDomain'] = None

        # set to None if upload_ext (nullable) is None
        # and model_fields_set contains the field
        if self.upload_ext is None and "upload_ext" in self.model_fields_set:
            _dict['uploadExt'] = None

        # set to None if upload_dashboard (nullable) is None
        # and model_fields_set contains the field
        if self.upload_dashboard is None and "upload_dashboard" in self.model_fields_set:
            _dict['uploadDashboard'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FormGalleryDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "path": obj.get("path"),
            "domain": obj.get("domain"),
            "ext": obj.get("ext"),
            "uploadPath": obj.get("uploadPath"),
            "uploadDomain": obj.get("uploadDomain"),
            "uploadExt": obj.get("uploadExt"),
            "uploadDashboard": obj.get("uploadDashboard")
        })
        return _obj


