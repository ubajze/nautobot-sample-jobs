import requests
from nautobot.apps import jobs


class WebRequest(jobs.Job):

    class Meta:

        name = "Web Request job"
        description = "The job performs a web request to the defined URL"

        read_only = False

    url = jobs.URLVar(
        description="The URL to perform the web request to",
        default="https://example.com",
    )

    def run(self, *, url):

        self.logger.info("The job started.")

        self.logger.info("Performing a web request to %s.", url)
        try:
            response = requests.get(url)
            self.logger.info("The response status code is %s.", response.status_code)
            self.logger.info("The response content is %s.", response.text)
        except Exception as e:
            self.logger.error("An error occurred while performing the web request: %s", str(e))

        self.logger.info("The job completed.")


jobs.register_jobs(WebRequest)
