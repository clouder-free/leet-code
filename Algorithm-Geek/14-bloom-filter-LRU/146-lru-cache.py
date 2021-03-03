# -*- coding: utf-8 -*-

class Solution(object):

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
            self.keys = [key] + self.keys[:index] + self.keys[index + 1:]
        else:
            if len(self.keys) < self.capacity:
                self.key_dict[key] = value
                self.keys = [key] + self.keys
            else:
                k = self.keys.pop()
                del self.key_dict[k]
                self.key_dict[key] = value
                self.keys = [key] + self.keys


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
