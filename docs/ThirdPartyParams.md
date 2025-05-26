# ThirdPartyParams

The third-party account parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_data** | [**AuthData**](AuthData.md) |  | [optional] 
**corporate** | **bool** | Specifies if this is a corporate account or not. | [optional] 
**rooms_storage** | **bool** | Specifies if this is a room storage or not. | [optional] 
**customer_title** | **str** | The customer title. | [optional] 
**provider_id** | **int** | The provider ID. | [optional] 
**provider_key** | **str** | The provider key. | [optional] 

## Example

```python
from docspace.models.third_party_params import ThirdPartyParams

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyParams from a JSON string
third_party_params_instance = ThirdPartyParams.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyParams.to_json())

# convert the object into a dict
third_party_params_dict = third_party_params_instance.to_dict()
# create an instance of ThirdPartyParams from a dict
third_party_params_from_dict = ThirdPartyParams.from_dict(third_party_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


