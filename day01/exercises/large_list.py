
def optimized_memory_function_with_lists():
    chunk_size = 100  # Define a chunk size
    total_sum = 0

    for _ in range(10):  # Process 10 chunks
        chunk = [[[1 for _ in range(chunk_size)] for _ in range(chunk_size)] for _ in range(chunk_size)]
        chunk_sum = sum(sum(sum(sublist) for sublist in inner_list) for inner_list in chunk)
        total_sum += chunk_sum

    return total_sum
