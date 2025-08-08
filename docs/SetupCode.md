# SetupCode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] [readonly] 
**manual_entry_key** | **str** |  | [optional] [readonly] 
**qr_code_setup_image_url** | **str** |  | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.setup_code import SetupCode

# TODO update the JSON string below
json = "{}"
# create an instance of SetupCode from a JSON string
setup_code_instance = SetupCode.from_json(json)
# print the JSON string representation of the object
print(SetupCode.to_json())

# convert the object into a dict
setup_code_dict = setup_code_instance.to_dict()
# create an instance of SetupCode from a dict
setup_code_from_dict = SetupCode.from_dict(setup_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


