# TestRunGroupByStatusModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_run_group_by_status_model import TestRunGroupByStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunGroupByStatusModel from a JSON string
test_run_group_by_status_model_instance = TestRunGroupByStatusModel.from_json(json)
# print the JSON string representation of the object
print(TestRunGroupByStatusModel.to_json())

# convert the object into a dict
test_run_group_by_status_model_dict = test_run_group_by_status_model_instance.to_dict()
# create an instance of TestRunGroupByStatusModel from a dict
test_run_group_by_status_model_from_dict = TestRunGroupByStatusModel.from_dict(test_run_group_by_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


