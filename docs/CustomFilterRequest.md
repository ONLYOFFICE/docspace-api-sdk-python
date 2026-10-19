# CustomFilterRequest
The Custom Filter state a spreadsheet is to be put into.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The state to reach: `true` turns the mode on, so that the sorting and filtering each person applies stays  visible to that person alone, and drops the others out of a running editing session; `false` turns it off and  makes filtering shared again. | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_filter_request import CustomFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFilterRequest from a JSON string
custom_filter_request_instance = CustomFilterRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFilterRequest.to_json())

# convert the object into a dict
custom_filter_request_dict = custom_filter_request_instance.to_dict()
# create an instance of CustomFilterRequest from a dict
custom_filter_request_from_dict = CustomFilterRequest.from_dict(custom_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


