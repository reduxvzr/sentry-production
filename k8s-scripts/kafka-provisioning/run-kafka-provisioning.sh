#!/bin/bash

id=$(date +%s)
sed "s/%%id%%/$id/g" kafka-provisioning-job.yaml | kubectl -n sentry apply -f -
