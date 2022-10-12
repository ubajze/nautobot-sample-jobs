import random
import string
import time
from nautobot.extras.jobs import Job, IntegerVar
from nautobot.extras.models import Status
from nautobot.dcim.models import Site

class CreateSite(Job):

    class Meta:

        name = "Create Site"
        description = "The job creates a new site using the random string"
        read_only = False

    delay = IntegerVar(description="Number of seconds to wait before starting the job.", label="Delay.", min_value=0, max_value=300, default=0)

    def run(self, data=None, commit=None):
        site_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        site_status = Status.objects.get_for_model(Site).get(slug="active")

        delay = data["delay"]
        if delay:
            self.log_success(f"Delay the execution for {delay}")
            time.sleep(delay)

        self.site, created = Site.objects.get_or_create(
            name=site_name,
            slug=site_name,
            status=site_status,
        )

        if created:
            log_message = f"Site {site_name} successfully created"
        else:
            log_message = f"Site {site_name} already exists"
        self.log_success(log_message)
