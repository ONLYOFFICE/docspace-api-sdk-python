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

class AmazonS3RegionDto(BaseModel):
    """
    An Amazon S3 region.
    """ # noqa: E501
    system_name: Optional[StrictStr] = Field(default=None, description="The region code to send as the region value when configuring an Amazon S3 storage or backup target. It is  the one field of this object that is an argument elsewhere; a code the server does not list here cannot be  reached, so pick one from this list rather than typing it.", alias="systemName", json_schema_extra={"examples": ["eu-west-1"]})
    display_name: Optional[StrictStr] = Field(default=None, description="The region name as Amazon writes it, in English regardless of the portal language, for showing in a  picker next to `systemName`.", alias="displayName", json_schema_extra={"examples": ["Europe (Ireland)"]})
    partition_name: Optional[StrictStr] = Field(default=None, description="The Amazon partition the region sits in - the ordinary commercial cloud, the Chinese one, or a government  one. Regions of different partitions are not reachable with the same credentials.", alias="partitionName", json_schema_extra={"examples": ["aws"]})
    partition_dns_suffix: Optional[StrictStr] = Field(default=None, description="The domain the partition's service host names end in, which differs from partition to partition.", alias="partitionDnsSuffix", json_schema_extra={"examples": ["amazonaws.com"]})
    partition_region_regex: Optional[StrictStr] = Field(default=None, description="The pattern every region code of this partition matches, for validating a code before sending it.", alias="partitionRegionRegex", json_schema_extra={"examples": ["^(us|eu|ap|sa|ca|me|af|il|mx)\\-\\w+\\-\\d+$"]})
    hostname_template: Optional[StrictStr] = Field(default=None, description="How a service host name of the partition is assembled, with `{service}`, `{region}` and `{dnsSuffix}` to  be filled in. It is reference material - the portal builds its own endpoints from `systemName`.", alias="hostnameTemplate", json_schema_extra={"examples": ["{service}.{region}.{dnsSuffix}"]})
    __properties: ClassVar[List[str]] = ["systemName", "displayName", "partitionName", "partitionDnsSuffix", "partitionRegionRegex", "hostnameTemplate"]

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
        """Create an instance of AmazonS3RegionDto from a JSON string"""
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
        # set to None if system_name (nullable) is None
        # and model_fields_set contains the field
        if self.system_name is None and "system_name" in self.model_fields_set:
            _dict['systemName'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['displayName'] = None

        # set to None if partition_name (nullable) is None
        # and model_fields_set contains the field
        if self.partition_name is None and "partition_name" in self.model_fields_set:
            _dict['partitionName'] = None

        # set to None if partition_dns_suffix (nullable) is None
        # and model_fields_set contains the field
        if self.partition_dns_suffix is None and "partition_dns_suffix" in self.model_fields_set:
            _dict['partitionDnsSuffix'] = None

        # set to None if partition_region_regex (nullable) is None
        # and model_fields_set contains the field
        if self.partition_region_regex is None and "partition_region_regex" in self.model_fields_set:
            _dict['partitionRegionRegex'] = None

        # set to None if hostname_template (nullable) is None
        # and model_fields_set contains the field
        if self.hostname_template is None and "hostname_template" in self.model_fields_set:
            _dict['hostnameTemplate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AmazonS3RegionDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "systemName": obj.get("systemName"),
            "displayName": obj.get("displayName"),
            "partitionName": obj.get("partitionName"),
            "partitionDnsSuffix": obj.get("partitionDnsSuffix"),
            "partitionRegionRegex": obj.get("partitionRegionRegex"),
            "hostnameTemplate": obj.get("hostnameTemplate")
        })
        return _obj


