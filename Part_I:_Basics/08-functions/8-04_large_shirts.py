# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. # Make a large shirt and
# a medium shirt with the default message, and a shirt of any size with a different
# message.


def make_shirt(size="large", text="I love Python"):
    """Functions that accepts a size and text of a message that should be printed on the shirt"""  # noqa: E501
    print("Size: " + size.title())
    print("Text: " + text)


make_shirt()
make_shirt("medium")
make_shirt(text="I love JS", size="small")
