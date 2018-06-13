#!/bin/bash

# Start the SKF Angular app
cd ../Angular
/usr/local/bin/ng serve --public demo.securityknowledgeframework.org:443 --env=prod &
