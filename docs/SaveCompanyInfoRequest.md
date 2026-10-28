# SaveCompanyInfoRequest
The company the installation is branded for, as shown on the About page and in letters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | The company name. | [optional] 
**site** | **str** | The company website, as an absolute URL. | [optional] 
**email** | **str** | The contact email address. | [optional] 
**address** | **str** | The postal address. | [optional] 
**phone** | **str** | The contact phone number. | [optional] 
**is_licensor** | **bool** | Accepted for compatibility with earlier clients and not read: saved details are never those of the licensor, so the server always stores `false`. | [optional] 
**hide_about** | **bool** | Whether the About page is hidden. | [optional] 
**last_modified** | **datetime** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.save_company_info_request import SaveCompanyInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCompanyInfoRequest from a JSON string
save_company_info_request_instance = SaveCompanyInfoRequest.from_json(json)
# print the JSON string representation of the object
print(SaveCompanyInfoRequest.to_json())

# convert the object into a dict
save_company_info_request_dict = save_company_info_request_instance.to_dict()
# create an instance of SaveCompanyInfoRequest from a dict
save_company_info_request_from_dict = SaveCompanyInfoRequest.from_dict(save_company_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


