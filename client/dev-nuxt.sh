#!/usr/bin/env bash

set -o errexit

root="$(dirname "$0")/.."
app="${root}/client"

(
  cd "${app}"
 
  if [[ ! -d node_modules/.bin ]]; then
    echo "Installing dependencies"
    npm install
  fi

  echo "Starting frontend server"
  #npm run lintfix
  npm install --no-package-lock
  npm run serve
)
