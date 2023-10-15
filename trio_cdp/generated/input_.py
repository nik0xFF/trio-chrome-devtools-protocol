# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.input_
from cdp.input_ import (
    DragData,
    DragDataItem,
    DragIntercepted,
    GestureSourceType,
    MouseButton,
    TimeSinceEpoch,
    TouchPoint
)


async def cancel_dragging() -> None:
    '''
    Cancels any active dragging in the page.
    '''
    session = get_session_context('input_.cancel_dragging')
    return await session.execute(cdp.input_.cancel_dragging())


async def dispatch_drag_event(
        type_: str,
        x: float,
        y: float,
        data: DragData,
        modifiers: typing.Optional[int] = None
    ) -> None:
    '''
    Dispatches a drag event into the page.

    **EXPERIMENTAL**

    :param type_: Type of the drag event.
    :param x: X coordinate of the event relative to the main frame's viewport in CSS pixels.
    :param y: Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
    :param data:
    :param modifiers: *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
    '''
    session = get_session_context('input_.dispatch_drag_event')
    return await session.execute(cdp.input_.dispatch_drag_event(type_, x, y, data, modifiers))


async def dispatch_key_event(
        type_: str,
        modifiers: typing.Optional[int] = None,
        timestamp: typing.Optional[TimeSinceEpoch] = None,
        text: typing.Optional[str] = None,
        unmodified_text: typing.Optional[str] = None,
        key_identifier: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        windows_virtual_key_code: typing.Optional[int] = None,
        native_virtual_key_code: typing.Optional[int] = None,
        auto_repeat: typing.Optional[bool] = None,
        is_keypad: typing.Optional[bool] = None,
        is_system_key: typing.Optional[bool] = None,
        location: typing.Optional[int] = None,
        commands: typing.Optional[typing.List[str]] = None
    ) -> None:
    '''
    Dispatches a key event to the page.

    :param type_: Type of the key event.
    :param modifiers: *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
    :param timestamp: *(Optional)* Time at which the event occurred.
    :param text: *(Optional)* Text as generated by processing a virtual key code with a keyboard layout. Not needed for for ```keyUp```` and ````rawKeyDown```` events (default: "")
    :param unmodified_text: *(Optional)* Text that would have been generated by the keyboard if no modifiers were pressed (except for shift). Useful for shortcut (accelerator) key handling (default: "").
    :param key_identifier: *(Optional)* Unique key identifier (e.g., 'U+0041') (default: "").
    :param code: *(Optional)* Unique DOM defined string value for each physical key (e.g., 'KeyA') (default: "").
    :param key: *(Optional)* Unique DOM defined string value describing the meaning of the key in the context of active modifiers, keyboard layout, etc (e.g., 'AltGr') (default: "").
    :param windows_virtual_key_code: *(Optional)* Windows virtual key code (default: 0).
    :param native_virtual_key_code: *(Optional)* Native virtual key code (default: 0).
    :param auto_repeat: *(Optional)* Whether the event was generated from auto repeat (default: false).
    :param is_keypad: *(Optional)* Whether the event was generated from the keypad (default: false).
    :param is_system_key: *(Optional)* Whether the event was a system key event (default: false).
    :param location: *(Optional)* Whether the event was from the left or right side of the keyboard. 1=Left, 2=Right (default: 0).
    :param commands: **(EXPERIMENTAL)** *(Optional)* Editing commands to send with the key event (e.g., 'selectAll') (default: []). These are related to but not equal the command names used in ````document.execCommand``` and NSStandardKeyBindingResponding. See https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/editing/commands/editor_command_names.h for valid command names.
    '''
    session = get_session_context('input_.dispatch_key_event')
    return await session.execute(cdp.input_.dispatch_key_event(type_, modifiers, timestamp, text, unmodified_text, key_identifier, code, key, windows_virtual_key_code, native_virtual_key_code, auto_repeat, is_keypad, is_system_key, location, commands))


