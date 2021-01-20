from subprocess import run
import sys
import logging
import yaml
import jinja2

log = logging.getLogger(__name__)


def cmd(cmd_line, cwd=None, ignore_error=False, input=None, yaml_output=False):
    log.info(f"run cmd '{cmd_line}'")
    proc = run(
        args=cmd_line.split(),
        input=input,
        capture_output=True,
    )
    if proc.returncode != 0 and not ignore_error:
        log.fatal(f"error executing '{cmd}' with exit_code '{proc.returncode}'")
    output = proc.stdout.decode(sys.stdout.encoding)
    if yaml_output:
        output = yaml.safe_load(output)
    return output


def template(filename):
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(filename)
    return template.render()

def from_yaml(text):
    return yaml.dump(text)
