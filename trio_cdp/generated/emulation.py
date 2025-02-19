# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.emulation
from cdp.emulation import (
    DisabledImageType,
    DisplayFeature,
    MediaFeature,
    ScreenOrientation,
    UserAgentBrandVersion,
    UserAgentMetadata,
    VirtualTimeBudgetExpired,
    VirtualTimePolicy
)


async def can_emulate() -> bool:
    '''
    Tells whether emulation is supported.

    :returns: True if emulation is supported.
    '''
    session = get_session_context('emulation.can_emulate')
    return await session.execute(cdp.emulation.can_emulate())


async def clear_device_metrics_override() -> None:
    '''
    Clears the overridden device metrics.
    '''
    session = get_session_context('emulation.clear_device_metrics_override')
    return await session.execute(cdp.emulation.clear_device_metrics_override())


async def clear_geolocation_override() -> None:
    '''
    Clears the overridden Geolocation Position and Error.
    '''
    session = get_session_context('emulation.clear_geolocation_override')
    return await session.execute(cdp.emulation.clear_geolocation_override())


async def clear_idle_override() -> None:
    '''
    Clears Idle state overrides.

    **EXPERIMENTAL**
    '''
    session = get_session_context('emulation.clear_idle_override')
    return await session.execute(cdp.emulation.clear_idle_override())


async def reset_page_scale_factor() -> None:
    '''
    Requests that page scale factor is reset to initial values.

    **EXPERIMENTAL**
    '''
    session = get_session_context('emulation.reset_page_scale_factor')
    return await session.execute(cdp.emulation.reset_page_scale_factor())


async def set_auto_dark_mode_override(
        enabled: typing.Optional[bool] = None
    ) -> None:
    '''
    Automatically render all web contents using a dark theme.

    **EXPERIMENTAL**

    :param enabled: *(Optional)* Whether to enable or disable automatic dark mode. If not specified, any existing override will be cleared.
    '''
    session = get_session_context('emulation.set_auto_dark_mode_override')
    return await session.execute(cdp.emulation.set_auto_dark_mode_override(enabled))


async def set_automation_override(
        enabled: bool
    ) -> None:
    '''
    Allows overriding the automation flag.

    **EXPERIMENTAL**

    :param enabled: Whether the override should be enabled.
    '''
    session = get_session_context('emulation.set_automation_override')
    return await session.execute(cdp.emulation.set_automation_override(enabled))


async def set_cpu_throttling_rate(
        rate: float
    ) -> None:
    '''
    Enables CPU throttling to emulate slow CPUs.

    **EXPERIMENTAL**

    :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
    '''
    session = get_session_context('emulation.set_cpu_throttling_rate')
    return await session.execute(cdp.emulation.set_cpu_throttling_rate(rate))


async def set_default_background_color_override(
        color: typing.Optional[cdp.dom.RGBA] = None
    ) -> None:
    '''
    Sets or clears an override of the default background color of the frame. This override is used
    if the content does not specify one.

    :param color: *(Optional)* RGBA of the default background color. If not specified, any existing override will be cleared.
    '''
    session = get_session_context('emulation.set_default_background_color_override')
    return await session.execute(cdp.emulation.set_default_background_color_override(color))


async def set_device_metrics_override(
        width: int,
        height: int,
        device_scale_factor: float,
        mobile: bool,
        scale: typing.Optional[float] = None,
        screen_width: typing.Optional[int] = None,
        screen_height: typing.Optional[int] = None,
        position_x: typing.Optional[int] = None,
        position_y: typing.Optional[int] = None,
        dont_set_visible_size: typing.Optional[bool] = None,
        screen_orientation: typing.Optional[ScreenOrientation] = None,
        viewport: typing.Optional[cdp.page.Viewport] = None,
        display_feature: typing.Optional[DisplayFeature] = None
    ) -> None:
    '''
    Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
    window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
    query results).

    :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
    :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
    :param scale: **(EXPERIMENTAL)** *(Optional)* Scale to apply to resulting view image.
    :param screen_width: **(EXPERIMENTAL)** *(Optional)* Overriding screen width value in pixels (minimum 0, maximum 10000000).
    :param screen_height: **(EXPERIMENTAL)** *(Optional)* Overriding screen height value in pixels (minimum 0, maximum 10000000).
    :param position_x: **(EXPERIMENTAL)** *(Optional)* Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
    :param position_y: **(EXPERIMENTAL)** *(Optional)* Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
    :param dont_set_visible_size: **(EXPERIMENTAL)** *(Optional)* Do not set visible view size, rely upon explicit setVisibleSize call.
    :param screen_orientation: *(Optional)* Screen orientation override.
    :param viewport: **(EXPERIMENTAL)** *(Optional)* If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions.
    :param display_feature: **(EXPERIMENTAL)** *(Optional)* If set, the display feature of a multi-segment screen. If not set, multi-segment support is turned-off.
    '''
    session = get_session_context('emulation.set_device_metrics_override')
    return await session.execute(cdp.emulation.set_device_metrics_override(width, height, device_scale_factor, mobile, scale, screen_width, screen_height, position_x, position_y, dont_set_visible_size, screen_orientation, viewport, display_feature))


