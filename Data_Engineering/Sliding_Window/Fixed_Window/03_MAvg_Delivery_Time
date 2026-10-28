'''
Moving average delivery time
Given delivery times, calculate the moving average of every k consecutive deliveries.
'''


def moving_average(times, k):
    if k <= 0 or k > len(times):
        return []

    result = []
    window_sum = 0

    for right in range(len(times)):
        window_sum += times[right]

        if right >= k:
            window_sum -= times[right - k]

        if right >= k - 1:
            result.append(round(window_sum / k, 2))

    return result


print(moving_average([20, 30, 25, 40, 35], 3))
# [25.0, 31.67, 33.33]






