import unittest

from tests.utils.test_embedded_messages import Test_embedded_welcome_messages


def run_suite():

    """
    Startet alle Tests im Projekt und gibt den Statuscode zurück.
    """
    suite = unittest.TestSuite()
    suite.addTests(Test_embedded_welcome_messages)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_suite()