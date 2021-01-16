
from envparse import Env
import click

env = Env(
  LOG_LEVEL=dict(cast=str, default='info'),
)

@click.command()
@click.option("--log-level", default=env.str("LOG_LEVEL"))
def main(log_level):
    print("Clickapp...\n")
    print(log_level)


if __name__ == "__main__":
    main()

