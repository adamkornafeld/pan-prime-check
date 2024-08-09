import click
import pan


@click.command()
def check_pan() -> int:
    """Verify if a payment card PAN is a prime number"""
    n = click.prompt('Enter PAN', type=int)

    check(n)
    return 0


def check(n: int) -> None:
    r = pan.check(n)
    print()
    match r:
        case pan.CheckResult.NotPAN:
            print("Not a PAN\n")
        case pan.CheckResult.PAN:
            print("Valid PAN but not a prime\n")
        case pan.CheckResult.PrimePAN:
            print("Valid PAN and a prime\n")


if __name__ == '__main__':
    check_pan()
