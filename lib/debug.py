#!/usr/bin/env python3

from parrot import parrot

if __name__ == '__main__':
    # Example calls to test the function
    print("Calling parrot with default:")
    parrot()

    print("\nCalling parrot with a custom message:")
    parrot("Polly wants a cracker!")

    # Optional debugging session
    import ipdb; ipdb.set_trace()
