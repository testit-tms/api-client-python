# TestPointSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**work_item_ids** | **List[str]** | Specifies the work item GUIDs, from which test points are created. You can specify several GUIDs. | 

## Example

```python
from testit_api_client.models.test_point_selector import TestPointSelector

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointSelector from a JSON string
test_point_selector_instance = TestPointSelector.from_json(json)
# print the JSON string representation of the object
print(TestPointSelector.to_json())

# convert the object into a dict
test_point_selector_dict = test_point_selector_instance.to_dict()
# create an instance of TestPointSelector from a dict
test_point_selector_from_dict = TestPointSelector.from_dict(test_point_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


