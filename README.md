# ansible-role-ssmtp

[![Build Status](https://travis-ci.org/Temelio/ansible-role-ssmtp.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-ssmtp)

Install ansible-role-ssmtp package.

## Requirements

This role requires Ansible 2.2, 2.3, 2.4
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
- https://temelio.com
- lise.machetel [at] temelio.com