async def dispatch_mouse_event(
        type_: str,
        x: float,
        y: float,
        modifiers: typing.Optional[int] = None,
        timestamp: typing.Optional[TimeSinceEpoch] = None,
        button: typing.Optional[MouseButton] = None,
        buttons: typing.Optional[int] = None,
        click_count: typing.Optional[int] = None,
        force: typing.Optional[float] = None,
        tangential_pressure: typing.Optional[float] = None,
        tilt_x: typing.Optional[float] = None,
        tilt_y: typing.Optional[float] = None,
        twist: typing.Optional[int] = None,
        delta_x: typing.Optional[float] = None,
        delta_y: typing.Optional[float] = None,
        pointer_type: typing.Optional[str] = None
    ) -> None:
    '''
    Dispatches a mouse event to the page.

    :param type_: Type of the mouse event.
    :param x: X coordinate of the event relative to the main frame's viewport in CSS pixels.
    :param y: Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
    :param modifiers: *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
    :param timestamp: *(Optional)* Time at which the event occurred.
    :param button: *(Optional)* Mouse button (default: "none").
    :param buttons: *(Optional)* A number indicating which buttons are pressed on the mouse when a mouse event is triggered. Left=1, Right=2, Middle=4, Back=8, Forward=16, None=0.
    :param click_count: *(Optional)* Number of times the mouse button was clicked (default: 0).
    :param force: **(EXPERIMENTAL)** *(Optional)* The normalized pressure, which has a range of [0,1] (default: 0).
    :param tangential_pressure: **(EXPERIMENTAL)** *(Optional)* The normalized tangential pressure, which has a range of [-1,1] (default: 0).
    :param tilt_x: *(Optional)* The plane angle between the Y-Z plane and the plane containing both the stylus axis and the Y axis, in degrees of the range [-90,90], a positive tiltX is to the right (default: 0).
    :param tilt_y: *(Optional)* The plane angle between the X-Z plane and the plane containing both the stylus axis and the X axis, in degrees of the range [-90,90], a positive tiltY is towards the user (default: 0).
    :param twist: **(EXPERIMENTAL)** *(Optional)* The clockwise rotation of a pen stylus around its own major axis, in degrees in the range [0,359] (default: 0).
    :param delta_x: *(Optional)* X delta in CSS pixels for mouse wheel event (default: 0).
    :param delta_y: *(Optional)* Y delta in CSS pixels for mouse wheel event (default: 0).
    :param pointer_type: *(Optional)* Pointer type (default: "mouse").
    '''
    session = get_session_context('input_.dispatch_mouse_event')
    return await session.execute(cdp.input_.dispatch_mouse_event(type_, x, y, modifiers, timestamp, button, buttons, click_count, force, tangential_pressure, tilt_x, tilt_y, twist, delta_x, delta_y, pointer_type))


async def dispatch_touch_event(
        type_: str,
        touch_points: typing.List[TouchPoint],
        modifiers: typing.Optional[int] = None,
        timestamp: typing.Optional[TimeSinceEpoch] = None
    ) -> None:
    '''
    Dispatches a touch event to the page.

    :param type_: Type of the touch event. TouchEnd and TouchCancel must not contain any touch points, while TouchStart and TouchMove must contains at least one.
    :param touch_points: Active touch points on the touch device. One event per any changed point (compared to previous touch event in a sequence) is generated, emulating pressing/moving/releasing points one by one.
    :param modifiers: *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
    :param timestamp: *(Optional)* Time at which the event occurred.
    '''
    session = get_session_context('input_.dispatch_touch_event')
    return await session.execute(cdp.input_.dispatch_touch_event(type_, touch_points, modifiers, timestamp))


async def emulate_touch_from_mouse_event(
        type_: str,
        x: int,
        y: int,
        button: MouseButton,
        timestamp: typing.Optional[TimeSinceEpoch] = None,
        delta_x: typing.Optional[float] = None,
        delta_y: typing.Optional[float] = None,
        modifiers: typing.Optional[int] = None,
        click_count: typing.Optional[int] = None
    ) -> None:
    '''
    Emulates touch event from the mouse event parameters.

    **EXPERIMENTAL**

    :param type_: Type of the mouse event.
    :param x: X coordinate of the mouse pointer in DIP.
    :param y: Y coordinate of the mouse pointer in DIP.
    :param button: Mouse button. Only "none", "left", "right" are supported.
    :param timestamp: *(Optional)* Time at which the event occurred (default: current time).
    :param delta_x: *(Optional)* X delta in DIP for mouse wheel event (default: 0).
    :param delta_y: *(Optional)* Y delta in DIP for mouse wheel event (default: 0).
    :param modifiers: *(Optional)* Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
    :param click_count: *(Optional)* Number of times the mouse button was clicked (default: 0).
    '''
    session = get_session_context('input_.emulate_touch_from_mouse_event')
    return await session.execute(cdp.input_.emulate_touch_from_mouse_event(type_, x, y, button, timestamp, delta_x, delta_y, modifiers, click_count))


async def ime_set_composition(
        text: str,
        selection_start: int,
        selection_end: int,
        replacement_start: typing.Optional[int] = None,
        replacement_end: typing.Optional[int] = None
    ) -> None:
    '''
    This method sets the current candidate text for ime.
    Use imeCommitComposition to commit the final text.
    Use imeSetComposition with empty string as text to cancel composition.

    **EXPERIMENTAL**

    :param text: The text to insert
    :param selection_start: selection start
    :param selection_end: selection end
    :param replacement_start: *(Optional)* replacement start
    :param replacement_end: *(Optional)* replacement end
    '''
    session = get_session_context('input_.ime_set_composition')
    return await session.execute(cdp.input_.ime_set_composition(text, selection_start, selection_end, replacement_start, replacement_end))


async def insert_text(
        text: str
    ) -> None:
    '''
    This method emulates inserting text that doesn't come from a key press,
    for example an emoji keyboard or an IME.

    **EXPERIMENTAL**

    :param text: The text to insert.
    '''
    session = get_session_context('input_.insert_text')
    return await session.execute(cdp.input_.insert_text(text))


