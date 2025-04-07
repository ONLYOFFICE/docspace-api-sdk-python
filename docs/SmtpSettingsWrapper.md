# SmtpSettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SmtpSettingsDto**](SmtpSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.smtp_settings_wrapper import SmtpSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpSettingsWrapper from a JSON string
smtp_settings_wrapper_instance = SmtpSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(SmtpSettingsWrapper.to_json())

# convert the object into a dict
smtp_settings_wrapper_dict = smtp_settings_wrapper_instance.to_dict()
# create an instance of SmtpSettingsWrapper from a dict
smtp_settings_wrapper_from_dict = SmtpSettingsWrapper.from_dict(smtp_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


