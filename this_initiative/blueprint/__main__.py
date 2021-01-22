import blueprint.runner
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process blueprint")
    parser.add_argument(
        "action",
        help="apply or destroy blueprint's resources"
    )

    args = parser.parse_args()
    # print(args)
    blueprint.runner.run(**vars(args))