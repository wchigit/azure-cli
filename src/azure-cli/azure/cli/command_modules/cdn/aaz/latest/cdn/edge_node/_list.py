# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "cdn edge-node list",
)
class List(AAZCommand):
    """List are the global Point of Presence (POP) locations used to deliver CDN content to end users.
    """

    _aaz_info = {
        "version": "2024-02-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.cdn/edgenodes", "2024-02-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    def _execute_operations(self):
        self.pre_operations()
        self.EdgeNodesList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class EdgeNodesList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Cdn/edgenodes",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-02-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.ip_address_groups = AAZListType(
                serialized_name="ipAddressGroups",
                flags={"required": True},
            )

            ip_address_groups = cls._schema_on_200.value.Element.properties.ip_address_groups
            ip_address_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ip_address_groups.Element
            _element.delivery_region = AAZStrType(
                serialized_name="deliveryRegion",
            )
            _element.ipv4_addresses = AAZListType(
                serialized_name="ipv4Addresses",
            )
            _element.ipv6_addresses = AAZListType(
                serialized_name="ipv6Addresses",
            )

            ipv4_addresses = cls._schema_on_200.value.Element.properties.ip_address_groups.Element.ipv4_addresses
            ipv4_addresses.Element = AAZObjectType()
            _ListHelper._build_schema_cidr_ip_address_read(ipv4_addresses.Element)

            ipv6_addresses = cls._schema_on_200.value.Element.properties.ip_address_groups.Element.ipv6_addresses
            ipv6_addresses.Element = AAZObjectType()
            _ListHelper._build_schema_cidr_ip_address_read(ipv6_addresses.Element)

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_cidr_ip_address_read = None

    @classmethod
    def _build_schema_cidr_ip_address_read(cls, _schema):
        if cls._schema_cidr_ip_address_read is not None:
            _schema.base_ip_address = cls._schema_cidr_ip_address_read.base_ip_address
            _schema.prefix_length = cls._schema_cidr_ip_address_read.prefix_length
            return

        cls._schema_cidr_ip_address_read = _schema_cidr_ip_address_read = AAZObjectType()

        cidr_ip_address_read = _schema_cidr_ip_address_read
        cidr_ip_address_read.base_ip_address = AAZStrType(
            serialized_name="baseIpAddress",
        )
        cidr_ip_address_read.prefix_length = AAZIntType(
            serialized_name="prefixLength",
        )

        _schema.base_ip_address = cls._schema_cidr_ip_address_read.base_ip_address
        _schema.prefix_length = cls._schema_cidr_ip_address_read.prefix_length


__all__ = ["List"]
