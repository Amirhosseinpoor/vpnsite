# from django.db import models
# from useraccount.models import CustomUser
#
# class LinkFragment(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='link_fragments')
#     vpn_link = models.TextField(blank=True)
#     fragment = models.CharField(max_length=255, blank=True)
#
#     def __str__(self):
#         # return f"{self.user.username} - {self.vpn_link}"
