# FormSubmissionsWrapper
The successful API response containing the FormSubmissionsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FormSubmissionsDto**](FormSubmissionsDto.md) | The FormSubmissionsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.form_submissions_wrapper import FormSubmissionsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FormSubmissionsWrapper from a JSON string
form_submissions_wrapper_instance = FormSubmissionsWrapper.from_json(json)
# print the JSON string representation of the object
print(FormSubmissionsWrapper.to_json())

# convert the object into a dict
form_submissions_wrapper_dict = form_submissions_wrapper_instance.to_dict()
# create an instance of FormSubmissionsWrapper from a dict
form_submissions_wrapper_from_dict = FormSubmissionsWrapper.from_dict(form_submissions_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


