# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.page
from cdp.page import (
    AdFrameExplanation,
    AdFrameStatus,
    AdFrameType,
    AdScriptId,
    AppManifestError,
    AppManifestParsedProperties,
    AutoResponseMode,
    BackForwardCacheNotRestoredExplanation,
    BackForwardCacheNotRestoredExplanationTree,
    BackForwardCacheNotRestoredReason,
    BackForwardCacheNotRestoredReasonType,
    BackForwardCacheNotUsed,
    ClientNavigationDisposition,
    ClientNavigationReason,
    CompilationCacheParams,
    CompilationCacheProduced,
    CrossOriginIsolatedContextType,
    DialogType,
    DocumentOpened,
    DomContentEventFired,
    FileChooserOpened,
    FontFamilies,
    FontSizes,
    Frame,
    FrameAttached,
    FrameDetached,
    FrameId,
    FrameNavigated,
    FrameRequestedNavigation,
    FrameResized,
    FrameResource,
    FrameResourceTree,
    FrameStartedLoading,
    FrameStoppedLoading,
    FrameTree,
    GatedAPIFeatures,
    InstallabilityError,
    InstallabilityErrorArgument,
    InterstitialHidden,
    InterstitialShown,
    JavascriptDialogClosed,
    JavascriptDialogOpening,
    LayoutViewport,
    LifecycleEvent,
    LoadEventFired,
    NavigatedWithinDocument,
    NavigationEntry,
    NavigationType,
    OriginTrial,
    OriginTrialStatus,
    OriginTrialToken,
    OriginTrialTokenStatus,
    OriginTrialTokenWithStatus,
    OriginTrialUsageRestriction,
    PermissionsPolicyBlockLocator,
    PermissionsPolicyBlockReason,
    PermissionsPolicyFeature,
    PermissionsPolicyFeatureState,
    ReferrerPolicy,
    ScreencastFrame,
    ScreencastFrameMetadata,
    ScreencastVisibilityChanged,
    ScriptFontFamilies,
    ScriptIdentifier,
    SecureContextType,
    TransitionType,
    Viewport,
    VisualViewport,
    WindowOpen
)


async def DownloadProgress(
        guid: str,
        total_bytes: float,
        received_bytes: float,
        state: str
    ) -> None:
    '''
    **EXPERIMENTAL**

    Fired when download makes progress. Last call has ``done`` == true.
    Deprecated. Use Browser.downloadProgress instead.
    '''
    session = get_session_context('page.DownloadProgress')
    return await session.execute(cdp.page.DownloadProgress(guid, total_bytes, received_bytes, state))


async def DownloadWillBegin(
        frame_id: FrameId,
        guid: str,
        url: str,
        suggested_filename: str
    ) -> None:
    '''
    **EXPERIMENTAL**

    Fired when page is about to start a download.
    Deprecated. Use Browser.downloadWillBegin instead.
    '''
    session = get_session_context('page.DownloadWillBegin')
    return await session.execute(cdp.page.DownloadWillBegin(frame_id, guid, url, suggested_filename))


async def FrameClearedScheduledNavigation(
        frame_id: FrameId
    ) -> None:
    '''
    Fired when frame no longer has a scheduled navigation.
    '''
    session = get_session_context('page.FrameClearedScheduledNavigation')
    return await session.execute(cdp.page.FrameClearedScheduledNavigation(frame_id))


async def FrameScheduledNavigation(
        frame_id: FrameId,
        delay: float,
        reason: ClientNavigationReason,
        url: str
    ) -> None:
    '''
    Fired when frame schedules a potential navigation.
    '''
    session = get_session_context('page.FrameScheduledNavigation')
    return await session.execute(cdp.page.FrameScheduledNavigation(frame_id, delay, reason, url))


async def add_compilation_cache(
        url: str,
        data: str
    ) -> None:
    '''
    Seeds compilation cache for given url. Compilation cache does not survive
    cross-process navigation.

    **EXPERIMENTAL**

    :param url:
    :param data: Base64-encoded data (Encoded as a base64 string when passed over JSON)
    '''
    session = get_session_context('page.add_compilation_cache')
    return await session.execute(cdp.page.add_compilation_cache(url, data))


