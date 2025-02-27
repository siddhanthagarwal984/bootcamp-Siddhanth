# Using Generators

## Problem Understanding
Convert the custom file reading iterator into a generator that yields lines from a file.

## Approach & Methodology
- Demonstrate its usage with a sample file.
- Explain the benefits of using generators over traditional iterators.
- Provide examples of using generators in practice.

## LLMs Used
GPT-4 was used to assist in creating a file generator.

## Prompts & Responses
**1. How can I convert an iterator into a generator in Python?**  
Use the `yield` statement instead of `return` in your iterator methods.

**2. What are the advantages of using generators?**  
Generators are more memory efficient as they yield items one at a time and do not store the entire dataset in memory.

**3. Can I use a for loop with my generator?**  
Yes, you can use a for loop to iterate over your generator just like any other iterable.
