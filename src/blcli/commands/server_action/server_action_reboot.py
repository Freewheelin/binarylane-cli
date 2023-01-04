from typing import Any, Union

from ...client.api.server_action.server_action_reboot import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.reboot import Reboot
from ...client.models.reboot_type import RebootType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_reboot"

    @property
    def description(self):
        return """Request a Server Perform a Reboot"""

    def configure(self, parser):
        """Add arguments for server-action_reboot"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=RebootType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: RebootType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Reboot(
                type=type,
            ),
        ).parsed
