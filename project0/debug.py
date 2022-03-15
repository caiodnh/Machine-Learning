
def get_sum_metrics(predictions, metrics=[]):
    # new_metrics = [lambda x: x, lambda x: x + 1, lambda x: x + 2]
    # metrics = metrics + new_metrics

    breakpoint()
    for i in range(3):
        metrics.append(lambda x: x + i)

    # metrics.append(lambda x: x)
    # metrics.append(lambda x: x + 1)
    # metrics.append(lambda x: x + 2)

    sum_metrics = 0
    for metric in metrics:
        # print(metric(0))
        sum_metrics += metric(predictions)

    return sum_metrics


def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9

if __name__ == "__main__":
    main()