async def set_disabled_image_types(
        image_types: typing.List[DisabledImageType]
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param image_types: Image types to disable.
    '''
    session = get_session_context('emulation.set_disabled_image_types')
    return await session.execute(cdp.emulation.set_disabled_image_types(image_types))


async def set_document_cookie_disabled(
        disabled: bool
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param disabled: Whether document.coookie API should be disabled.
    '''
    session = get_session_context('emulation.set_document_cookie_disabled')
    return await session.execute(cdp.emulation.set_document_cookie_disabled(disabled))


async def set_emit_touch_events_for_mouse(
        enabled: bool,
        configuration: typing.Optional[str] = None
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param enabled: Whether touch emulation based on mouse input should be enabled.
    :param configuration: *(Optional)* Touch/gesture events configuration. Default: current platform.
    '''
    session = get_session_context('emulation.set_emit_touch_events_for_mouse')
    return await session.execute(cdp.emulation.set_emit_touch_events_for_mouse(enabled, configuration))


async def set_emulated_media(
        media: typing.Optional[str] = None,
        features: typing.Optional[typing.List[MediaFeature]] = None
    ) -> None:
    '''
    Emulates the given media type or media feature for CSS media queries.

    :param media: *(Optional)* Media type to emulate. Empty string disables the override.
    :param features: *(Optional)* Media features to emulate.
    '''
    session = get_session_context('emulation.set_emulated_media')
    return await session.execute(cdp.emulation.set_emulated_media(media, features))


async def set_emulated_vision_deficiency(
        type_: str
    ) -> None:
    '''
    Emulates the given vision deficiency.

    **EXPERIMENTAL**

    :param type_: Vision deficiency to emulate. Order: best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies.
    '''
    session = get_session_context('emulation.set_emulated_vision_deficiency')
    return await session.execute(cdp.emulation.set_emulated_vision_deficiency(type_))


async def set_focus_emulation_enabled(
        enabled: bool
    ) -> None:
    '''
    Enables or disables simulating a focused and active page.

    **EXPERIMENTAL**

    :param enabled: Whether to enable to disable focus emulation.
    '''
    session = get_session_context('emulation.set_focus_emulation_enabled')
    return await session.execute(cdp.emulation.set_focus_emulation_enabled(enabled))


async def set_geolocation_override(
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        accuracy: typing.Optional[float] = None
    ) -> None:
    '''
    Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
    unavailable.

    :param latitude: *(Optional)* Mock latitude
    :param longitude: *(Optional)* Mock longitude
    :param accuracy: *(Optional)* Mock accuracy
    '''
    session = get_session_context('emulation.set_geolocation_override')
    return await session.execute(cdp.emulation.set_geolocation_override(latitude, longitude, accuracy))


async def set_hardware_concurrency_override(
        hardware_concurrency: int
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param hardware_concurrency: Hardware concurrency to report
    '''
    session = get_session_context('emulation.set_hardware_concurrency_override')
    return await session.execute(cdp.emulation.set_hardware_concurrency_override(hardware_concurrency))


async def set_idle_override(
        is_user_active: bool,
        is_screen_unlocked: bool
    ) -> None:
    '''
    Overrides the Idle state.

    **EXPERIMENTAL**

    :param is_user_active: Mock isUserActive
    :param is_screen_unlocked: Mock isScreenUnlocked
    '''
    session = get_session_context('emulation.set_idle_override')
    return await session.execute(cdp.emulation.set_idle_override(is_user_active, is_screen_unlocked))


async def set_locale_override(
        locale: typing.Optional[str] = None
    ) -> None:
    '''
    Overrides default host system locale with the specified one.

    **EXPERIMENTAL**

    :param locale: *(Optional)* ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and restores default host system locale.
    '''
    session = get_session_context('emulation.set_locale_override')
    return await session.execute(cdp.emulation.set_locale_override(locale))


async def set_navigator_overrides(
        platform: str
    ) -> None:
    '''
    Overrides value returned by the javascript navigator object.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param platform: The platform navigator.platform should return.
    '''
    session = get_session_context('emulation.set_navigator_overrides')
    return await session.execute(cdp.emulation.set_navigator_overrides(platform))


async def set_page_scale_factor(
        page_scale_factor: float
    ) -> None:
    '''
    Sets a specified page scale factor.

    **EXPERIMENTAL**

    :param page_scale_factor: Page scale factor.
    '''
    session = get_session_context('emulation.set_page_scale_factor')
    return await session.execute(cdp.emulation.set_page_scale_factor(page_scale_factor))


async def set_script_execution_disabled(
        value: bool
    ) -> None:
    '''
    Switches script execution in the page.

    :param value: Whether script execution should be disabled in the page.
    '''
    session = get_session_context('emulation.set_script_execution_disabled')
    return await session.execute(cdp.emulation.set_script_execution_disabled(value))


async def set_scrollbars_hidden(
        hidden: bool
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param hidden: Whether scrollbars should be always hidden.
    '''
    session = get_session_context('emulation.set_scrollbars_hidden')
    return await session.execute(cdp.emulation.set_scrollbars_hidden(hidden))


async def set_timezone_override(
        timezone_id: str
    ) -> None:
    '''
    Overrides default host system timezone with the specified one.

    **EXPERIMENTAL**

    :param timezone_id: The timezone identifier. If empty, disables the override and restores default host system timezone.
    '''
    session = get_session_context('emulation.set_timezone_override')
    return await session.execute(cdp.emulation.set_timezone_override(timezone_id))


async def set_touch_emulation_enabled(
        enabled: bool,
        max_touch_points: typing.Optional[int] = None
    ) -> None:
    '''
    Enables touch on platforms which do not support them.

    :param enabled: Whether the touch event emulation should be enabled.
    :param max_touch_points: *(Optional)* Maximum touch points supported. Defaults to one.
    '''
    session = get_session_context('emulation.set_touch_emulation_enabled')
    return await session.execute(cdp.emulation.set_touch_emulation_enabled(enabled, max_touch_points))


async def set_user_agent_override(
        user_agent: str,
        accept_language: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        user_agent_metadata: typing.Optional[UserAgentMetadata] = None
    ) -> None:
    '''
    Allows overriding user agent with the given string.

    :param user_agent: User agent to use.
    :param accept_language: *(Optional)* Browser langugage to emulate.
    :param platform: *(Optional)* The platform navigator.platform should return.
    :param user_agent_metadata: **(EXPERIMENTAL)** *(Optional)* To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
    '''
    session = get_session_context('emulation.set_user_agent_override')
    return await session.execute(cdp.emulation.set_user_agent_override(user_agent, accept_language, platform, user_agent_metadata))


async def set_virtual_time_policy(
        policy: VirtualTimePolicy,
        budget: typing.Optional[float] = None,
        max_virtual_time_task_starvation_count: typing.Optional[int] = None,
        initial_virtual_time: typing.Optional[cdp.network.TimeSinceEpoch] = None
    ) -> float:
    '''
    Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
    the current virtual time policy.  Note this supersedes any previous time budget.

    **EXPERIMENTAL**

    :param policy:
    :param budget: *(Optional)* If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
    :param max_virtual_time_task_starvation_count: *(Optional)* If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock.
    :param initial_virtual_time: *(Optional)* If set, base::Time::Now will be overridden to initially return this value.
    :returns: Absolute timestamp at which virtual time was first enabled (up time in milliseconds).
    '''
    session = get_session_context('emulation.set_virtual_time_policy')
    return await session.execute(cdp.emulation.set_virtual_time_policy(policy, budget, max_virtual_time_task_starvation_count, initial_virtual_time))


async def set_visible_size(
        width: int,
        height: int
    ) -> None:
    '''
    Resizes the frame/viewport of the page. Note that this does not affect the frame's container
    (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
    on Android.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param width: Frame width (DIP).
    :param height: Frame height (DIP).
    '''
    session = get_session_context('emulation.set_visible_size')
    return await session.execute(cdp.emulation.set_visible_size(width, height))
