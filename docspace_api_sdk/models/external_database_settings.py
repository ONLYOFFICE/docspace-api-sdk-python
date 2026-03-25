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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.external_database_type import ExternalDatabaseType
from typing import Optional, Set
from typing_extensions import Self

class ExternalDatabaseSettings(BaseModel):
    """
    ExternalDatabaseSettings
    """ # noqa: E501
    database_type: Optional[StrictStr] = Field(default=None, alias="databaseType")
    database_type_enum: Optional[ExternalDatabaseType] = Field(default=None, alias="databaseTypeEnum")
    db_host: Optional[StrictStr] = Field(default=None, alias="dbHost")
    db_port: Optional[StrictInt] = Field(default=None, alias="dbPort")
    db_name: Optional[StrictStr] = Field(default=None, alias="dbName")
    db_user: Optional[StrictStr] = Field(default=None, alias="dbUser")
    db_password: Optional[StrictStr] = Field(default=None, alias="dbPassword")
    db_ssl: Optional[StrictBool] = Field(default=None, alias="dbSsl")
    sqlite_file_path: Optional[StrictStr] = Field(default=None, alias="sqliteFilePath")
    __properties: ClassVar[List[str]] = ["databaseType", "databaseTypeEnum", "dbHost", "dbPort", "dbName", "dbUser", "dbPassword", "dbSsl", "sqliteFilePath"]

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
        """Create an instance of ExternalDatabaseSettings from a JSON string"""
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
        # set to None if database_type (nullable) is None
        # and model_fields_set contains the field
        if self.database_type is None and "database_type" in self.model_fields_set:
            _dict['databaseType'] = None

        # set to None if db_host (nullable) is None
        # and model_fields_set contains the field
        if self.db_host is None and "db_host" in self.model_fields_set:
            _dict['dbHost'] = None

        # set to None if db_name (nullable) is None
        # and model_fields_set contains the field
        if self.db_name is None and "db_name" in self.model_fields_set:
            _dict['dbName'] = None

        # set to None if db_user (nullable) is None
        # and model_fields_set contains the field
        if self.db_user is None and "db_user" in self.model_fields_set:
            _dict['dbUser'] = None

        # set to None if db_password (nullable) is None
        # and model_fields_set contains the field
        if self.db_password is None and "db_password" in self.model_fields_set:
            _dict['dbPassword'] = None

        # set to None if sqlite_file_path (nullable) is None
        # and model_fields_set contains the field
        if self.sqlite_file_path is None and "sqlite_file_path" in self.model_fields_set:
            _dict['sqliteFilePath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalDatabaseSettings from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "databaseType": obj.get("databaseType"),
            "databaseTypeEnum": obj.get("databaseTypeEnum"),
            "dbHost": obj.get("dbHost"),
            "dbPort": obj.get("dbPort"),
            "dbName": obj.get("dbName"),
            "dbUser": obj.get("dbUser"),
            "dbPassword": obj.get("dbPassword"),
            "dbSsl": obj.get("dbSsl"),
            "sqliteFilePath": obj.get("sqliteFilePath")
        })
        return _obj


