from django.contrib.auth.models import User,PermissionsMixin


class User(User,PermissionsMixin):
    
    def __str__(self):
        return f"@{self.username}"
