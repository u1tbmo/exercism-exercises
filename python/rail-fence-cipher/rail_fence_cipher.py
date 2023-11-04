def encode(message: str, rails: int) -> str:
    if rails < 2:
        return message

    res = ["" for _ in range(rails)]
    direction = -1
    current_rail = 0

    for char in message:
        res[current_rail] += char

        if current_rail == 0 or current_rail == rails - 1:
            direction *= -1

        current_rail += direction

    return "".join(res)


def decode(encoded_message: str, rails: int) -> str:
    if rails < 2:
        return encoded_message

    decoded = [""] * len(encoded_message)
    n = len(encoded_message)
    cycle_len = 2 * rails - 2

    for rail in range(rails):
        i = rail
        j = cycle_len - rail

        while i < n:
            decoded[i] = encoded_message[0]
            encoded_message = encoded_message[1:]
            i += cycle_len

            if rail != 0 and rail != rails - 1 and j < n:
                decoded[j] = encoded_message[0]
                encoded_message = encoded_message[1:]
                j += cycle_len

    return "".join(decoded)
