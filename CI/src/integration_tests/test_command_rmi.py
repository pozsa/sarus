import unittest

import common.util as util


class TestCommandRmi(unittest.TestCase):
    """
    These tests verify that the images are correctly removed.
    """

    def test_command_rmi_with_local_repository(self):
        self._test_command_rmi(is_centralized_repository=False)

    def test_command_rmi_with_centralized_repository(self):
        self._test_command_rmi(is_centralized_repository=True)

    def _test_command_rmi(self, is_centralized_repository):
        image = "alpine:latest"

        util.pull_image_if_necessary(is_centralized_repository, image)
        actual_images = set(util.list_images(is_centralized_repository))
        self.assertTrue(image in actual_images)

        util.remove_image_if_necessary(is_centralized_repository, image)
        actual_images = set(util.list_images(is_centralized_repository))
        self.assertTrue(image not in actual_images)