# SmtpSettingsWrapper
The successful API response containing the SmtpSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SmtpSettingsDto**](SmtpSettingsDto.md) | The SmtpSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.smtp_settings_wrapper import SmtpSettingsWrapper

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


