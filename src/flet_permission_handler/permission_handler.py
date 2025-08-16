from typing import Optional

import flet as ft

from flet_permission_handler.types import Permission, PermissionStatus

__all__ = ["PermissionHandler"]


@ft.control("PermissionHandler")
class PermissionHandler(ft.Service):
    """
    Manages permissions for the application.

    This control is non-visual and should be added
    to [`Page.services`][flet.Page.services] list.

    Danger: Platform support
        Currently only supported on Android, iOS, Windows, and Web platforms.

    Raises:
        FletUnsupportedPlatformException: If the platform is not supported.
    """

    def before_update(self):
        super().before_update()

        # validate platform
        if not (
            self.page.web
            or self.page.platform
            in [
                ft.PagePlatform.ANDROID,
                ft.PagePlatform.IOS,
                ft.PagePlatform.WINDOWS,
            ]
        ):
            raise ft.FletUnsupportedPlatformException(
                "PermissionHandler is currently only supported on Android, iOS, "
                "Windows, and Web platforms."
            )

    async def get_status(
        self, permission: Permission, timeout: int = 10
    ) -> Optional[PermissionStatus]:
        """
        Gets the current status of the given `permission`.

        Args:
            permission: The `Permission` to check the status for.
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Returns:
            A `PermissionStatus` if the status is known, otherwise `None`.

        Raises:
            TimeoutError: If the request times out.
        """
        status = await self._invoke_method(
            method_name="get_status",
            arguments={"permission": permission},
            timeout=timeout,
        )
        return PermissionStatus(status) if status is not None else None

    async def request(
        self, permission: Permission, timeout: int = 60
    ) -> Optional[PermissionStatus]:
        """
        Request the user for access to the `permission` if access hasn't already been
        granted access before.

        Args:
            permission: The `Permission` to request.
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Returns:
            The new `PermissionStatus` after the request, or `None` if the request
                was not successful.

        Raises:
            TimeoutError: If the request times out.
        """
        r = await self._invoke_method(
            method_name="request",
            arguments={"permission": permission},
            timeout=timeout,
        )
        return PermissionStatus(r) if r is not None else None

    async def open_app_settings(self, timeout: int = 10) -> bool:
        """
        Opens the app settings page.

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Returns:
            `True` if the app settings page could be opened, otherwise `False`.

        Raises:
            TimeoutError: If the request times out.
        """
        return await self._invoke_method(
            method_name="open_app_settings",
            timeout=timeout,
        )
