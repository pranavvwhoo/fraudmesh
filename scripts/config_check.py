from omegaconf import OmegaConf


def main() -> None:
    config = OmegaConf.load("configs/config.yaml")
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()
