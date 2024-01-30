def human_size(bytes):
    """ Returns a human readable string representation of bytes in KB, MB, or GB """
    size = float(bytes)

    if size < 1024:
        return "{:.2f} KB".format(size)
    elif size < 1024**2:
        return "{:.2f} MB".format(size / 1024.0)
    else:
        return "{:.2f} GB".format(size / (1024.0**2))
