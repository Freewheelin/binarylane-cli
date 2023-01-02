from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.available_advanced_server_features_response import AvailableAdvancedServerFeaturesResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/available_advanced_features".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AvailableAdvancedServerFeaturesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: Client,
) -> Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
    """Fetch the Currently Available Advanced Features for a Server

    Args:
        server_id (int): The target server id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
    """Fetch the Currently Available Advanced Features for a Server

    Args:
        server_id (int): The target server id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
) -> Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
    """Fetch the Currently Available Advanced Features for a Server

    Args:
        server_id (int): The target server id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
    """Fetch the Currently Available Advanced Features for a Server

    Args:
        server_id (int): The target server id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed
