# ThirdPartyConfigurationWrapper
The successful API response containing the ThirdPartyConfigurationDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ThirdPartyConfigurationDto**](ThirdPartyConfigurationDto.md) | The ThirdPartyConfigurationDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_configuration_wrapper import ThirdPartyConfigurationWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyConfigurationWrapper from a JSON string
third_party_configuration_wrapper_instance = ThirdPartyConfigurationWrapper.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyConfigurationWrapper.to_json())

# convert the object into a dict
third_party_configuration_wrapper_dict = third_party_configuration_wrapper_instance.to_dict()
# create an instance of ThirdPartyConfigurationWrapper from a dict
third_party_configuration_wrapper_from_dict = ThirdPartyConfigurationWrapper.from_dict(third_party_configuration_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


