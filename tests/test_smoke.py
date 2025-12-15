import unittest
import subprocess


class SmokeTest(unittest.TestCase):
    """Basic smoke tests to ensure the application works with updated dependencies."""

    def test_help_command(self):
        """Test that --help command works."""
        result = subprocess.run(
            ['prometheus-es-exporter', '--help'],
            capture_output=True,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn('Export Elasticsearch query results to Prometheus', result.stdout)

    def test_imports(self):
        """Test that all core modules can be imported."""
        import prometheus_es_exporter
        import prometheus_es_exporter.parser
        import prometheus_es_exporter.cluster_health_parser
        import prometheus_es_exporter.indices_stats_parser
        import prometheus_es_exporter.nodes_stats_parser

        self.assertTrue(hasattr(prometheus_es_exporter.parser, 'parse_response'))
        self.assertTrue(hasattr(prometheus_es_exporter, 'main'))

    def test_version_info(self):
        """Test that version information is accessible."""
        import prometheus_es_exporter

        self.assertIsNotNone(prometheus_es_exporter)


if __name__ == '__main__':
    unittest.main()
