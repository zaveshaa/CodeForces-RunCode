import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--per-day', type=float, dest='per_day')
    parser.add_argument('--per-week', type=float, dest='per_week')
    parser.add_argument('--per-month', type=float, dest='per_month')
    parser.add_argument('--per-year', type=float, dest='per_year')
    parser.add_argument(
        '--get-by', choices=['day', 'month', 'year'], dest='get_by')

    args = parser.parse_args()

    daily_total = 0.0

    if args.per_day is not None:
        daily_total += args.per_day
    if args.per_week is not None:
        daily_total += args.per_week / 7
    if args.per_month is not None:
        daily_total += args.per_month / 30
    if args.per_year is not None:
        daily_total += args.per_year / 360

    period = args.get_by or 'day'

    if period == 'day':
        result = daily_total
    elif period == 'month':
        result = daily_total * 30
    else:
        result = daily_total * 360

    print(int(result))


if __name__ == '__main__':
    main()
