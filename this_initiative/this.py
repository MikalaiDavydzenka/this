import this.lxd.profile
import logging

log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # log.error("error")
    # log.debug("debug")
    # log.info("info")
    # log.fatal("fatal")

    this.lxd.profile.list()