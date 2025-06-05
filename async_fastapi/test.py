# import time 


# def task(name):
#     time.sleep(3)

# start_time = time.perf_counter()

# task("A")
# task("B")

# end_time = time.perf_counter()

# print(f"Finished in {end_time - start_time:.2f} seconds")

############################################################

# import time
# import asyncio

# async def task(name):
#     await asyncio.sleep(3)
#     print(f"Task {name} finished")

# async def main():
#     await asyncio.gather(task("A"), task("B"))

# start_time = time.perf_counter()
# asyncio.run(main())
# end_time = time.perf_counter()
# print(f"Finished in {end_time - start_time:.2f} seconds")