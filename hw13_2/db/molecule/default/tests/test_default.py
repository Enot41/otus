import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# check if MongoDB is enabled and running
def test_mongo_running_and_enabled(host):
  mongo = host.service("mongodb")
  assert mongo.is_running
  assert mongo.is_enabled
def test_mongodb_is_listening(host):
  assert host.socket("tcp://0.0.0.0:27017").is_listening
