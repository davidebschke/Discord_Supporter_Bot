import unittest

from tests.utils.test_embedded_messages import Test_embedded_welcome_messages
from tests.groupFeatures.test_tree_commands import Test_tree_commands


def run_suite():

    """
    Startet alle Tests im Projekt und gibt den Statuscode zurück.
    """
    suite = unittest.TestSuite()
    suite.addTests(Test_embedded_welcome_messages)
    suite.addTests(Test_tree_commands)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_suite()