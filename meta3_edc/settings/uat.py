from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=1)
EDC_SITES_UAT_DOMAIN = True
ALLOWED_HOSTS = [
    "amana.uat.tz.meta3.clinicedc.org",
    "bunju.uat.tz.meta3.clinicedc.org",
    "hindu-mandal.uat.tz.meta3.clinicedc.org",
    "mkuranga.uat.tz.meta3.clinicedc.org",
    "mwananyamala.uat.tz.meta3.clinicedc.org",
    "localhost",
]
