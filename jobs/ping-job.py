import sys
import re
import subprocess
from nautobot.apps import jobs


class Ping(jobs.Job):

    class Meta:

        name = "Ping job"
        description = "The job performs a ping to the defined host"
        read_only = False

    host = jobs.TextVar(
        description="The host to perform the ping to",
        default="10.0.0.1",
    )
    number_of_packets = jobs.IntegerVar(
        description="The number of packets to send",
        default=5,
    )

    def run(self, *, host, number_of_packets):

        self.logger.info("The job started.")

        self.logger.info("Performing a ping to %s.", host)
        try:
            proc = subprocess.run(['ping', '-c', str(number_of_packets), host], capture_output=True, text=True)
            self.logger.info("Ping output:\n%s", proc.stdout)
            m = re.search(r'(\d+) packets transmitted, (\d+) received', proc.stdout)
            if m:
                sent = int(m.group(1))
                received = int(m.group(2))
                lost = sent - received
                self.logger.info("Ping statistics: sent=%d, received=%d, lost=%d", sent, received, lost)
            self.logger.info("Ping job completed.")
        except Exception as e:
            self.logger.error("An error occurred while performing the ping: %s", str(e))
            sys.exit(1)


jobs.register_jobs(Ping)
