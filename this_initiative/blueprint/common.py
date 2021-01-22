from subprocess import run
import sys
import logging
import yaml
import jinja2

log = logging.getLogger(__name__)


def cmd(cmd_line, cwd=None, ignore_error=False, input=None, yaml_output=False):
    log.debug(f"run cmd '{cmd_line}'")
    proc = run(
        args=cmd_line.split(),
        input=input,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0 and not ignore_error:
        log.fatal(f"error executing '{cmd_line}' with exit_code '{proc.returncode}'")
    output = proc.stdout #.decode(sys.stdout.encoding)
    if yaml_output:
        output = yaml.safe_load(output)
    return output


def from_template(filepath, **kwargs):
    templateLoader = jinja2.FileSystemLoader(searchpath=".")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(filepath)
    return template.render(**kwargs)

def from_yaml_template(filepath, **kwargs):
    text = from_template(filepath, **kwargs)
    return yaml.safe_load(text)
