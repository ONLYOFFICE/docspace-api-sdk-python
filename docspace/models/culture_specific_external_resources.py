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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from docspace.models.culture_specific_external_resource import CultureSpecificExternalResource
from typing import Optional, Set
from typing_extensions import Self

class CultureSpecificExternalResources(BaseModel):
    """
    The external resources settings.
    """ # noqa: E501
    api: Optional[CultureSpecificExternalResource] = None
    common: Optional[CultureSpecificExternalResource] = None
    forum: Optional[CultureSpecificExternalResource] = None
    helpcenter: Optional[CultureSpecificExternalResource] = None
    integrations: Optional[CultureSpecificExternalResource] = None
    site: Optional[CultureSpecificExternalResource] = None
    social_networks: Optional[CultureSpecificExternalResource] = Field(default=None, alias="socialNetworks")
    support: Optional[CultureSpecificExternalResource] = None
    videoguides: Optional[CultureSpecificExternalResource] = None
    __properties: ClassVar[List[str]] = ["api", "common", "forum", "helpcenter", "integrations", "site", "socialNetworks", "support", "videoguides"]

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
        """Create an instance of CultureSpecificExternalResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of api
        if self.api:
            _dict['api'] = self.api.to_dict()
        # override the default output from pydantic by calling `to_dict()` of common
        if self.common:
            _dict['common'] = self.common.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forum
        if self.forum:
            _dict['forum'] = self.forum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of helpcenter
        if self.helpcenter:
            _dict['helpcenter'] = self.helpcenter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of integrations
        if self.integrations:
            _dict['integrations'] = self.integrations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of site
        if self.site:
            _dict['site'] = self.site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of social_networks
        if self.social_networks:
            _dict['socialNetworks'] = self.social_networks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support
        if self.support:
            _dict['support'] = self.support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of videoguides
        if self.videoguides:
            _dict['videoguides'] = self.videoguides.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CultureSpecificExternalResources from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "api": CultureSpecificExternalResource.from_dict(obj["api"]) if obj.get("api") is not None else None,
            "common": CultureSpecificExternalResource.from_dict(obj["common"]) if obj.get("common") is not None else None,
            "forum": CultureSpecificExternalResource.from_dict(obj["forum"]) if obj.get("forum") is not None else None,
            "helpcenter": CultureSpecificExternalResource.from_dict(obj["helpcenter"]) if obj.get("helpcenter") is not None else None,
            "integrations": CultureSpecificExternalResource.from_dict(obj["integrations"]) if obj.get("integrations") is not None else None,
            "site": CultureSpecificExternalResource.from_dict(obj["site"]) if obj.get("site") is not None else None,
            "socialNetworks": CultureSpecificExternalResource.from_dict(obj["socialNetworks"]) if obj.get("socialNetworks") is not None else None,
            "support": CultureSpecificExternalResource.from_dict(obj["support"]) if obj.get("support") is not None else None,
            "videoguides": CultureSpecificExternalResource.from_dict(obj["videoguides"]) if obj.get("videoguides") is not None else None
        })
        return _obj


