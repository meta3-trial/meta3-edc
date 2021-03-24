from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=1)
EDC_SITES_UAT_DOMAIN = False
ALLOWED_HOSTS = [
    "amana.tz.meta3.clinicedc.org",
    "bunju.tz.meta3.clinicedc.org",
    "hindu-mandal.tz.meta3.clinicedc.org",
    "mkuranga.tz.meta3.clinicedc.org",
    "mwananyamala.tz.meta3.clinicedc.org",
    "localhost",
]
