from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....system.func.a_s_c.core.common.configuration.data_store_consumer.a_s_c.core.common.configuration.data_store_consumer import DataStoreConsumer
    from .storage_settings_props import StorageSettings_props

@dataclass
class StorageSettings(Parsable):
    # The module property
    module: Optional[str] = None
    # The props property
    props: Optional[StorageSettings_props] = None
    # The switch property
    switch: Optional[DataStoreConsumer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....system.func.a_s_c.core.common.configuration.data_store_consumer.a_s_c.core.common.configuration.data_store_consumer import DataStoreConsumer
        from .storage_settings_props import StorageSettings_props

        from .....system.func.a_s_c.core.common.configuration.data_store_consumer.a_s_c.core.common.configuration.data_store_consumer import DataStoreConsumer
        from .storage_settings_props import StorageSettings_props

        fields: Dict[str, Callable[[Any], None]] = {
            "module": lambda n : setattr(self, 'module', n.get_str_value()),
            "props": lambda n : setattr(self, 'props', n.get_object_value(StorageSettings_props)),
            "switch": lambda n : setattr(self, 'switch', n.get_object_value(DataStoreConsumer)),
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
        from .....system.func.a_s_c.core.common.configuration.data_store_consumer.a_s_c.core.common.configuration.data_store_consumer import DataStoreConsumer
        from .storage_settings_props import StorageSettings_props

        writer.write_str_value("module", self.module)
        writer.write_object_value("props", self.props)
        writer.write_object_value("switch", self.switch)
    

