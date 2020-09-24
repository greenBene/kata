import unittest
from ringbuffer import RingBuffer

class TestRingBuffer(unittest.TestCase):
    def test_count(self):
        buffer = RingBuffer(3)
        self.assertEqual(buffer.get_count(), 0)
        buffer.add(1)
        self.assertEqual(buffer.get_count(), 1)
        buffer.add(2)
        self.assertEqual(buffer.get_count(), 2)
        buffer.add(3)
        self.assertEqual(buffer.get_count(), 3)
        buffer.add(4)
        self.assertEqual(buffer.get_count(), 3)
        buffer.take()
        self.assertEqual(buffer.get_count(), 2)
        buffer.take()
        self.assertEqual(buffer.get_count(), 1)
        buffer.take()
        self.assertEqual(buffer.get_count(), 0)

    def test_content(self):
        buffer = RingBuffer(3)
        buffer.add(1)
        buffer.add('2')
        buffer.add(3.0)
        buffer.add(True)

        self.assertEqual(buffer.take(), True)
        self.assertEqual(buffer.take(), 3.0)
        self.assertEqual(buffer.take(), '2')
        self.assertEqual(buffer.get_count(), 0)

    def test_size(self):
        buffer = RingBuffer(3)

        self.assertEqual(buffer.get_size(), 3)

    def test_exception(self):
        buffer = RingBuffer(3)
        self.assertRaises(Exception, buffer.take)

if __name__ == '__main__':
    unittest.main()
