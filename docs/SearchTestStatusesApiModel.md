# SearchTestStatusesApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inquiry** | [**Inquiry**](Inquiry.md) |  | [optional] 

## Example

```python
from testit_api_client.models.search_test_statuses_api_model import SearchTestStatusesApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTestStatusesApiModel from a JSON string
search_test_statuses_api_model_instance = SearchTestStatusesApiModel.from_json(json)
# print the JSON string representation of the object
print SearchTestStatusesApiModel.to_json()

# convert the object into a dict
search_test_statuses_api_model_dict = search_test_statuses_api_model_instance.to_dict()
# create an instance of SearchTestStatusesApiModel from a dict
search_test_statuses_api_model_from_dict = SearchTestStatusesApiModel.from_dict(search_test_statuses_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


