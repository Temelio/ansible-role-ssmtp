# ssmtp

[![Build Status](https://travis-ci.org/Temelio/ansible-role-ssmtp.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-ssmtp)

Install ssmtp package.

## Requirements

This role requires Ansible 2.2, 2.3 and 2.4
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Debian Stretch
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables
# Repository & package management
# -----------------------------------------------------------------------------
ssmtp_prerequisites_packages: "{{ _ssmtp_prerequisites_packages }}"
ssmtp_repository_cache_valid_time: 3600
ssmtp_repository_update_cache: 'True'

# ssmtp user and group
# -----------------------------------------------------------------------------
ssmtp_user_name: 'root'
ssmtp_group_name: 'mail'

# Path management
# -----------------------------------------------------------------------------
ssmtp_paths:
  dirs:
    config:
      path: '/etc/ssmtp'
  files:
    main_config:
      path: '/etc/ssmtp/ssmtp.conf'
      owner: "{{ ssmtp_user_name }}"
      group: "{{ ssmtp_group_name }}"
      mode: '0640'
    revaliases_config:
      path: '/etc/ssmtp/revaliases'
      owner: "{{ ssmtp_user_name }}"
      group: "{{ ssmtp_group_name }}"
      mode: '0640'

# ssmtp config
# -----------------------------------------------------------------------------
ssmtp_root_recipient: 'admin@example.com'
ssmtp_mailhub: 'mail.example.com'
ssmtp_mailhub_port: '25'
ssmtp_from_line_override: 'YES'
ssmtp_use_STARTTLS: 'YES'
ssmtp_authUser: 'user@example.com'
ssmtp_authPass: 'change me'

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.ansible-role-ssmtp }
```

## License

MIT

## Author Information

Lise Machetel (for Temelio company)
- http://temelio.com
- lise.machetel [at] temelio.com
