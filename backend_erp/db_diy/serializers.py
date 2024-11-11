from rest_framework import serializers
from .models import Role, Entity, RolePermission, Users

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['entity_id', 'entity_name']

class RolePermissionSerializer(serializers.ModelSerializer):
    entity = serializers.PrimaryKeyRelatedField(queryset=Entity.objects.all())

    class Meta:
        model = RolePermission
        fields = ['entity', 'view', 'create', 'edit', 'delete', 'full_access']

class RoleSerializer(serializers.ModelSerializer):
    role_permissions = RolePermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = ['role_id', 'role_name', 'description', 'role_permissions']

    def create(self, validated_data):
        role_permissions_data = validated_data.pop('role_permissions', [])
        role = Role.objects.create(**validated_data)

        for role_permission_data in role_permissions_data:
            RolePermission.objects.create(
                role=role,
                entity=role_permission_data['entity'],
                view=role_permission_data.get('view', False),
                create=role_permission_data.get('create', False),
                edit=role_permission_data.get('edit', False),
                delete=role_permission_data.get('delete', False),
                full_access=role_permission_data.get('full_access', False),
            )
        return role

    def update(self, instance, validated_data):
        instance.role_name = validated_data.get('role_name', instance.role_name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        role_permissions_data = validated_data.pop('role_permissions', [])
        existing_permissions = {(rp.entity.entity_id, rp.role.role_id) for rp in instance.role_permissions.all()}

        for role_permission_data in role_permissions_data:
            entity = role_permission_data['entity']

            if (entity.entity_id, instance.role_id) in existing_permissions:
                role_permission = RolePermission.objects.get(role=instance, entity=entity)
                role_permission.view = role_permission_data.get('view', role_permission.view)
                role_permission.create = role_permission_data.get('create', role_permission.create)
                role_permission.edit = role_permission_data.get('edit', role_permission.edit)
                role_permission.delete = role_permission_data.get('delete', role_permission.delete)
                role_permission.full_access = role_permission_data.get('full_access', role_permission.full_access)
                role_permission.save()
            else:
                RolePermission.objects.create(
                    role=instance,
                    entity=entity, 
                    view=role_permission_data.get('view', False),
                    create=role_permission_data.get('create', False),
                    edit=role_permission_data.get('edit', False),
                    delete=role_permission_data.get('delete', False),
                    full_access=role_permission_data.get('full_access', False),
                )

        return instance


class UserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'fullname', 'dob', 'email', 'tels', 'address', 'gender', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance