
from nautobot.dcim.models.devices import Platform

from nautobot.apps.jobs import Job, register_jobs


import random
import string
import time
from nautobot.extras.jobs import Job, IntegerVar
from nautobot.extras.models import Status
from nautobot.dcim.models import Site

class RecreatePlatform(Job):

    class Meta:

        name = "Recreate Platform"
        description = "The job reads, delete, and create platforms"
        read_only = False

    def run(self):

        logger.info("The job started.")


        logger.info("Get the platform.")
        p = Platform.objects.first()
        name = p.name

        logger.info("Delete the platform %s", name)
        p.delete()
        logger.info("Deleted.")

        try:
            p1 = Platform.objects.get(name=name)
            logger.info("The platform %s found.", name)
        except:
            logger.info("The platform %s not found.", name)

        p.save()

        try:
            p1 = Platform.objects.get(name=name)
            logger.info("The platform %s found.", name)
        except:
            logger.info("The platform %s not found.", name)

        logger.info("The job completed.")


register_jobs(RecreatePlatform)
