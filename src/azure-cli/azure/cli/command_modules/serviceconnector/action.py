# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
from collections import defaultdict
from azure.cli.core.azclierror import ValidationError


class AddCustomizedKeys(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.customized_keys = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k] = v
            properties = dict(properties)
            return properties
        except ValueError:
            raise ValidationError('Usage error: {} [KEY=VALUE ...]'.format(option_string))


class AddSecretAuthInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.secret_auth_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise ValidationError('Usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'name':
                d['name'] = v[0]
            elif kl == 'secret':
                d['secret_info'] = {
                    'secret_type': 'rawValue',
                    'value': v[0]
                }
            elif kl == 'secret-uri':
                d['secret_info'] = {
                    'secret_type': 'keyVaultSecretUri',
                    'value': v[0]
                }
            elif kl == 'secret-name':
                d['secret_info'] = {
                    'secret_type': 'keyVaultSecretReference',
                    'name': v[0]
                }
            else:
                raise ValidationError('Unsupported Key {} is provided for parameter secret_auth_info. All possible '
                                      'keys are: name, secret/secret-uri/secret-name'.format(k))
        if len(d) != 2:
            raise ValidationError('Required keys missing for parameter --secret.'
                                  ' All possible keys are: name, secret/secret-uri/secret-name')
        d['auth_type'] = 'secret'
        return d


class AddSecretAuthInfoAuto(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.secret_auth_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise ValidationError('Usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            raise ValidationError('Unsupported Key {} is provided for parameter --auto-secret')
        d['auth_type'] = 'secret'
        return d


class AddUserAssignedIdentityAuthInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.user_identity_auth_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise ValidationError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'client-id':
                d['client_id'] = v[0]
            elif kl == 'subs-id':
                d['subscription_id'] = v[0]
            else:
                raise ValidationError('Unsupported Key {} is provided for parameter --user-identity. All '
                                      'possible keys are: client-id, subs-id'.format(k))
        if len(d) != 2:
            raise ValidationError('Required keys missing for parameter --user-identity. '
                                  'All possible keys are: client-id, subs-id')
        d['auth_type'] = 'userAssignedIdentity'
        return d


class AddSystemAssignedIdentityAuthInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.system_identity_auth_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise ValidationError('Usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]
            if k.lower() == 'mysql-identity-id':
                d['mysql-identity-id'] = v[0]
            else:
                raise ValidationError('Unsupported Key {} is provided for parameter --system-identity')
        d['auth_type'] = 'systemAssignedIdentity'
        return d


class AddUserAccountAuthInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.user_account_auth_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise ValidationError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'object-id':
                d['principal_id'] = v[0]
            elif kl == 'mysql-identity-id':
                d['mysql-identity-id'] = v[0]
            else:
                raise ValidationError('Unsupported Key {} is provided for parameter --user-account. All '
                                      'possible keys are: principal-id, mysql-identity-id'.format(k))
        d['auth_type'] = 'userAccount'
        return d


class AddServicePrincipalAuthInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.service_principal_auth_info_secret = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise ValidationError('Usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'client-id':
                d['client_id'] = v[0]
            elif kl == 'object-id':
                d['principal_id'] = v[0]
            elif kl == 'secret':
                d['secret'] = v[0]
            else:
                raise ValidationError('Unsupported Key {} is provided for parameter --service-principal. All possible '
                                      'keys are: client-id, object-id, secret'.format(k))
        if 'client_id' not in d or 'secret' not in d:
            raise ValidationError('Required keys missing for parameter --service-principal. '
                                  'Required keys are: client-id, secret')
        if 'principal_id' not in d:
            from ._utils import run_cli_cmd
            output = run_cli_cmd('az ad sp show --id {}'.format(d['client_id']))
            if output:
                d['principal_id'] = output.get('id')
            else:
                raise ValidationError('Could not resolve object-id from the given client-id: {}. Please '
                                      'confirm the client-id and provide the object-id (Enterprise Application) '
                                      'of the service principal, by using --service-principal client-id=XX '
                                      'object-id=XX secret=XX'.format(d['client_id']))

        d['auth_type'] = 'servicePrincipalSecret'
        return d


class AddOptOut(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.opt_out_set = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        opt_out_set = set()
        opt_out_options = {'public-network', 'config'}

        for x in values:
            if x not in opt_out_options:
                raise ValidationError('Unsupported value {} is provided for parameter --opt-out. All '
                                      'possible values are: {}'.format(x, ', '.join(opt_out_options)))
            else:
                opt_out_set.add(x)

        if len(opt_out_set) == 0:
            raise ValidationError('At least one value is required for parameter --opt-out. '
                                  'All possible values are: {}'.format(', '.join(opt_out_options)))
        return opt_out_set