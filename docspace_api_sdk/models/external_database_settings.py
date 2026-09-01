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
    The connection parameters of an external database.
    """ # noqa: E501
    database_type: Optional[StrictStr] = Field(default=None, description="The engine of the external database.", alias="databaseType", json_schema_extra={"examples": ["mysql"]})
    database_type_enum: Optional[ExternalDatabaseType] = Field(default=None, description="The engine of an external database.", alias="databaseTypeEnum")
    db_host: Optional[StrictStr] = Field(default=None, description="The host name or the IP address of the database server.", alias="dbHost", json_schema_extra={"examples": ["localhost"]})
    db_port: Optional[StrictInt] = Field(default=None, description="The port the database server listens on.", alias="dbPort", json_schema_extra={"examples": [3306]})
    db_name: Optional[StrictStr] = Field(default=None, description="The name of the database to connect to.", alias="dbName", json_schema_extra={"examples": ["docspace"]})
    db_user: Optional[StrictStr] = Field(default=None, description="The user name to connect with.", alias="dbUser", json_schema_extra={"examples": ["root"]})
    db_password: Optional[StrictStr] = Field(default=None, description="The password to connect with.", alias="dbPassword", json_schema_extra={"examples": ["my-secret-password"]})
    db_ssl: Optional[StrictBool] = Field(default=None, description="Specifies whether the connection to the database is secured with SSL.", alias="dbSsl", json_schema_extra={"examples": [False]})
    sqlite_file_path: Optional[StrictStr] = Field(default=None, description="The path to the database file, used by the SQLite engine only.", alias="sqliteFilePath", json_schema_extra={"examples": ["/var/lib/docspace/external.db"]})
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


