
import time
from nautobot.apps import jobs


class WaitJob(jobs.Job):

    class Meta:

        name = "Wait job"
        description = "The job waits for defined time"

        read_only = False

    wait_time = jobs.IntegerVar(
        description="Time to wait in seconds",
        default=10,
        min_value=1,
        max_value=3600,
    )

    def run(self):

        self.logger.info("The job started.")

        for i in range(self.wait_time):
            self.logger.info("Waiting for %s seconds.", i + 1)
            time.sleep(1)

        self.logger.info("The job completed.")


jobs.register_jobs(WaitJob)
