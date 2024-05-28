
import random
from nautobot.dcim.models.devices import Platform
from nautobot.apps.jobs import Job, register_jobs

class RecreatePlatform(Job):

    class Meta:

        name = "Recreate Platform"
        description = "The job reads, delete, and create platforms"
        read_only = False

    def run(self):

        self.logger.info("The job started.")

        for i in range(1000):
            p = Platform.objects.first()

            name = p.name
            self.logger.info("Processing the platform %s.", name)

            self.logger.info("Delete the platform %s", name)
            p.delete()
            self.logger.info("Deleted.")

            try:
                p1 = Platform.objects.get(name=name)
                self.logger.info("The platform %s found.", name)
            except:
                self.logger.info("The platform %s not found.", name)

            self.logger.info("Recreating the platform.")
            p.name = name.replace("platform", "s-platform")
            p.save()
            self.logger.info("Done")

            try:
                p1 = Platform.objects.get(name=name)
                self.logger.info("The platform %s found.", name)
            except:
                self.logger.info("The platform %s not found.", name)

        self.logger.info("The job completed.")


register_jobs(RecreatePlatform)
