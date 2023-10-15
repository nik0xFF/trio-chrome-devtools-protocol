# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.layer_tree
from cdp.layer_tree import (
    Layer,
    LayerId,
    LayerPainted,
    LayerTreeDidChange,
    PaintProfile,
    PictureTile,
    ScrollRect,
    SnapshotId,
    StickyPositionConstraint
)


async def compositing_reasons(
        layer_id: LayerId
    ) -> typing.Tuple[typing.List[str], typing.List[str]]:
    '''
    Provides the reasons why the given layer was composited.

    :param layer_id: The id of the layer for which we want to get the reasons it was composited.
    :returns: A tuple with the following items:

        0. **compositingReasons** - A list of strings specifying reasons for the given layer to become composited.
        1. **compositingReasonIds** - A list of strings specifying reason IDs for the given layer to become composited.
    '''
    session = get_session_context('layer_tree.compositing_reasons')
    return await session.execute(cdp.layer_tree.compositing_reasons(layer_id))


async def disable() -> None:
    '''
    Disables compositing tree inspection.
    '''
    session = get_session_context('layer_tree.disable')
    return await session.execute(cdp.layer_tree.disable())


async def enable() -> None:
    '''
    Enables compositing tree inspection.
    '''
    session = get_session_context('layer_tree.enable')
    return await session.execute(cdp.layer_tree.enable())


async def load_snapshot(
        tiles: typing.List[PictureTile]
    ) -> SnapshotId:
    '''
    Returns the snapshot identifier.

    :param tiles: An array of tiles composing the snapshot.
    :returns: The id of the snapshot.
    '''
    session = get_session_context('layer_tree.load_snapshot')
    return await session.execute(cdp.layer_tree.load_snapshot(tiles))


async def make_snapshot(
        layer_id: LayerId
    ) -> SnapshotId:
    '''
    Returns the layer snapshot identifier.

    :param layer_id: The id of the layer.
    :returns: The id of the layer snapshot.
    '''
    session = get_session_context('layer_tree.make_snapshot')
    return await session.execute(cdp.layer_tree.make_snapshot(layer_id))


async def profile_snapshot(
        snapshot_id: SnapshotId,
        min_repeat_count: typing.Optional[int] = None,
        min_duration: typing.Optional[float] = None,
        clip_rect: typing.Optional[cdp.dom.Rect] = None
    ) -> typing.List[PaintProfile]:
    '''
    :param snapshot_id: The id of the layer snapshot.
    :param min_repeat_count: *(Optional)* The maximum number of times to replay the snapshot (1, if not specified).
    :param min_duration: *(Optional)* The minimum duration (in seconds) to replay the snapshot.
    :param clip_rect: *(Optional)* The clip rectangle to apply when replaying the snapshot.
    :returns: The array of paint profiles, one per run.
    '''
    session = get_session_context('layer_tree.profile_snapshot')
    return await session.execute(cdp.layer_tree.profile_snapshot(snapshot_id, min_repeat_count, min_duration, clip_rect))


async def release_snapshot(
        snapshot_id: SnapshotId
    ) -> None:
    '''
    Releases layer snapshot captured by the back-end.

    :param snapshot_id: The id of the layer snapshot.
    '''
    session = get_session_context('layer_tree.release_snapshot')
    return await session.execute(cdp.layer_tree.release_snapshot(snapshot_id))


async def replay_snapshot(
        snapshot_id: SnapshotId,
        from_step: typing.Optional[int] = None,
        to_step: typing.Optional[int] = None,
        scale: typing.Optional[float] = None
    ) -> str:
    '''
    Replays the layer snapshot and returns the resulting bitmap.

    :param snapshot_id: The id of the layer snapshot.
    :param from_step: *(Optional)* The first step to replay from (replay from the very start if not specified).
    :param to_step: *(Optional)* The last step to replay to (replay till the end if not specified).
    :param scale: *(Optional)* The scale to apply while replaying (defaults to 1).
    :returns: A data: URL for resulting image.
    '''
    session = get_session_context('layer_tree.replay_snapshot')
    return await session.execute(cdp.layer_tree.replay_snapshot(snapshot_id, from_step, to_step, scale))


async def snapshot_command_log(
        snapshot_id: SnapshotId
    ) -> typing.List[dict]:
    '''
    Replays the layer snapshot and returns canvas log.

    :param snapshot_id: The id of the layer snapshot.
    :returns: The array of canvas function calls.
    '''
    session = get_session_context('layer_tree.snapshot_command_log')
    return await session.execute(cdp.layer_tree.snapshot_command_log(snapshot_id))
