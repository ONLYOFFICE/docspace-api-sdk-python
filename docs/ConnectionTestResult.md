# ConnectionTestResult
The outcome of a connection test against an external database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Specifies whether the connection to the database succeeded. | [optional] 
**error** | **str** | The reason the connection failed, or null when it succeeded. | [optional] 

## Example

```python
from docspace_api_sdk.models.connection_test_result import ConnectionTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTestResult from a JSON string
connection_test_result_instance = ConnectionTestResult.from_json(json)
# print the JSON string representation of the object
print(ConnectionTestResult.to_json())

# convert the object into a dict
connection_test_result_dict = connection_test_result_instance.to_dict()
# create an instance of ConnectionTestResult from a dict
connection_test_result_from_dict = ConnectionTestResult.from_dict(connection_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


