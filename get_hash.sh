
#!/bin/bash

# Ensure that there are no uncommitted changes
if git diff-index --quiet HEAD --; then
    echo "No uncommitted changes."
else
    echo "You have uncommitted changes. Please commit them before proceeding."
    exit 1
fi

# Get the current Git commit hash and store it in a file
commit_hash=$(git rev-parse --short HEAD)

# Export the commit hash as an environment variable
echo "Commit hash: $commit_hash"
echo "COMMIT_HASH=$commit_hash" >> .env

# Proceed with the next steps
exit 0
