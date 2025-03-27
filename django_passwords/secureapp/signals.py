import os

from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def update_site(sender, **kwargs):
    """
    Updates or creates the Site model after migrations.
    Ensures the domain and name are correctly set from environment variables.
    """
    SITE_ID = getattr(settings, "SITE_ID", 1)
    SITE_DOMAIN = os.getenv("DJANGO_SITE_DOMAIN", "example.com")
    SITE_NAME = os.getenv("DJANGO_SITE_NAME", "My Django App")

    try:
        site, created = Site.objects.get_or_create(id=SITE_ID)
        if created or site.domain != SITE_DOMAIN or site.name != SITE_NAME:
            site.domain = SITE_DOMAIN
            site.name = SITE_NAME
            site.save()
            print(f"✅ Site model updated: {site.domain}")
    except Exception as e:
        print(f"⚠️ Error updating Site model: {e}")  # Debugging