async def add_script_to_evaluate_on_load(
        script_source: str
    ) -> ScriptIdentifier:
    '''
    Deprecated, please use addScriptToEvaluateOnNewDocument instead.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param script_source:
    :returns: Identifier of the added script.
    '''
    session = get_session_context('page.add_script_to_evaluate_on_load')
    return await session.execute(cdp.page.add_script_to_evaluate_on_load(script_source))


async def add_script_to_evaluate_on_new_document(
        source: str,
        world_name: typing.Optional[str] = None,
        include_command_line_api: typing.Optional[bool] = None,
        run_immediately: typing.Optional[bool] = None
    ) -> ScriptIdentifier:
    '''
    Evaluates given script in every frame upon creation (before loading frame's scripts).

    :param source:
    :param world_name: **(EXPERIMENTAL)** *(Optional)* If specified, creates an isolated world with the given name and evaluates given script in it. This world name will be used as the ExecutionContextDescription::name when the corresponding event is emitted.
    :param include_command_line_api: **(EXPERIMENTAL)** *(Optional)* Specifies whether command line API should be available to the script, defaults to false.
    :param run_immediately: **(EXPERIMENTAL)** *(Optional)* If true, runs the script immediately on existing execution contexts or worlds. Default: false.
    :returns: Identifier of the added script.
    '''
    session = get_session_context('page.add_script_to_evaluate_on_new_document')
    return await session.execute(cdp.page.add_script_to_evaluate_on_new_document(source, world_name, include_command_line_api, run_immediately))


async def bring_to_front() -> None:
    '''
    Brings page to front (activates tab).
    '''
    session = get_session_context('page.bring_to_front')
    return await session.execute(cdp.page.bring_to_front())


async def capture_screenshot(
        format_: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        clip: typing.Optional[Viewport] = None,
        from_surface: typing.Optional[bool] = None,
        capture_beyond_viewport: typing.Optional[bool] = None,
        optimize_for_speed: typing.Optional[bool] = None
    ) -> str:
    '''
    Capture page screenshot.

    :param format_: *(Optional)* Image compression format (defaults to png).
    :param quality: *(Optional)* Compression quality from range [0..100] (jpeg only).
    :param clip: *(Optional)* Capture the screenshot of a given region only.
    :param from_surface: **(EXPERIMENTAL)** *(Optional)* Capture the screenshot from the surface, rather than the view. Defaults to true.
    :param capture_beyond_viewport: **(EXPERIMENTAL)** *(Optional)* Capture the screenshot beyond the viewport. Defaults to false.
    :param optimize_for_speed: **(EXPERIMENTAL)** *(Optional)* Optimize image encoding for speed, not for resulting size (defaults to false)
    :returns: Base64-encoded image data. (Encoded as a base64 string when passed over JSON)
    '''
    session = get_session_context('page.capture_screenshot')
    return await session.execute(cdp.page.capture_screenshot(format_, quality, clip, from_surface, capture_beyond_viewport, optimize_for_speed))


async def capture_snapshot(
        format_: typing.Optional[str] = None
    ) -> str:
    '''
    Returns a snapshot of the page as a string. For MHTML format, the serialization includes
    iframes, shadow DOM, external resources, and element-inline styles.

    **EXPERIMENTAL**

    :param format_: *(Optional)* Format (defaults to mhtml).
    :returns: Serialized page data.
    '''
    session = get_session_context('page.capture_snapshot')
    return await session.execute(cdp.page.capture_snapshot(format_))


async def clear_compilation_cache() -> None:
    '''
    Clears seeded compilation cache.

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.clear_compilation_cache')
    return await session.execute(cdp.page.clear_compilation_cache())


async def clear_device_metrics_override() -> None:
    '''
    Clears the overridden device metrics.

    .. deprecated:: 1.3

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.clear_device_metrics_override')
    return await session.execute(cdp.page.clear_device_metrics_override())


async def clear_device_orientation_override() -> None:
    '''
    Clears the overridden Device Orientation.

    .. deprecated:: 1.3

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.clear_device_orientation_override')
    return await session.execute(cdp.page.clear_device_orientation_override())


async def clear_geolocation_override() -> None:
    '''
    Clears the overridden Geolocation Position and Error.

    .. deprecated:: 1.3
    '''
    session = get_session_context('page.clear_geolocation_override')
    return await session.execute(cdp.page.clear_geolocation_override())


async def close() -> None:
    '''
    Tries to close page, running its beforeunload hooks, if any.

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.close')
    return await session.execute(cdp.page.close())


