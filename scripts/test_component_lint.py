import tempfile
import unittest
from pathlib import Path

from component_lint import lint_file, lint_html, reference_errors


class ComponentLintTests(unittest.TestCase):
    def test_current_libraries_and_references(self):
        root = Path(__file__).resolve().parents[1]
        refs = [root / 'references/theme-moyu-blue.md', root / 'references/common-components.md']
        for path in refs:
            self.assertEqual(lint_file(str(path))[1], [])
        self.assertEqual(reference_errors(str(root), [str(p) for p in refs]), [])

    def test_inline_underline_rejected_in_callout(self):
        for style in ['border-bottom:3px solid #287CFB', 'text-decoration:underline']:
            self.assertTrue(lint_html(f'<span style="{style}"><span leaf="">内容</span></span>', '9b'))

    def test_explicit_source_underline_supported(self):
        html = '<span style="border-bottom:2px solid #A5C5FC;font-weight:600;"><span leaf="">原文</span></span>'
        self.assertEqual(lint_html(html, '6e'), [])
        self.assertTrue(lint_html(html, '9b'))

    def test_dashed_box_requires_correct_component(self):
        html = '<section style="border:1px dashed #A5C5FC;text-align:center;"><span leaf="">内容</span></section>'
        self.assertEqual(lint_html(html, '9b'), [])
        self.assertEqual(lint_html(html, '2c', 'common'), [])
        self.assertTrue(lint_html(html, '9a'))
        self.assertTrue(lint_html(html.replace('text-align:center', 'text-align:left'), '9b'))

    def test_table_borders_and_deletion_are_not_underlines(self):
        html = '<td style="border-bottom:1px solid #E5E7EB;"><span style="text-decoration:line-through;"><span leaf="">内容</span></span></td>'
        self.assertEqual(lint_html(html, '11f'), [])

    def test_missing_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'references').mkdir()
            theme = root / 'references/theme-test.md'
            theme.write_text('### 9a. quote\n\n引用组件 99z\n', encoding='utf-8')
            (root / 'SKILL.md').write_text('使用 9a\n', encoding='utf-8')
            errors = reference_errors(tmp, [str(theme)])
            self.assertEqual(len(errors), 1)
            self.assertIn('99z', errors[0])


if __name__ == '__main__':
    unittest.main()
