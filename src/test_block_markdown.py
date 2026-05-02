import unittest
from block_markdown import block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        block = "1. first\n2. second"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        block = "this is just a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_wrong_number(self):
        block = "1. first\n3. second" # Skipped 2
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)