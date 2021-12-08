# Test IT TMS API client for JavaScript
![Test IT](https://raw.githubusercontent.com/testit-tms/api-client-python/master/images/banner.png)

# Getting Started

## Installation
```
pip install testit-api-client
```

# Usage

## Configuration

To use client you need to provide configuration to `Client`:
```py
from testit_api_client.api import Api

requests = Api(url, private_token, proxy=proxy)
```

After configuration is done you can access different clients from `Client` object and then use methods to control Test IT.

## Examples

### Create and start test-run
```py
from testit_api_client.json_fixture import JSONFixture

testrun_id = requests.create_testrun(
                JSONFixture.create_testrun(
                    project_id,
                    testrun_name))
					
requests.testrun_activity(testrun_id, 'start')
```

### Create autotest
```py
autotest_id = requests.create_autotest(
				JSONFixture.create_autotest(
					external_id,
					project_id,
					autotest_name,
					steps,
					setup,
					teardown,
					namespace,
					classname,
					title,
					description,
					links,
					labels
				))		
```

# Contributing

You can help to develop the project. Any contributions are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/testit-tms/api-client-python/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/testit-tms/api-client-python/blob/master/CODE_OF_CONDUCT.md) before posting your first idea as well.

# License

Distributed under the Apache-2.0 License. See [LICENSE](https://github.com/testit-tms/api-client-python/blob/master/LICENSE.md) for more information.