async def set_ignore_input_events(
        ignore: bool
    ) -> None:
    '''
    Ignores input events (useful while auditing page).

    :param ignore: Ignores input events processing when set to true.
    '''
    session = get_session_context('input_.set_ignore_input_events')
    return await session.execute(cdp.input_.set_ignore_input_events(ignore))


async def set_intercept_drags(
        enabled: bool
    ) -> None:
    '''
    Prevents default drag and drop behavior and instead emits ``Input.dragIntercepted`` events.
    Drag and drop behavior can be directly controlled via ``Input.dispatchDragEvent``.

    **EXPERIMENTAL**

    :param enabled:
    '''
    session = get_session_context('input_.set_intercept_drags')
    return await session.execute(cdp.input_.set_intercept_drags(enabled))


async def synthesize_pinch_gesture(
        x: float,
        y: float,
        scale_factor: float,
        relative_speed: typing.Optional[int] = None,
        gesture_source_type: typing.Optional[GestureSourceType] = None
    ) -> None:
    '''
    Synthesizes a pinch gesture over a time period by issuing appropriate touch events.

    **EXPERIMENTAL**

    :param x: X coordinate of the start of the gesture in CSS pixels.
    :param y: Y coordinate of the start of the gesture in CSS pixels.
    :param scale_factor: Relative scale factor after zooming (>1.0 zooms in, <1.0 zooms out).
    :param relative_speed: *(Optional)* Relative pointer speed in pixels per second (default: 800).
    :param gesture_source_type: *(Optional)* Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
    '''
    session = get_session_context('input_.synthesize_pinch_gesture')
    return await session.execute(cdp.input_.synthesize_pinch_gesture(x, y, scale_factor, relative_speed, gesture_source_type))


async def synthesize_scroll_gesture(
        x: float,
        y: float,
        x_distance: typing.Optional[float] = None,
        y_distance: typing.Optional[float] = None,
        x_overscroll: typing.Optional[float] = None,
        y_overscroll: typing.Optional[float] = None,
        prevent_fling: typing.Optional[bool] = None,
        speed: typing.Optional[int] = None,
        gesture_source_type: typing.Optional[GestureSourceType] = None,
        repeat_count: typing.Optional[int] = None,
        repeat_delay_ms: typing.Optional[int] = None,
        interaction_marker_name: typing.Optional[str] = None
    ) -> None:
    '''
    Synthesizes a scroll gesture over a time period by issuing appropriate touch events.

    **EXPERIMENTAL**

    :param x: X coordinate of the start of the gesture in CSS pixels.
    :param y: Y coordinate of the start of the gesture in CSS pixels.
    :param x_distance: *(Optional)* The distance to scroll along the X axis (positive to scroll left).
    :param y_distance: *(Optional)* The distance to scroll along the Y axis (positive to scroll up).
    :param x_overscroll: *(Optional)* The number of additional pixels to scroll back along the X axis, in addition to the given distance.
    :param y_overscroll: *(Optional)* The number of additional pixels to scroll back along the Y axis, in addition to the given distance.
    :param prevent_fling: *(Optional)* Prevent fling (default: true).
    :param speed: *(Optional)* Swipe speed in pixels per second (default: 800).
    :param gesture_source_type: *(Optional)* Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
    :param repeat_count: *(Optional)* The number of times to repeat the gesture (default: 0).
    :param repeat_delay_ms: *(Optional)* The number of milliseconds delay between each repeat. (default: 250).
    :param interaction_marker_name: *(Optional)* The name of the interaction markers to generate, if not empty (default: "").
    '''
    session = get_session_context('input_.synthesize_scroll_gesture')
    return await session.execute(cdp.input_.synthesize_scroll_gesture(x, y, x_distance, y_distance, x_overscroll, y_overscroll, prevent_fling, speed, gesture_source_type, repeat_count, repeat_delay_ms, interaction_marker_name))


async def synthesize_tap_gesture(
        x: float,
        y: float,
        duration: typing.Optional[int] = None,
        tap_count: typing.Optional[int] = None,
        gesture_source_type: typing.Optional[GestureSourceType] = None
    ) -> None:
    '''
    Synthesizes a tap gesture over a time period by issuing appropriate touch events.

    **EXPERIMENTAL**

    :param x: X coordinate of the start of the gesture in CSS pixels.
    :param y: Y coordinate of the start of the gesture in CSS pixels.
    :param duration: *(Optional)* Duration between touchdown and touchup events in ms (default: 50).
    :param tap_count: *(Optional)* Number of times to perform the tap (e.g. 2 for double tap, default: 1).
    :param gesture_source_type: *(Optional)* Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
    '''
    session = get_session_context('input_.synthesize_tap_gesture')
    return await session.execute(cdp.input_.synthesize_tap_gesture(x, y, duration, tap_count, gesture_source_type))
