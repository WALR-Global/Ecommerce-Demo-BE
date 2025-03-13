from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user  # Get the authenticated user

        # Get user groups
        groups = list(user.groups.values_list("name", flat=True))
        # data["groups"] = groups

        # Set the role as the first group, or None if no groups exist
        data["role"] = groups[0] if groups else None

        # Get user permissions
        data["permissions"] = groups

        # Get user groups
        # data["groups"] = list(user.groups.values_list("name", flat=True))

        # Get user permissions
        # data["permissions"] = list(user.user_permissions.values_list("codename", flat=True))
        # data["permissions"] = list(user.groups.values_list("name", flat=True))

        return data
