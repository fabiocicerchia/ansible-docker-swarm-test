#!/bin/bash

ansible-lint playbooks/*.yml
cd roles/docker-remote-api && molecule test
