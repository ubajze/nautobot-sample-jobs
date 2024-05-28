
from nautobot.dcim.models.devices import Platform
from nautobot.apps.jobs import Job, register_jobs

class RecreatePlatform(Job):

    class Meta:

        name = "Recreate Platform"
        description = "The job reads, delete, and create platforms"
        read_only = False

    def run(self):

        self.logger.info("The job started.")

        self.logger.info("Get the platform.")
        p = Platform.objects.first()
        name = p.name

        self.logger.info("Delete the platform %s", name)
        p.delete()
        self.logger.info("Deleted.")

        try:
            p1 = Platform.objects.get(name=name)
            self.logger.info("The platform %s found.", name)
        except:
            self.logger.info("The platform %s not found.", name)

        p.save()

        try:
            p1 = Platform.objects.get(name=name)
            self.logger.info("The platform %s found.", name)
        except:
            self.logger.info("The platform %s not found.", name)

        self.logger.info("The job completed.")


register_jobs(RecreatePlatform)
