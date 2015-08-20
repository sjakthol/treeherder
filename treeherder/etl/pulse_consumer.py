import jsonschema

from treeherder.client.thclient import pulse

class PulseConsumer:
    jobs_schema = None
    artifact_schema = None

    def __init__(self):
        self.jobs_schema = pulse.get_jobs_schema()
        # self.jobs_schema = yaml.load("artifact.yml")


    def load_jobs(self, joblist):
        for job in joblist:
            jsonschema.validate(job, self.jobs_schema)


    def load_artifacts(self, artifactlist):
        jsonschema.validate(artifactlist, self.artifact_schema)
