
#!/bin/sh
# Fail if git working tree is dirty
git diff --quiet || exit 1
