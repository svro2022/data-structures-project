"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue, Node


class TestQueue(unittest.TestCase):
    """
    Класс для тестирования класса Queue
    """

    def test_init_node(self):
        first = Node(5, None)
        self.assertEqual(first.data, 5)
        self.assertEqual(first.next_node, None)

    def test_init_queue(self):
        queue = Queue()
        self.assertIsNone(queue.head)

    def test_enqueue_queue(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        queue.enqueue("test")
        self.assertEqual(queue.head.data, "test")

    def test_str_queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert str(queue) == "data1\ndata2\ndata3"

        queue1 = Queue()
        assert str(queue1) == ""

    def test_dequeue(self):
        four = Queue()
        four.enqueue('data1')
        four.enqueue('data2')
        four.enqueue('data3')

        assert four.dequeue() == 'data1'
        assert four.dequeue() == 'data2'
        assert four.dequeue() == 'data3'
        assert four.dequeue() is None

