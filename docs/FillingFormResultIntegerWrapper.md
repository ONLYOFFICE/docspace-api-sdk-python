# FillingFormResultIntegerWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FillingFormResultDtoInteger**](FillingFormResultDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.filling_form_result_integer_wrapper import FillingFormResultIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FillingFormResultIntegerWrapper from a JSON string
filling_form_result_integer_wrapper_instance = FillingFormResultIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(FillingFormResultIntegerWrapper.to_json())

# convert the object into a dict
filling_form_result_integer_wrapper_dict = filling_form_result_integer_wrapper_instance.to_dict()
# create an instance of FillingFormResultIntegerWrapper from a dict
filling_form_result_integer_wrapper_from_dict = FillingFormResultIntegerWrapper.from_dict(filling_form_result_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


