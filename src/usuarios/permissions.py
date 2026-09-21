from rest_framework import permissions

class PermissionsJefe(permissions.BasePermission):
    #Permisson custom para permitir acceso si usuario es staff
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.groups.filter(name="Jefe").exists() or request.user.is_superuser)

class PermissionEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.groups.filter(name__in=['Jefe','Empleado']).exists() or request.user.is_superuser)

class PermissionAlumno(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.groups.filter(name__in=['Jefe', 'Empleado', 'Alumno']).exists() or request.user.is_superuser)