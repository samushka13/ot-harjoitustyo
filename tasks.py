from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage report -m")

@task(coverage)
def coverage_report_html(ctx):
    ctx.run("coverage html")

@task(coverage)
def coverage_report_xml(ctx):
    ctx.run("coverage xml")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("poetry run invoke format")