# RerunsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rerun_count** | **int** |  | 
**rerun_test_results** | [**List[RerunTestResultModel]**](RerunTestResultModel.md) |  | 

## Example

```python
from testit_api_client.models.reruns_model import RerunsModel

# TODO update the JSON string below
json = "{}"
# create an instance of RerunsModel from a JSON string
reruns_model_instance = RerunsModel.from_json(json)
# print the JSON string representation of the object
print(RerunsModel.to_json())

# convert the object into a dict
reruns_model_dict = reruns_model_instance.to_dict()
# create an instance of RerunsModel from a dict
reruns_model_from_dict = RerunsModel.from_dict(reruns_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


