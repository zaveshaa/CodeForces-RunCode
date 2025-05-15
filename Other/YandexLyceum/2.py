# WRONG
import asyncio
from PIL import Image


async def VoiceOfTheVoid(filename):
    print(f"Start {filename}")

    img = Image.open(filename).convert("RGB")
    width, height = img.size
    total_pixels = width * height

    brightness_sum = 0

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            brightness_sum += r + g + b

    avg_brightness = brightness_sum / total_pixels if total_pixels else 0
    await asyncio.sleep(0.1)

    color_counter = {}
    bright_count = 0
    quadrants = {"I": 0, "II": 0, "III": 0, "IV": 0}
    half_w, half_h = width // 2, height // 2

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            brightness = r + g + b
            if brightness > avg_brightness:
                bright_count += 1
                color = (r, g, b)
                color_counter[color] = color_counter.get(color, 0) + 1

                if x < half_w:
                    if y < half_h:
                        quadrants["II"] += 1
                    else:
                        quadrants["III"] += 1
                else:
                    if y < half_h:
                        quadrants["I"] += 1
                    else:
                        quadrants["IV"] += 1

    if bright_count == 0:
        percent = 0
        amount = 0
        quarter = "I"
    else:
        most_common_color = max(color_counter.items(), key=lambda i: i[1])[0]
        count_most_common = color_counter[most_common_color]
        percent = (count_most_common * 1000) // bright_count
        amount = (bright_count * 100) // total_pixels
        max_q = max(quadrants.items(), key=lambda q: (-q[1], q[0]))
        quarter = max_q[0]

    print(f"Done {filename}, percent {percent}")
    print(f"Done {filename}, amount {amount}")
    print(f"Done {filename}, quarter {quarter}")
    print(f"Ready {filename}")

    return (filename, percent, amount, quarter)


async def asteroids(*filenames):
    tasks = [VoiceOfTheVoid(fn) for fn in filenames]
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    import asyncio
    data = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    result = asyncio.run(asteroids(*data))
    print(result)
