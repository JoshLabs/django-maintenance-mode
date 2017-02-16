# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.core.management.base import BaseCommand
from maintenance_mode import settings


class Command(BaseCommand):

    args = '<relative|absolute> org_ids'
    help = (
        "Include Organizations to Maintenance Mode. First argument is (R)elative/(A)bsolute. "
        "Relative Argument adds to previous list. Absolute argument recreates the list. Default is relative"
        "This is followed by List of Org IDs. "
        "These organization will be in maintenance mode"
    )

    def handle(self, *args, **options):

        mode = args[0].lower()

        if mode in ["a", "absolute"]:
            settings.MAINTENANCE_INCLUDED_ORGS = []

        for org_id in args[1:]:
            settings.MAINTENANCE_INCLUDED_ORGS.append(org_id)
