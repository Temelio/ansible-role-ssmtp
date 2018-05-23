"""
Role tests
"""

import pytest
import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssmtp_package(host):
    """
    Test ssmtp is installed
    """

    assert host.package('ssmtp').is_installed


@pytest.mark.parametrize('item_type,path,user', [
        ('directory', '/etc/ssmtp', 'root'),
        ('file', '/etc/ssmtp/ssmtp.conf', 'root'),
        ('file', '/etc/ssmtp/revaliases', 'root'),
    ])
def test_paths_properties(host, item_type, path, user):
    """
    Test ssmtp folders and files properties
    """

    current_item = host.file(path)

    if item_type == 'directory':
        assert current_item.is_directory
    elif item_type == 'file':
        assert current_item.is_file

    assert current_item.exists
    assert current_item.user == user
    
