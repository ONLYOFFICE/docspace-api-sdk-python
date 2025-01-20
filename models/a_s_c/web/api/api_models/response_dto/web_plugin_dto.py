from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.employee_dto import EmployeeDto

@dataclass
class WebPluginDto(Parsable):
    # Author
    author: Optional[str] = None
    # The createBy property
    create_by: Optional[EmployeeDto] = None
    # Create on
    create_on: Optional[datetime.datetime] = None
    # Description
    description: Optional[str] = None
    # Enabled
    enabled: Optional[bool] = None
    # Home page
    home_page: Optional[str] = None
    # Image
    image: Optional[str] = None
    # License
    license: Optional[str] = None
    # Name
    name: Optional[str] = None
    # PluginName
    plugin_name: Optional[str] = None
    # Scopes
    scopes: Optional[str] = None
    # Settings
    settings: Optional[str] = None
    # System
    system: Optional[bool] = None
    # Url
    url: Optional[str] = None
    # Version
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebPluginDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebPluginDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebPluginDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.employee_dto import EmployeeDto

        from ...models.employee_dto import EmployeeDto

        fields: Dict[str, Callable[[Any], None]] = {
            "author": lambda n : setattr(self, 'author', n.get_str_value()),
            "createBy": lambda n : setattr(self, 'create_by', n.get_object_value(EmployeeDto)),
            "createOn": lambda n : setattr(self, 'create_on', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "homePage": lambda n : setattr(self, 'home_page', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "license": lambda n : setattr(self, 'license', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "pluginName": lambda n : setattr(self, 'plugin_name', n.get_str_value()),
            "scopes": lambda n : setattr(self, 'scopes', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_str_value()),
            "system": lambda n : setattr(self, 'system', n.get_bool_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from ...models.employee_dto import EmployeeDto

        writer.write_str_value("author", self.author)
        writer.write_object_value("createBy", self.create_by)
        writer.write_datetime_value("createOn", self.create_on)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("homePage", self.home_page)
        writer.write_str_value("image", self.image)
        writer.write_str_value("license", self.license)
        writer.write_str_value("name", self.name)
        writer.write_str_value("pluginName", self.plugin_name)
        writer.write_str_value("scopes", self.scopes)
        writer.write_str_value("settings", self.settings)
        writer.write_bool_value("system", self.system)
        writer.write_str_value("url", self.url)
        writer.write_str_value("version", self.version)
    

