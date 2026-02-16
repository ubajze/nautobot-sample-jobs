from nautobot.apps import jobs
from nautobot.extras.models.secrets import Secret


class RetriveSecret(jobs.Job):

    class Meta:

        name = "Retrieve secret"
        description = "The job retrieves a secret from the vault"

        read_only = False

    secret = jobs.ObjectVar(
        description="Secret that should be retrieved from vault",
        default=None,
        model=Secret
    )

    def run(self, *, secret):

        self.logger.info("The job started.")
        self.logger.info("Retrieving the secret %s from vault.", secret.name)
        secret_value = secret.get_value()
        self.logger.info("The secret value is %s.", secret_value)
        self.logger.info("The job completed.")


jobs.register_jobs(RetriveSecret)
