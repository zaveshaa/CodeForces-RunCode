import asyncio


class Gift:
    def __init__(self, name, pick_time, wrap_time):
        self.name = name
        self.pick_time = pick_time
        self.wrap_time = wrap_time
        self.total_time = pick_time + wrap_time

    def __str__(self):
        return self.name


async def buy_gift(gift):
    print(f"Buy {gift}")
    await asyncio.sleep(gift.pick_time // 100)
    await asyncio.sleep(gift.wrap_time // 100)
    print(f"Got {gift}")


def sort_gifts(gifts):
    return sorted(gifts, key=lambda g: (-g.total_time, g.name))


async def stop(stop_num, available_time, gifts):
    print(f"Buying gifts at {stop_num} stop")
    possible = []
    total_spent = 0

    for gift in sorted(gifts, key=lambda g: (-g.total_time, g.name)):
        if gift.pick_time + total_spent <= available_time and gift in gifts:
            possible.append(gift)
            total_spent += gift.pick_time
            gifts.remove(gift)

    tasks = [buy_gift(gift) for gift in possible]
    if tasks:
        await asyncio.gather(*tasks)

    print(f"Arrive from {stop_num} stop")


async def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    stops = []
    i = 0
    while i < len(data) and data[i].strip() != '':
        parts = list(map(int, data[i].split()))
        stops.append((parts[0], parts[1]))
        i += 1

    i += 1
    gifts = []
    while i < len(data) and data[i].strip() != '':
        name, pt, wt = data[i].split()
        pt = int(pt)
        wt = int(wt)
        gifts.append(Gift(name, pt, wt))
        i += 1

    current_time = 0
    stop_number = 1

    for departure_time, ride_time in stops:
        time_at_stop = departure_time - current_time
        await stop(stop_number, time_at_stop, gifts)
        current_time += ride_time
        stop_number += 1

    if gifts:
        print("Buying gifts after arrival")
        tasks = [buy_gift(gift) for gift in gifts]
        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
