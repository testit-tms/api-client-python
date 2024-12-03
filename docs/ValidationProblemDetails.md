# ValidationProblemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.validation_problem_details import ValidationProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationProblemDetails from a JSON string
validation_problem_details_instance = ValidationProblemDetails.from_json(json)
# print the JSON string representation of the object
print(ValidationProblemDetails.to_json())

# convert the object into a dict
validation_problem_details_dict = validation_problem_details_instance.to_dict()
# create an instance of ValidationProblemDetails from a dict
validation_problem_details_from_dict = ValidationProblemDetails.from_dict(validation_problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


