#!/usr/bin/env python3

def random_emoji():
    # ranges were chosen based on where most emojis are
    ranges = [
        (0x1F600, 0x1F64F),  # Emoticons
        (0x1F300, 0x1F5FF),  # Misc Symbols and Pictographs
        (0x1F680, 0x1F6FF),  # Transport and Map
        (0x2600, 0x26FF),    # Misc symbols
        (0x2700, 0x27BF),    # Dingbats
        (0x1F1E6, 0x1F1FF),  # Flags
        (0x1F191, 0x1F251),  # Misc
        (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
        (0x200D, 0x200D),    # Zero Width Joiner
        (0x238C, 0x2454),    # Misc items
        (0x20D0, 0x20FF),    # Combining Diacritical Marks for Symbols
        (0x1F000, 0x1F02B),  # Mahjong tiles
    ]
    
    while True:
        range_ = rand.choice(ranges)
        emoji_code = rand.randint(range_[0], range_[1])
        emoji = chr(emoji_code)
        if emoji.isprintable():
            return emoji


if __name__ == '__main__':
    print(random_emoji())
