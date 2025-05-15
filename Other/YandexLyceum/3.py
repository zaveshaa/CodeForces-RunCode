# NO
import asyncio


async def process_plant(plant, soak_time, germination_time, rooting_time):
    print(f"0 Beginning of sowing the {plant} plant")

    print(f"1 Soaking of the {plant} started")

    fertilize_task = asyncio.create_task(fertilize(plant))
    pest_control_task = asyncio.create_task(treat_pests(plant))

    await asyncio.sleep(soak_time / 1000)
    print(f"2 Soaking of the {plant} is finished")

    print(f"3 Shelter of the {plant} is supplied")

    germinate_task = asyncio.create_task(
        asyncio.sleep(germination_time / 1000))

    await germinate_task
    print(f"4 Shelter of the {plant} is removed")

    print(f"5 The {plant} has been transplanted")

    await asyncio.sleep(rooting_time / 1000)
    print(f"6 The {plant} has taken root")

    await fertilize_task
    await pest_control_task

    print(f"9 The seedlings of the {plant} are ready")


async def fertilize(plant):
    print(f"7 Application of fertilizers for {plant}")
    await asyncio.sleep(3 / 1000)
    print(f"7 Fertilizers for the {plant} have been introduced")


async def treat_pests(plant):
    print(f"8 Treatment of {plant} from pests")
    await asyncio.sleep(5 / 1000)
    print(f"8 The {plant} is treated from pests")


async def sowing(*plants_data):
    tasks = [process_plant(*data) for data in plants_data]
    await asyncio.gather(*tasks)

data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
asyncio.run(sowing(*data))
