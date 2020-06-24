#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
运用你所掌握的数据结构，设计和实现一个LRU (最近最少使用) 缓存机制。
它应该支持以下操作： 获取数据get和写入数据put。
获取数据 get(key)-如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value)-如果密钥不存在，则写入其数据值。
当缓存容量达到上限时，
它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？
"""

class LRUCache(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.key_dict = {}

    def get(self, key: int) -> int:
        if key in self.key_dict:
            index = self.keys.index(key)
            self.keys = [key] + self.keys[:index] + self.keys[index+1:]
        return self.key_dict.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.key_dict:
            self.key_dict[key] = value
            index = self.keys.index(key)
            self.keys = [key] + self.keys[:index] + self.keys[index+1:]
        else:
            if len(self.keys) < self.capacity:
                self.key_dict[key] = value
                self.keys = [key] + self.keys
            else:
                k = self.keys.pop()
                del self.key_dict[k]
                self.key_dict[key] = value
                self.keys = [key] + self.keys
        # print("put--key:", key, "value:", value, "keys:", self.keys, "dict:", self.key_dict)

def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

if __name__ == "__main__":
    main()
