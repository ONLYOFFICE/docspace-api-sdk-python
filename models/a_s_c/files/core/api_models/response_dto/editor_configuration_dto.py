from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....web.files.services.document_service.co_editing_config import CoEditingConfig
    from .....web.files.services.document_service.embedded_config import EmbeddedConfig
    from .....web.files.services.document_service.encryption_keys_config import EncryptionKeysConfig
    from .....web.files.services.document_service.plugins_config import PluginsConfig
    from .....web.files.services.document_service.recent_config import RecentConfig
    from .....web.files.services.document_service.templates_config import TemplatesConfig
    from .....web.files.services.document_service.user_config import UserConfig
    from .customization_config_dto import CustomizationConfigDto

@dataclass
class EditorConfigurationDto(Parsable):
    # Callback url
    callback_url: Optional[str] = None
    # The coEditing property
    co_editing: Optional[CoEditingConfig] = None
    # Create url
    create_url: Optional[str] = None
    # The customization property
    customization: Optional[CustomizationConfigDto] = None
    # The embedded property
    embedded: Optional[EmbeddedConfig] = None
    # The encryptionKeys property
    encryption_keys: Optional[EncryptionKeysConfig] = None
    # Lang
    lang: Optional[str] = None
    # Mode
    mode: Optional[str] = None
    # Mode write
    mode_write: Optional[bool] = None
    # The plugins property
    plugins: Optional[PluginsConfig] = None
    # Recent
    recent: Optional[List[RecentConfig]] = None
    # Templates
    templates: Optional[List[TemplatesConfig]] = None
    # The user property
    user: Optional[UserConfig] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EditorConfigurationDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditorConfigurationDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EditorConfigurationDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....web.files.services.document_service.co_editing_config import CoEditingConfig
        from .....web.files.services.document_service.embedded_config import EmbeddedConfig
        from .....web.files.services.document_service.encryption_keys_config import EncryptionKeysConfig
        from .....web.files.services.document_service.plugins_config import PluginsConfig
        from .....web.files.services.document_service.recent_config import RecentConfig
        from .....web.files.services.document_service.templates_config import TemplatesConfig
        from .....web.files.services.document_service.user_config import UserConfig
        from .customization_config_dto import CustomizationConfigDto

        from .....web.files.services.document_service.co_editing_config import CoEditingConfig
        from .....web.files.services.document_service.embedded_config import EmbeddedConfig
        from .....web.files.services.document_service.encryption_keys_config import EncryptionKeysConfig
        from .....web.files.services.document_service.plugins_config import PluginsConfig
        from .....web.files.services.document_service.recent_config import RecentConfig
        from .....web.files.services.document_service.templates_config import TemplatesConfig
        from .....web.files.services.document_service.user_config import UserConfig
        from .customization_config_dto import CustomizationConfigDto

        fields: Dict[str, Callable[[Any], None]] = {
            "callbackUrl": lambda n : setattr(self, 'callback_url', n.get_str_value()),
            "coEditing": lambda n : setattr(self, 'co_editing', n.get_object_value(CoEditingConfig)),
            "createUrl": lambda n : setattr(self, 'create_url', n.get_str_value()),
            "customization": lambda n : setattr(self, 'customization', n.get_object_value(CustomizationConfigDto)),
            "embedded": lambda n : setattr(self, 'embedded', n.get_object_value(EmbeddedConfig)),
            "encryptionKeys": lambda n : setattr(self, 'encryption_keys', n.get_object_value(EncryptionKeysConfig)),
            "lang": lambda n : setattr(self, 'lang', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "modeWrite": lambda n : setattr(self, 'mode_write', n.get_bool_value()),
            "plugins": lambda n : setattr(self, 'plugins', n.get_object_value(PluginsConfig)),
            "recent": lambda n : setattr(self, 'recent', n.get_collection_of_object_values(RecentConfig)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(TemplatesConfig)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UserConfig)),
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
        from .....web.files.services.document_service.co_editing_config import CoEditingConfig
        from .....web.files.services.document_service.embedded_config import EmbeddedConfig
        from .....web.files.services.document_service.encryption_keys_config import EncryptionKeysConfig
        from .....web.files.services.document_service.plugins_config import PluginsConfig
        from .....web.files.services.document_service.recent_config import RecentConfig
        from .....web.files.services.document_service.templates_config import TemplatesConfig
        from .....web.files.services.document_service.user_config import UserConfig
        from .customization_config_dto import CustomizationConfigDto

        writer.write_str_value("callbackUrl", self.callback_url)
        writer.write_object_value("coEditing", self.co_editing)
        writer.write_str_value("createUrl", self.create_url)
        writer.write_object_value("customization", self.customization)
        writer.write_object_value("embedded", self.embedded)
        writer.write_object_value("encryptionKeys", self.encryption_keys)
        writer.write_str_value("lang", self.lang)
        writer.write_str_value("mode", self.mode)
        writer.write_bool_value("modeWrite", self.mode_write)
        writer.write_object_value("plugins", self.plugins)
        writer.write_collection_of_object_values("recent", self.recent)
        writer.write_collection_of_object_values("templates", self.templates)
        writer.write_object_value("user", self.user)
    