async def crash() -> None:
    '''
    Crashes renderer on the IO thread, generates minidumps.

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.crash')
    return await session.execute(cdp.page.crash())


async def create_isolated_world(
        frame_id: FrameId,
        world_name: typing.Optional[str] = None,
        grant_univeral_access: typing.Optional[bool] = None
    ) -> cdp.runtime.ExecutionContextId:
    '''
    Creates an isolated world for the given frame.

    :param frame_id: Id of the frame in which the isolated world should be created.
    :param world_name: *(Optional)* An optional name which is reported in the Execution Context.
    :param grant_univeral_access: *(Optional)* Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
    :returns: Execution context of the isolated world.
    '''
    session = get_session_context('page.create_isolated_world')
    return await session.execute(cdp.page.create_isolated_world(frame_id, world_name, grant_univeral_access))


async def delete_cookie(
        cookie_name: str,
        url: str
    ) -> None:
    '''
    Deletes browser cookie with given name, domain and path.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param cookie_name: Name of the cookie to remove.
    :param url: URL to match cooke domain and path.
    '''
    session = get_session_context('page.delete_cookie')
    return await session.execute(cdp.page.delete_cookie(cookie_name, url))


async def disable() -> None:
    '''
    Disables page domain notifications.
    '''
    session = get_session_context('page.disable')
    return await session.execute(cdp.page.disable())


async def enable() -> None:
    '''
    Enables page domain notifications.
    '''
    session = get_session_context('page.enable')
    return await session.execute(cdp.page.enable())


async def generate_test_report(
        message: str,
        group: typing.Optional[str] = None
    ) -> None:
    '''
    Generates a report for testing.

    **EXPERIMENTAL**

    :param message: Message to be displayed in the report.
    :param group: *(Optional)* Specifies the endpoint group to deliver the report to.
    '''
    session = get_session_context('page.generate_test_report')
    return await session.execute(cdp.page.generate_test_report(message, group))


async def get_ad_script_id(
        frame_id: FrameId
    ) -> typing.Optional[AdScriptId]:
    '''


    **EXPERIMENTAL**

    :param frame_id:
    :returns: *(Optional)* Identifies the bottom-most script which caused the frame to be labelled as an ad. Only sent if frame is labelled as an ad and id is available.
    '''
    session = get_session_context('page.get_ad_script_id')
    return await session.execute(cdp.page.get_ad_script_id(frame_id))


async def get_app_id() -> typing.Tuple[typing.Optional[str], typing.Optional[str]]:
    '''
    Returns the unique (PWA) app id.
    Only returns values if the feature flag 'WebAppEnableManifestId' is enabled

    **EXPERIMENTAL**

    :returns: A tuple with the following items:

        0. **appId** - *(Optional)* App id, either from manifest's id attribute or computed from start_url
        1. **recommendedId** - *(Optional)* Recommendation for manifest's id attribute to match current id computed from start_url
    '''
    session = get_session_context('page.get_app_id')
    return await session.execute(cdp.page.get_app_id())


async def get_app_manifest() -> typing.Tuple[str, typing.List[AppManifestError], typing.Optional[str], typing.Optional[AppManifestParsedProperties]]:
    '''


    :returns: A tuple with the following items:

        0. **url** - Manifest location.
        1. **errors** - 
        2. **data** - *(Optional)* Manifest content.
        3. **parsed** - *(Optional)* Parsed manifest properties
    '''
    session = get_session_context('page.get_app_manifest')
    return await session.execute(cdp.page.get_app_manifest())


async def get_cookies() -> typing.List[cdp.network.Cookie]:
    '''
    Returns all browser cookies for the page and all of its subframes. Depending
    on the backend support, will return detailed cookie information in the
    ``cookies`` field.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :returns: Array of cookie objects.
    '''
    session = get_session_context('page.get_cookies')
    return await session.execute(cdp.page.get_cookies())


async def get_frame_tree() -> FrameTree:
    '''
    Returns present frame tree structure.

    :returns: Present frame tree structure.
    '''
    session = get_session_context('page.get_frame_tree')
    return await session.execute(cdp.page.get_frame_tree())


async def get_installability_errors() -> typing.List[InstallabilityError]:
    '''


    **EXPERIMENTAL**

    :returns: 
    '''
    session = get_session_context('page.get_installability_errors')
    return await session.execute(cdp.page.get_installability_errors())


async def get_layout_metrics() -> typing.Tuple[LayoutViewport, VisualViewport, cdp.dom.Rect, LayoutViewport, VisualViewport, cdp.dom.Rect]:
    '''
    Returns metrics relating to the layouting of the page, such as viewport bounds/scale.

    :returns: A tuple with the following items:

        0. **layoutViewport** - Deprecated metrics relating to the layout viewport. Is in device pixels. Use ``cssLayoutViewport`` instead.
        1. **visualViewport** - Deprecated metrics relating to the visual viewport. Is in device pixels. Use ``cssVisualViewport`` instead.
        2. **contentSize** - Deprecated size of scrollable area. Is in DP. Use ``cssContentSize`` instead.
        3. **cssLayoutViewport** - Metrics relating to the layout viewport in CSS pixels.
        4. **cssVisualViewport** - Metrics relating to the visual viewport in CSS pixels.
        5. **cssContentSize** - Size of scrollable area in CSS pixels.
    '''
    session = get_session_context('page.get_layout_metrics')
    return await session.execute(cdp.page.get_layout_metrics())


async def get_manifest_icons() -> typing.Optional[str]:
    '''
    Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :returns: 
    '''
    session = get_session_context('page.get_manifest_icons')
    return await session.execute(cdp.page.get_manifest_icons())


async def get_navigation_history() -> typing.Tuple[int, typing.List[NavigationEntry]]:
    '''
    Returns navigation history for the current page.

    :returns: A tuple with the following items:

        0. **currentIndex** - Index of the current navigation history entry.
        1. **entries** - Array of navigation history entries.
    '''
    session = get_session_context('page.get_navigation_history')
    return await session.execute(cdp.page.get_navigation_history())


async def get_origin_trials(
        frame_id: FrameId
    ) -> typing.List[OriginTrial]:
    '''
    Get Origin Trials on given frame.

    **EXPERIMENTAL**

    :param frame_id:
    :returns: 
    '''
    session = get_session_context('page.get_origin_trials')
    return await session.execute(cdp.page.get_origin_trials(frame_id))


async def get_permissions_policy_state(
        frame_id: FrameId
    ) -> typing.List[PermissionsPolicyFeatureState]:
    '''
    Get Permissions Policy state on given frame.

    **EXPERIMENTAL**

    :param frame_id:
    :returns: 
    '''
    session = get_session_context('page.get_permissions_policy_state')
    return await session.execute(cdp.page.get_permissions_policy_state(frame_id))


async def get_resource_content(
        frame_id: FrameId,
        url: str
    ) -> typing.Tuple[str, bool]:
    '''
    Returns content of the given resource.

    **EXPERIMENTAL**

    :param frame_id: Frame id to get resource for.
    :param url: URL of the resource to get content for.
    :returns: A tuple with the following items:

        0. **content** - Resource content.
        1. **base64Encoded** - True, if content was served as base64.
    '''
    session = get_session_context('page.get_resource_content')
    return await session.execute(cdp.page.get_resource_content(frame_id, url))


async def get_resource_tree() -> FrameResourceTree:
    '''
    Returns present frame / resource tree structure.

    **EXPERIMENTAL**

    :returns: Present frame / resource tree structure.
    '''
    session = get_session_context('page.get_resource_tree')
    return await session.execute(cdp.page.get_resource_tree())


async def handle_java_script_dialog(
        accept: bool,
        prompt_text: typing.Optional[str] = None
    ) -> None:
    '''
    Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).

    :param accept: Whether to accept or dismiss the dialog.
    :param prompt_text: *(Optional)* The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
    '''
    session = get_session_context('page.handle_java_script_dialog')
    return await session.execute(cdp.page.handle_java_script_dialog(accept, prompt_text))


async def navigate(
        url: str,
        referrer: typing.Optional[str] = None,
        transition_type: typing.Optional[TransitionType] = None,
        frame_id: typing.Optional[FrameId] = None,
        referrer_policy: typing.Optional[ReferrerPolicy] = None
    ) -> typing.Tuple[FrameId, typing.Optional[cdp.network.LoaderId], typing.Optional[str]]:
    '''
    Navigates current page to the given URL.

    :param url: URL to navigate the page to.
    :param referrer: *(Optional)* Referrer URL.
    :param transition_type: *(Optional)* Intended transition type.
    :param frame_id: *(Optional)* Frame id to navigate, if not specified navigates the top frame.
    :param referrer_policy: **(EXPERIMENTAL)** *(Optional)* Referrer-policy used for the navigation.
    :returns: A tuple with the following items:

        0. **frameId** - Frame id that has navigated (or failed to navigate)
        1. **loaderId** - *(Optional)* Loader identifier. This is omitted in case of same-document navigation, as the previously committed loaderId would not change.
        2. **errorText** - *(Optional)* User friendly error message, present if and only if navigation has failed.
    '''
    session = get_session_context('page.navigate')
    return await session.execute(cdp.page.navigate(url, referrer, transition_type, frame_id, referrer_policy))


async def navigate_to_history_entry(
        entry_id: int
    ) -> None:
    '''
    Navigates current page to the given history entry.

    :param entry_id: Unique id of the entry to navigate to.
    '''
    session = get_session_context('page.navigate_to_history_entry')
    return await session.execute(cdp.page.navigate_to_history_entry(entry_id))


async def print_to_pdf(
        landscape: typing.Optional[bool] = None,
        display_header_footer: typing.Optional[bool] = None,
        print_background: typing.Optional[bool] = None,
        scale: typing.Optional[float] = None,
        paper_width: typing.Optional[float] = None,
        paper_height: typing.Optional[float] = None,
        margin_top: typing.Optional[float] = None,
        margin_bottom: typing.Optional[float] = None,
        margin_left: typing.Optional[float] = None,
        margin_right: typing.Optional[float] = None,
        page_ranges: typing.Optional[str] = None,
        header_template: typing.Optional[str] = None,
        footer_template: typing.Optional[str] = None,
        prefer_css_page_size: typing.Optional[bool] = None,
        transfer_mode: typing.Optional[str] = None,
        generate_tagged_pdf: typing.Optional[bool] = None
    ) -> typing.Tuple[str, typing.Optional[cdp.io.StreamHandle]]:
    '''
    Print page as PDF.

    :param landscape: *(Optional)* Paper orientation. Defaults to false.
    :param display_header_footer: *(Optional)* Display header and footer. Defaults to false.
    :param print_background: *(Optional)* Print background graphics. Defaults to false.
    :param scale: *(Optional)* Scale of the webpage rendering. Defaults to 1.
    :param paper_width: *(Optional)* Paper width in inches. Defaults to 8.5 inches.
    :param paper_height: *(Optional)* Paper height in inches. Defaults to 11 inches.
    :param margin_top: *(Optional)* Top margin in inches. Defaults to 1cm (~0.4 inches).
    :param margin_bottom: *(Optional)* Bottom margin in inches. Defaults to 1cm (~0.4 inches).
    :param margin_left: *(Optional)* Left margin in inches. Defaults to 1cm (~0.4 inches).
    :param margin_right: *(Optional)* Right margin in inches. Defaults to 1cm (~0.4 inches).
    :param page_ranges: *(Optional)* Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are printed in the document order, not in the order specified, and no more than once. Defaults to empty string, which implies the entire document is printed. The page numbers are quietly capped to actual page count of the document, and ranges beyond the end of the document are ignored. If this results in no pages to print, an error is reported. It is an error to specify a range with start greater than end.
    :param header_template: *(Optional)* HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - ```date````: formatted print date - ````title````: document title - ````url````: document location - ````pageNumber````: current page number - ````totalPages````: total pages in the document  For example, ````<span class=title></span>```` would generate span containing the title.
    :param footer_template: *(Optional)* HTML template for the print footer. Should use the same format as the ````headerTemplate````.
    :param prefer_css_page_size: *(Optional)* Whether or not to prefer page size as defined by css. Defaults to false, in which case the content will be scaled to fit the paper size.
    :param transfer_mode: **(EXPERIMENTAL)** *(Optional)* return as stream
    :param generate_tagged_pdf: **(EXPERIMENTAL)** *(Optional)* Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice.
    :returns: A tuple with the following items:

        0. **data** - Base64-encoded pdf data. Empty if `` returnAsStream` is specified. (Encoded as a base64 string when passed over JSON)
        1. **stream** - *(Optional)* A handle of the stream that holds resulting PDF data.
    '''
    session = get_session_context('page.print_to_pdf')
    return await session.execute(cdp.page.print_to_pdf(landscape, display_header_footer, print_background, scale, paper_width, paper_height, margin_top, margin_bottom, margin_left, margin_right, page_ranges, header_template, footer_template, prefer_css_page_size, transfer_mode, generate_tagged_pdf))


async def produce_compilation_cache(
        scripts: typing.List[CompilationCacheParams]
    ) -> None:
    '''
    Requests backend to produce compilation cache for the specified scripts.
    ``scripts`` are appeneded to the list of scripts for which the cache
    would be produced. The list may be reset during page navigation.
    When script with a matching URL is encountered, the cache is optionally
    produced upon backend discretion, based on internal heuristics.
    See also: ``Page.compilationCacheProduced``.

    **EXPERIMENTAL**

    :param scripts:
    '''
    session = get_session_context('page.produce_compilation_cache')
    return await session.execute(cdp.page.produce_compilation_cache(scripts))


async def reload(
        ignore_cache: typing.Optional[bool] = None,
        script_to_evaluate_on_load: typing.Optional[str] = None
    ) -> None:
    '''
    Reloads given page optionally ignoring the cache.

    :param ignore_cache: *(Optional)* If true, browser cache is ignored (as if the user pressed Shift+refresh).
    :param script_to_evaluate_on_load: *(Optional)* If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin.
    '''
    session = get_session_context('page.reload')
    return await session.execute(cdp.page.reload(ignore_cache, script_to_evaluate_on_load))


async def remove_script_to_evaluate_on_load(
        identifier: ScriptIdentifier
    ) -> None:
    '''
    Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param identifier:
    '''
    session = get_session_context('page.remove_script_to_evaluate_on_load')
    return await session.execute(cdp.page.remove_script_to_evaluate_on_load(identifier))


async def remove_script_to_evaluate_on_new_document(
        identifier: ScriptIdentifier
    ) -> None:
    '''
    Removes given script from the list.

    :param identifier:
    '''
    session = get_session_context('page.remove_script_to_evaluate_on_new_document')
    return await session.execute(cdp.page.remove_script_to_evaluate_on_new_document(identifier))


async def reset_navigation_history() -> None:
    '''
    Resets navigation history for the current page.
    '''
    session = get_session_context('page.reset_navigation_history')
    return await session.execute(cdp.page.reset_navigation_history())


async def screencast_frame_ack(
        session_id: int
    ) -> None:
    '''
    Acknowledges that a screencast frame has been received by the frontend.

    **EXPERIMENTAL**

    :param session_id: Frame number.
    '''
    session = get_session_context('page.screencast_frame_ack')
    return await session.execute(cdp.page.screencast_frame_ack(session_id))


async def search_in_resource(
        frame_id: FrameId,
        url: str,
        query: str,
        case_sensitive: typing.Optional[bool] = None,
        is_regex: typing.Optional[bool] = None
    ) -> typing.List[cdp.debugger.SearchMatch]:
    '''
    Searches for given string in resource content.

    **EXPERIMENTAL**

    :param frame_id: Frame id for resource to search in.
    :param url: URL of the resource to search in.
    :param query: String to search for.
    :param case_sensitive: *(Optional)* If true, search is case sensitive.
    :param is_regex: *(Optional)* If true, treats string parameter as regex.
    :returns: List of search matches.
    '''
    session = get_session_context('page.search_in_resource')
    return await session.execute(cdp.page.search_in_resource(frame_id, url, query, case_sensitive, is_regex))


async def set_ad_blocking_enabled(
        enabled: bool
    ) -> None:
    '''
    Enable Chrome's experimental ad filter on all sites.

    **EXPERIMENTAL**

    :param enabled: Whether to block ads.
    '''
    session = get_session_context('page.set_ad_blocking_enabled')
    return await session.execute(cdp.page.set_ad_blocking_enabled(enabled))


async def set_bypass_csp(
        enabled: bool
    ) -> None:
    '''
    Enable page Content Security Policy by-passing.

    **EXPERIMENTAL**

    :param enabled: Whether to bypass page CSP.
    '''
    session = get_session_context('page.set_bypass_csp')
    return await session.execute(cdp.page.set_bypass_csp(enabled))


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
        screen_orientation: typing.Optional[cdp.emulation.ScreenOrientation] = None,
        viewport: typing.Optional[Viewport] = None
    ) -> None:
    '''
    Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
    window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
    query results).

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
    :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
    :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
    :param scale: *(Optional)* Scale to apply to resulting view image.
    :param screen_width: *(Optional)* Overriding screen width value in pixels (minimum 0, maximum 10000000).
    :param screen_height: *(Optional)* Overriding screen height value in pixels (minimum 0, maximum 10000000).
    :param position_x: *(Optional)* Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
    :param position_y: *(Optional)* Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
    :param dont_set_visible_size: *(Optional)* Do not set visible view size, rely upon explicit setVisibleSize call.
    :param screen_orientation: *(Optional)* Screen orientation override.
    :param viewport: *(Optional)* The viewport dimensions and scale. If not set, the override is cleared.
    '''
    session = get_session_context('page.set_device_metrics_override')
    return await session.execute(cdp.page.set_device_metrics_override(width, height, device_scale_factor, mobile, scale, screen_width, screen_height, position_x, position_y, dont_set_visible_size, screen_orientation, viewport))


async def set_device_orientation_override(
        alpha: float,
        beta: float,
        gamma: float
    ) -> None:
    '''
    Overrides the Device Orientation.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param alpha: Mock alpha
    :param beta: Mock beta
    :param gamma: Mock gamma
    '''
    session = get_session_context('page.set_device_orientation_override')
    return await session.execute(cdp.page.set_device_orientation_override(alpha, beta, gamma))


async def set_document_content(
        frame_id: FrameId,
        html: str
    ) -> None:
    '''
    Sets given markup as the document's HTML.

    :param frame_id: Frame id to set HTML for.
    :param html: HTML content to set.
    '''
    session = get_session_context('page.set_document_content')
    return await session.execute(cdp.page.set_document_content(frame_id, html))


async def set_download_behavior(
        behavior: str,
        download_path: typing.Optional[str] = None
    ) -> None:
    '''
    Set the behavior when downloading a file.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny).
    :param download_path: *(Optional)* The default path to save downloaded files to. This is required if behavior is set to 'allow'
    '''
    session = get_session_context('page.set_download_behavior')
    return await session.execute(cdp.page.set_download_behavior(behavior, download_path))


async def set_font_families(
        font_families: FontFamilies,
        for_scripts: typing.Optional[typing.List[ScriptFontFamilies]] = None
    ) -> None:
    '''
    Set generic font families.

    **EXPERIMENTAL**

    :param font_families: Specifies font families to set. If a font family is not specified, it won't be changed.
    :param for_scripts: *(Optional)* Specifies font families to set for individual scripts.
    '''
    session = get_session_context('page.set_font_families')
    return await session.execute(cdp.page.set_font_families(font_families, for_scripts))


async def set_font_sizes(
        font_sizes: FontSizes
    ) -> None:
    '''
    Set default font sizes.

    **EXPERIMENTAL**

    :param font_sizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
    '''
    session = get_session_context('page.set_font_sizes')
    return await session.execute(cdp.page.set_font_sizes(font_sizes))


async def set_geolocation_override(
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        accuracy: typing.Optional[float] = None
    ) -> None:
    '''
    Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
    unavailable.

    .. deprecated:: 1.3

    :param latitude: *(Optional)* Mock latitude
    :param longitude: *(Optional)* Mock longitude
    :param accuracy: *(Optional)* Mock accuracy
    '''
    session = get_session_context('page.set_geolocation_override')
    return await session.execute(cdp.page.set_geolocation_override(latitude, longitude, accuracy))


async def set_intercept_file_chooser_dialog(
        enabled: bool
    ) -> None:
    '''
    Intercept file chooser requests and transfer control to protocol clients.
    When file chooser interception is enabled, native file chooser dialog is not shown.
    Instead, a protocol event ``Page.fileChooserOpened`` is emitted.

    **EXPERIMENTAL**

    :param enabled:
    '''
    session = get_session_context('page.set_intercept_file_chooser_dialog')
    return await session.execute(cdp.page.set_intercept_file_chooser_dialog(enabled))


async def set_lifecycle_events_enabled(
        enabled: bool
    ) -> None:
    '''
    Controls whether page will emit lifecycle events.

    **EXPERIMENTAL**

    :param enabled: If true, starts emitting lifecycle events.
    '''
    session = get_session_context('page.set_lifecycle_events_enabled')
    return await session.execute(cdp.page.set_lifecycle_events_enabled(enabled))


async def set_prerendering_allowed(
        is_allowed: bool
    ) -> None:
    '''
    Enable/disable prerendering manually.

    This command is a short-term solution for https://crbug.com/1440085.
    See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA
    for more details.

    TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets.

    **EXPERIMENTAL**

    :param is_allowed:
    '''
    session = get_session_context('page.set_prerendering_allowed')
    return await session.execute(cdp.page.set_prerendering_allowed(is_allowed))


async def set_rph_registration_mode(
        mode: AutoResponseMode
    ) -> None:
    '''
    Extensions for Custom Handlers API:
    https://html.spec.whatwg.org/multipage/system-state.html#rph-automation

    **EXPERIMENTAL**

    :param mode:
    '''
    session = get_session_context('page.set_rph_registration_mode')
    return await session.execute(cdp.page.set_rph_registration_mode(mode))


async def set_spc_transaction_mode(
        mode: AutoResponseMode
    ) -> None:
    '''
    Sets the Secure Payment Confirmation transaction mode.
    https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode

    **EXPERIMENTAL**

    :param mode:
    '''
    session = get_session_context('page.set_spc_transaction_mode')
    return await session.execute(cdp.page.set_spc_transaction_mode(mode))


async def set_touch_emulation_enabled(
        enabled: bool,
        configuration: typing.Optional[str] = None
    ) -> None:
    '''
    Toggles mouse event-based touch event emulation.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param enabled: Whether the touch event emulation should be enabled.
    :param configuration: *(Optional)* Touch/gesture events configuration. Default: current platform.
    '''
    session = get_session_context('page.set_touch_emulation_enabled')
    return await session.execute(cdp.page.set_touch_emulation_enabled(enabled, configuration))


async def set_web_lifecycle_state(
        state: str
    ) -> None:
    '''
    Tries to update the web lifecycle state of the page.
    It will transition the page to the given state according to:
    https://github.com/WICG/web-lifecycle/

    **EXPERIMENTAL**

    :param state: Target lifecycle state
    '''
    session = get_session_context('page.set_web_lifecycle_state')
    return await session.execute(cdp.page.set_web_lifecycle_state(state))


async def start_screencast(
        format_: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        max_width: typing.Optional[int] = None,
        max_height: typing.Optional[int] = None,
        every_nth_frame: typing.Optional[int] = None
    ) -> None:
    '''
    Starts sending each frame using the ``screencastFrame`` event.

    **EXPERIMENTAL**

    :param format_: *(Optional)* Image compression format.
    :param quality: *(Optional)* Compression quality from range [0..100].
    :param max_width: *(Optional)* Maximum screenshot width.
    :param max_height: *(Optional)* Maximum screenshot height.
    :param every_nth_frame: *(Optional)* Send every n-th frame.
    '''
    session = get_session_context('page.start_screencast')
    return await session.execute(cdp.page.start_screencast(format_, quality, max_width, max_height, every_nth_frame))


async def stop_loading() -> None:
    '''
    Force the page stop all navigations and pending resource fetches.
    '''
    session = get_session_context('page.stop_loading')
    return await session.execute(cdp.page.stop_loading())


async def stop_screencast() -> None:
    '''
    Stops sending each frame in the ``screencastFrame``.

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.stop_screencast')
    return await session.execute(cdp.page.stop_screencast())


async def wait_for_debugger() -> None:
    '''
    Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.

    **EXPERIMENTAL**
    '''
    session = get_session_context('page.wait_for_debugger')
    return await session.execute(cdp.page.wait_for_debugger())
