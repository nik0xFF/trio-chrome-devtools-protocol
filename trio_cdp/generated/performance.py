# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.performance
from cdp.performance import (
    Metric,
    Metrics
)


async def disable() -> None:
    '''
    Disable collecting and reporting metrics.
    '''
    session = get_session_context('performance.disable')
    return await session.execute(cdp.performance.disable())


async def enable(
        time_domain: typing.Optional[str] = None
    ) -> None:
    '''
    Enable collecting and reporting metrics.

    :param time_domain: *(Optional)* Time domain to use for collecting and reporting duration metrics.
    '''
    session = get_session_context('performance.enable')
    return await session.execute(cdp.performance.enable(time_domain))


async def get_metrics() -> typing.List[Metric]:
    '''
    Retrieve current values of run-time metrics.

    :returns: Current values for run-time metrics.
    '''
    session = get_session_context('performance.get_metrics')
    return await session.execute(cdp.performance.get_metrics())


async def set_time_domain(
        time_domain: str
    ) -> None:
    '''
    Sets time domain to use for collecting and reporting duration metrics.
    Note that this must be called before enabling metrics collection. Calling
    this method while metrics collection is enabled returns an error.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param time_domain: Time domain
    '''
    session = get_session_context('performance.set_time_domain')
    return await session.execute(cdp.performance.set_time_domain(time_domain))
