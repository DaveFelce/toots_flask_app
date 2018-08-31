curl -u "standardcandlesoftware@gmail.com" https://api.buildkite.com/v2/organizations/standardcandle-1/pipelines/python-docker-example/builds \
  -X POST \
  -F "commit=HEAD" \
  -F "branch=master" \
  -F "message=First build :rocket:"
