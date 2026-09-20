# FileLinkRequest
The settings of an external link to a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **UUID** | The link to rewrite, as reported by `GET api/2.0/files/file/{id}/links`. An identifier that is not yet in use,  the empty one included, creates a link instead. | [optional] 
**access** | [**FileShare**](FileShare.md) | The rights the link grants to whoever follows it. The value that denies everything revokes the link. | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) | The moment the link stops working, read in the time zone of the portal. A date more than a few years ahead is  rejected as an invalid request; left out, the link does not expire on its own. | [optional] 
**title** | **str** | The name the link carries in the sharing list of the file, for the people who manage it; it is not shown to  whoever follows the link. | [optional] 
**internal** | **bool** | Who may follow the link: `true` admits only accounts that are signed in to the portal, `false` admits anybody  who has the address. | [optional] 
**primary** | **bool** | Whether this link becomes the primary link of the file - the one the Copy link action of a client hands out.  A file has one primary link at a time. | [optional] 
**deny_download** | **bool** | What a visitor may do with the content: `true` leaves them with viewing in the browser, `false` lets them  download and print it as their rights allow. | [optional] 
**password** | **str** | The secret a visitor has to type before the file opens; left out, the link opens without one. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_link_request import FileLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileLinkRequest from a JSON string
file_link_request_instance = FileLinkRequest.from_json(json)
# print the JSON string representation of the object
print(FileLinkRequest.to_json())

# convert the object into a dict
file_link_request_dict = file_link_request_instance.to_dict()
# create an instance of FileLinkRequest from a dict
file_link_request_from_dict = FileLinkRequest.from_dict(file_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


