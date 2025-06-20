# WorkItemSelectApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WorkItemFilterApiModel**](WorkItemFilterApiModel.md) |  | 
**extraction_model** | [**WorkItemExtractionApiModel**](WorkItemExtractionApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_select_api_model import WorkItemSelectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemSelectApiModel from a JSON string
work_item_select_api_model_instance = WorkItemSelectApiModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemSelectApiModel.to_json())

# convert the object into a dict
work_item_select_api_model_dict = work_item_select_api_model_instance.to_dict()
# create an instance of WorkItemSelectApiModel from a dict
work_item_select_api_model_from_dict = WorkItemSelectApiModel.from_dict(work_item_select_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


