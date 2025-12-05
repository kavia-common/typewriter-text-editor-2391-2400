#!/bin/bash
cd /tmp/kavia/workspace/code-generation/typewriter-text-editor-2391-2400/backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

