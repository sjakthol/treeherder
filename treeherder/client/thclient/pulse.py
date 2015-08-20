import os
import yaml

def get_jobs_schema():
    with open("{0}/job.yml".format(
              os.path.dirname(__file__))) as f:
        return yaml.load(f)
