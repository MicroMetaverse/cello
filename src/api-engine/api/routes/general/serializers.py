#
# SPDX-License-Identifier: Apache-2.0
#
from abc import ABC

from rest_framework import serializers


class RegisterBody(serializers.Serializer):
    orgName = serializers.CharField(help_text="name of Organization")
    email = serializers.EmailField(help_text="email of user")
    username = serializers.CharField(
        help_text="name of Administrator", default="Administator")
    password = serializers.CharField(
        help_text="password of Administrator", default="666666")
    passwordAgain = serializers.CharField(help_text="password of Administrator")


class RegisterIDSerializer(serializers.Serializer):
    id = serializers.UUIDField(help_text="ID of Organization")


class RegisterResponse(serializers.Serializer):
    id = serializers.UUIDField(help_text="ID of Organization")
    #msg = serializers.CharField(help_text="name of Organization")


class LoginBody(serializers.Serializer):
    orgName = serializers.CharField(help_text="name of Organization")
    username = serializers.CharField(help_text="name of user")
    password = serializers.CharField(help_text="password of user")
