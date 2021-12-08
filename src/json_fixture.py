class JSONFixture:
    @staticmethod
    def create_autotest(
        external_id,
        project_id,
        name,
        steps=None,
        setup=None,
        teardown=None,
        namespace=None,
        classname=None,
        title=None,
        description=None,
        links=None,
        labels=None
    ):
        return {
            'externalId': external_id,
            'projectId': project_id,
            'name': name,
            'steps': steps,
            'setup': setup,
            'teardown': teardown,
            'namespace': namespace,
            'classname': classname,
            'title': title,
            'description': description,
            'links': links,
            'labels': labels
        }

    @staticmethod
    def update_autotest(
        external_id,
        project_id,
        name,
        ID,
        steps=None,
        setup=None,
        teardown=None,
        namespace=None,
        classname=None,
        title=None,
        description=None,
        links=None,
        labels=None
    ):
        return {
            'externalId': external_id,
            'projectId': project_id,
            'name': name,
            'id': ID,
            'steps': steps,
            'setup': setup,
            'teardown': teardown,
            'namespace': namespace,
            'classname': classname,
            'title': title,
            'description': description,
            'links': links,
            'labels': labels
        }

    @staticmethod
    def create_testrun(project_id, name):
        return {
            'projectId': project_id,
            'name': name
        }

    @staticmethod
    def set_results_for_testrun(
        autotest_external_id,
        configuration_id,
        outcome,
        step_results=None,
        setup_results=None,
        teardown_results=None,
        traces=None,
        attachments=None,
        parameters=None,
        links=None,
        duration=None,
        failure_reason_name=None,
        message=None
    ):
        return {
            'autoTestExternalId': autotest_external_id,
            'configurationId': configuration_id,
            'outcome': outcome,
            'stepResults': step_results,
            'setupResults': setup_results,
            'teardownResults': teardown_results,
            'traces': traces,
            'attachments': attachments,
            'parameters': parameters,
            'links': links,
            'duration': duration,
            'failureReasonName': failure_reason_name,
            'message': message
        }
