def length_of_longest_substring_two_distinct(s: str) -> int:
    # 使用哈希表来存储窗口中每个字符的最新索引
    char_index_map = {}
    left = 0  # 窗口的左边界
    max_length = 0  # 最长子串的长度

    # 遍历字符串
    for right in range(len(s)):
        char_index_map[s[right]] = right  # 更新字符的最新索引

        # 如果窗口中的字符种类超过两种，缩小窗口
        if len(char_index_map) > 2:
            # 找到窗口中最左侧字符的索引，并从哈希表中移除
            leftmost_char_index = min(char_index_map.values())
            del char_index_map[s[leftmost_char_index]]
            left = leftmost_char_index + 1  # 移动窗口的左边界

        # 更新最长子串长度
        max_length = max(max_length, right - left + 1)

    return max_length

# 测试示例
test_str = "ecefawsdwafvababababababa"
length_of_longest_substring_two_distinct(test_str)

